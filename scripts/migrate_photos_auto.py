#!/usr/bin/env python3
"""
Mac写真.app → Windows 移行スクリプト（自動実行版）
"""

import osxphotos
import shutil
from pathlib import Path
from datetime import datetime
import json
import os
import sys

# HEIC変換の確認
try:
    import pyheif
    from PIL import Image
    HEIC_AVAILABLE = True
    print("✓ HEIC→JPEG変換: 有効")
except ImportError:
    HEIC_AVAILABLE = False
    print("× HEIC→JPEG変換: 無効")

# 設定
LIBRARY_PATH = "/Volumes/SSD/写真ライブラリ.photoslibrary"
OUTPUT_PATH = "/Volumes/SUNEAST/photo"
CONVERT_HEIC = True  # HEIC→JPEG変換

# 統計情報
stats = {
    'total': 0,
    'success': 0,
    'failed': 0,
    'skipped': 0,
    'heic_converted': 0,
    'raw_copied': 0
}

# エラーログ
errors = []

def convert_heic_to_jpeg(source_path, output_path, quality=95):
    """HEIC画像をJPEGに変換"""
    try:
        heif_file = pyheif.read(source_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        image.save(output_path, "JPEG", quality=quality)
        return True
    except Exception as e:
        print(f"HEIC変換エラー: {e}")
        return False

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
            
            # HEIC変換処理
            if CONVERT_HEIC and HEIC_AVAILABLE and source_path.suffix.lower() in ['.heic', '.heif']:
                # JPEG名で出力
                output_filename = Path(filename).stem + '.jpg'
                output_path = out_dir / output_filename
                output_path = get_unique_path(output_path)
                
                if convert_heic_to_jpeg(source_path, output_path):
                    stats['heic_converted'] += 1
                else:
                    # 変換失敗時は元ファイルをコピー
                    output_path = out_dir / filename
                    output_path = get_unique_path(output_path)
                    shutil.copy2(source_path, output_path)
            else:
                # 通常のコピー
                output_path = out_dir / filename
                output_path = get_unique_path(output_path)
                shutil.copy2(source_path, output_path)            
            # ファイル日時を撮影日時に設定
            if photo.date:
                timestamp = photo.date.timestamp()
                os.utime(output_path, (timestamp, timestamp))
            
            stats['success'] += 1
            
            # 進捗表示（100枚ごと）
            if idx % 100 == 0:
                elapsed = (datetime.now() - start_time).total_seconds()
                rate = idx / elapsed if elapsed > 0 else 0
                remaining = (stats['total'] - idx) / rate if rate > 0 else 0
                
                print(f"進捗: {idx:,}/{stats['total']:,} ({idx/stats['total']*100:.1f}%) "
                      f"- {rate:.1f} 枚/秒 - 残り約 {int(remaining/60)} 分")
        
        except Exception as e:
            stats['failed'] += 1
            errors.append({
                'index': idx,
                'path': str(photo.path) if photo.path else 'Unknown',
                'error': str(e)
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
    print(f"HEIC変換: {stats['heic_converted']:,}")
    print(f"RAWファイル: {stats['raw_copied']:,}")
    print(f"処理時間: {int(elapsed/60)} 分 {int(elapsed%60)} 秒")
    print("=" * 60)
    
    # レポート保存
    report = {
        'migration_date': datetime.now().isoformat(),
        'source': LIBRARY_PATH,
        'destination': OUTPUT_PATH,
        'statistics': stats,
        'processing_time_seconds': elapsed,
        'errors': errors[:100]  # 最初の100件のみ
    }
    
    report_path = Path(OUTPUT_PATH) / "migration_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n移行レポートを保存しました: {report_path}")

if __name__ == "__main__":
    print("Mac写真ライブラリ → Windows 移行ツール（自動実行）")
    print("=" * 60)
    print(f"ライブラリ: {LIBRARY_PATH}")
    print(f"出力先: {OUTPUT_PATH}")
    print(f"HEIC変換: {'有効' if CONVERT_HEIC and HEIC_AVAILABLE else '無効'}")
    print("=" * 60)
    
    # 自動的に移行開始
    print("\n移行を開始します...")
    migrate_photos()
