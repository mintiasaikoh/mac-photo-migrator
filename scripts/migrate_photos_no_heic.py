#!/usr/bin/env python3
"""
Mac写真.app → Windows 移行スクリプト（HEIC変換なし版）
メタデータ（位置情報・日付）を保持したまま写真をコピー
"""

import osxphotos
import shutil
from pathlib import Path
from datetime import datetime
import json
import os
import sys
import piexif

# 設定
LIBRARY_PATH = "/Volumes/SSD/写真ライブラリ.photoslibrary"
OUTPUT_PATH = "/Volumes/SUNEAST/photo"

# 統計情報
stats = {
    'total': 0,
    'success': 0,
    'failed': 0,
    'skipped': 0,
    'raw_copied': 0,
    'metadata_preserved': 0
}

# エラーログ
errors = []

def get_unique_path(path):
    """重複しないファイルパスを生成"""
    if not path.exists():
        return path
    
    counter = 1
    stem = path.stem
    suffix = path.suffix
    parent = path.parent    
    while path.exists():
        path = parent / f"{stem}_{counter}{suffix}"
        counter += 1
    
    return path

def copy_with_metadata(source_path, dest_path, photo):
    """メタデータを保持しながらファイルをコピー"""
    try:
        # ファイルをコピー
        shutil.copy2(source_path, dest_path)
        
        # EXIF情報を保持（JPEGの場合）
        if source_path.suffix.lower() in ['.jpg', '.jpeg']:
            try:
                # 位置情報がある場合、EXIFに確実に保存
                if photo.location:
                    exif_data = piexif.load(str(source_path))
                    
                    # GPS情報を設定
                    gps_ifd = {
                        piexif.GPSIFD.GPSLatitudeRef: 'N' if photo.location[0] >= 0 else 'S',
                        piexif.GPSIFD.GPSLatitude: [(abs(photo.location[0]), 1)],
                        piexif.GPSIFD.GPSLongitudeRef: 'E' if photo.location[1] >= 0 else 'W',
                        piexif.GPSIFD.GPSLongitude: [(abs(photo.location[1]), 1)]
                    }
                    
                    exif_data['GPS'] = gps_ifd
                    exif_bytes = piexif.dump(exif_data)
                    piexif.insert(exif_bytes, str(dest_path))
                    stats['metadata_preserved'] += 1
            except Exception as e:
                # EXIF処理でエラーが出ても続行
                pass
        
        # ファイル日時を撮影日時に設定
        if photo.date:
            timestamp = photo.date.timestamp()
            os.utime(dest_path, (timestamp, timestamp))
        
        return True
    except Exception as e:
        print(f"コピーエラー: {e}")
        return False

def migrate_photos():
    """メイン移行処理"""
    print(f"\n写真ライブラリを開いています: {LIBRARY_PATH}")
    print("※初回は時間がかかる場合があります...")
    
    # osxphotosでライブラリを開く
    photosdb = osxphotos.PhotosDB(LIBRARY_PATH)
    photos = photosdb.photos()
    
    stats['total'] = len(photos)
    print(f"\n合計 {stats['total']:,} 枚の写真/動画が見つかりました")
    print("-" * 60)
    
    # 出力ディレクトリ作成
    Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)
    
    # 各写真を処理
    start_time = datetime.now()
    
    for idx, photo in enumerate(photos, 1):
        try:
            # ファイル情報取得
            if not photo.path or not Path(photo.path).exists():
                stats['skipped'] += 1
                continue
            
            source_path = Path(photo.path)
            
            # 日付でフォルダ分け
            date = photo.date or datetime.now()
            year = date.strftime("%Y")
            month = date.strftime("%m_%B")
            
            # RAWファイルの判定
            is_raw = photo.israw or source_path.suffix.lower() in ['.raf', '.raw', '.cr2', '.cr3', '.nef', '.arw', '.dng']
            
            # 出力ディレクトリ
            if is_raw:
                out_dir = Path(OUTPUT_PATH) / "RAW" / year / month
                stats['raw_copied'] += 1
            else:
                out_dir = Path(OUTPUT_PATH) / year / month
            
            out_dir.mkdir(parents=True, exist_ok=True)
            
            # ファイル名（元のファイル名を使用）
            filename = photo.original_filename or source_path.name
            output_path = out_dir / filename
            output_path = get_unique_path(output_path)
            
            # メタデータを保持してコピー
            if copy_with_metadata(source_path, output_path, photo):
                stats['success'] += 1
            else:
                stats['failed'] += 1
            
            # 進捗表示（100枚ごと）
            if idx % 100 == 0:
                elapsed = (datetime.now() - start_time).total_seconds()
                rate = idx / elapsed if elapsed > 0 else 0
                remaining = (stats['total'] - idx) / rate if rate > 0 else 0
                
                print(f"進捗: {idx:,}/{stats['total']:,} ({idx/stats['total']*100:.1f}%) "
                      f"- {rate:.1f} 枚/秒 - 残り約 {int(remaining/60)} 分")
                
                # 位置情報保持の状況も表示
                if stats['metadata_preserved'] > 0:
                    print(f"  位置情報保持: {stats['metadata_preserved']:,} 枚")
        
        except Exception as e:
            stats['failed'] += 1
            errors.append({
                'index': idx,
                'path': str(photo.path) if photo.path else 'Unknown',
                'error': str(e),
                'location': photo.location if photo.location else None
            })
            if idx <= 10:  # 最初の10件はエラーを表示
                print(f"エラー (写真 {idx}): {e}")
    
    # 完了
    elapsed = (datetime.now() - start_time).total_seconds()
    print("\n" + "=" * 60)
    print("移行完了！")
    print("=" * 60)
    print(f"総ファイル数: {stats['total']:,}")
    print(f"成功: {stats['success']:,}")
    print(f"失敗: {stats['failed']:,}")
    print(f"スキップ: {stats['skipped']:,}")
    print(f"RAWファイル: {stats['raw_copied']:,}")
    print(f"位置情報保持: {stats['metadata_preserved']:,}")
    print(f"処理時間: {int(elapsed/60)} 分 {int(elapsed%60)} 秒")
    print("=" * 60)
    
    # レポート保存
    report = {
        'migration_date': datetime.now().isoformat(),
        'source': LIBRARY_PATH,
        'destination': OUTPUT_PATH,
        'statistics': stats,
        'processing_time_seconds': elapsed,
        'heic_conversion': False,
        'errors': errors[:100]  # 最初の100件のみ
    }
    
    report_path = Path(OUTPUT_PATH) / "migration_report_no_heic.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n移行レポートを保存しました: {report_path}")
    
    if errors:
        print(f"\n⚠️  {len(errors)} 件のエラーが発生しました。")
        print("詳細は migration_report_no_heic.json を確認してください。")

if __name__ == "__main__":
    print("Mac写真ライブラリ → Windows 移行ツール（HEIC変換なし版）")
    print("=" * 60)
    print(f"ライブラリ: {LIBRARY_PATH}")
    print(f"出力先: {OUTPUT_PATH}")
    print("HEIC変換: 無効（オリジナルファイルをそのままコピー）")
    print("メタデータ: 保持（位置情報・日付情報）")
    print("=" * 60)
    
    # 確認
    response = input("\n移行を開始しますか？ (y/n): ")
    if response.lower() == 'y':
        migrate_photos()
    else:
        print("キャンセルしました。")