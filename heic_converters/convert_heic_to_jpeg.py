#!/usr/bin/env python3
"""
HEICファイルをJPEGに変換するスクリプト
"""

import os
from pathlib import Path
import subprocess
import json
from datetime import datetime

# 設定
SOURCE_DIR = "/Volumes/SUNEAST/photo"
BACKUP_DIR = "/Volumes/SUNEAST/photo_heic_backup"

stats = {
    'total': 0,
    'success': 0,
    'failed': 0
}

def convert_heic_with_sips(heic_path, jpeg_path):
    """macOS標準のsipsコマンドでHEIC→JPEG変換"""
    try:
        # sipsコマンドで変換
        cmd = [
            'sips', 
            '-s', 'format', 'jpeg',
            '-s', 'formatOptions', '95',  # 品質95%
            heic_path,
            '--out', jpeg_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"変換エラー: {e}")
        return False

def find_heic_files():
    """HEICファイルを検索"""
    heic_files = []
    for root, dirs, files in os.walk(SOURCE_DIR):
        # RAWフォルダはスキップ
        if 'RAW' in root:
            continue
        
        for file in files:
            if file.lower().endswith(('.heic', '.heif')):
                heic_files.append(Path(root) / file)
    
    return heic_files

def main():
    print("HEICファイルの検索中...")
    heic_files = find_heic_files()
    stats['total'] = len(heic_files)
    
    print(f"\n{stats['total']:,} 個のHEICファイルが見つかりました")
    
    if stats['total'] == 0:
        print("変換するファイルがありません")
        return
    
    response = input("\nJPEGに変換しますか？(元のHEICファイルは保持されます) (y/n): ")
    if response.lower() != 'y':
        print("キャンセルしました")
        return
    
    print("\n変換を開始します...")
    start_time = datetime.now()
    
    for idx, heic_path in enumerate(heic_files, 1):
        try:
            # JPEG名を作成
            jpeg_path = heic_path.with_suffix('.jpg')
            
            # 既にJPEGが存在する場合はスキップ
            if jpeg_path.exists():
                print(f"スキップ: {jpeg_path.name} (既に存在)")
                continue
            
            # 変換実行
            if convert_heic_with_sips(str(heic_path), str(jpeg_path)):
                stats['success'] += 1
                
                # 元のHEICファイルの日時をJPEGにコピー
                stat = os.stat(heic_path)
                os.utime(jpeg_path, (stat.st_atime, stat.st_mtime))
            else:
                stats['failed'] += 1
                print(f"失敗: {heic_path.name}")
            
            # 進捗表示
            if idx % 100 == 0:
                elapsed = (datetime.now() - start_time).total_seconds()
                rate = idx / elapsed if elapsed > 0 else 0
                remaining = (stats['total'] - idx) / rate if rate > 0 else 0
                
                print(f"進捗: {idx:,}/{stats['total']:,} ({idx/stats['total']*100:.1f}%) "
                      f"- {rate:.1f} 枚/秒 - 残り約 {int(remaining/60)} 分")
    
    # 完了
    elapsed = (datetime.now() - start_time).total_seconds()
    print("\n" + "=" * 60)
    print("変換完了！")
    print("=" * 60)
    print(f"総ファイル数: {stats['total']:,}")
    print(f"成功: {stats['success']:,}")
    print(f"失敗: {stats['failed']:,}")
    print(f"処理時間: {int(elapsed/60)} 分 {int(elapsed%60)} 秒")
    
    if stats['success'] > 0:
        print("\n元のHEICファイルを削除しますか？")
        response = input("(削除する場合は 'delete' と入力): ")
        if response == 'delete':
            print("HEICファイルを削除中...")
            for heic_path in heic_files:
                jpeg_path = heic_path.with_suffix('.jpg')
                if jpeg_path.exists():
                    heic_path.unlink()
            print("削除完了")

if __name__ == "__main__":
    main()
