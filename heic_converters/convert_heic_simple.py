#!/usr/bin/env python3
"""
HEICファイルをJPEGに変換するスクリプト（簡易版）
"""

import os
from pathlib import Path
import subprocess
from datetime import datetime

# 設定
SOURCE_DIR = "/Volumes/SUNEAST/photo"

def convert_heic_with_sips(heic_path, jpeg_path):
    """macOS標準のsipsコマンドでHEIC→JPEG変換"""
    try:
        cmd = [
            'sips', 
            '-s', 'format', 'jpeg',
            '-s', 'formatOptions', '95',
            str(heic_path),
            '--out', str(jpeg_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"変換エラー: {e}")
        return False

print("HEICファイルの検索中...")

# HEICファイルを検索
heic_count = 0
for root, dirs, files in os.walk(SOURCE_DIR):
    if 'RAW' in root:
        continue
    for file in files:
        if file.lower().endswith(('.heic', '.heif')):
            heic_count += 1

print(f"\n{heic_count:,} 個のHEICファイルが見つかりました")

if heic_count == 0:
    print("変換するファイルがありません")
    exit()

response = input("\nJPEGに変換しますか？(y/n): ")
if response.lower() != 'y':
    print("キャンセルしました")
    exit()

# 変換実行
print("\n変換を開始します...")
start_time = datetime.now()
success = 0
failed = 0
processed = 0

for root, dirs, files in os.walk(SOURCE_DIR):
    if 'RAW' in root:
        continue
    
    for file in files:
        if file.lower().endswith(('.heic', '.heif')):
            processed += 1
            heic_path = Path(root) / file
            jpeg_path = heic_path.with_suffix('.jpg')
            
            # 既存のJPEGはスキップ
            if jpeg_path.exists():
                continue
            
            # 変換
            if convert_heic_with_sips(heic_path, jpeg_path):
                success += 1
                # ファイル日時をコピー
                stat = os.stat(heic_path)
                os.utime(jpeg_path, (stat.st_atime, stat.st_mtime))
            else:
                failed += 1
                print(f"失敗: {file}")
            
            # 進捗表示
            if processed % 100 == 0:
                print(f"進捗: {processed}/{heic_count} ({processed/heic_count*100:.1f}%)")

# 完了
elapsed = (datetime.now() - start_time).total_seconds()
print(f"\n変換完了！")
print(f"成功: {success}")
print(f"失敗: {failed}")
print(f"処理時間: {int(elapsed/60)}分 {int(elapsed%60)}秒")
