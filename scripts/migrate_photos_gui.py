#!/usr/bin/env python3
"""
Mac Photos to Windows Migration Tool - GUI Version (No HEIC Conversion)
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import osxphotos
import shutil
from pathlib import Path
from datetime import datetime
import json
import os
import threading
import queue
import piexif

class PhotoMigratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mac Photos to Windows")
        self.root.geometry("800x600")
        
        # 変数
        self.library_path = tk.StringVar(value="/Volumes/SSD/写真ライブラリ.photoslibrary")
        self.output_path = tk.StringVar(value="/Volumes/SUNEAST/photo")
        self.is_running = False
        self.thread = None
        self.queue = queue.Queue()
        
        # 統計情報
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,            'raw_copied': 0,
            'metadata_preserved': 0
        }
        
        self.setup_ui()
        self.update_queue()
        
    def setup_ui(self):
        # メインフレーム
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 設定セクション
        settings_frame = ttk.LabelFrame(main_frame, text="設定", padding="10")
        settings_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # ライブラリパス
        ttk.Label(settings_frame, text="写真ライブラリ:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(settings_frame, textvariable=self.library_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(settings_frame, text="選択", command=self.select_library).grid(row=0, column=2)
        
        # 出力先パス
        ttk.Label(settings_frame, text="出力先:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(settings_frame, textvariable=self.output_path, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(settings_frame, text="選択", command=self.select_output).grid(row=1, column=2)
        
        # 実行ボタン
        self.start_button = ttk.Button(main_frame, text="移行開始", command=self.start_migration)
        self.start_button.grid(row=1, column=0, pady=10)
        
        self.stop_button = ttk.Button(main_frame, text="中止", command=self.stop_migration, state="disabled")
        self.stop_button.grid(row=1, column=1, pady=10)
        
        # プログレスバー
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # 状態表示
        self.status_label = ttk.Label(main_frame, text="準備完了")
        self.status_label.grid(row=3, column=0, columnspan=3, pady=5)
        
        # ログエリア
        log_frame = ttk.LabelFrame(main_frame, text="ログ", padding="10")
        log_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=70)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # ウィンドウのリサイズ設定
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
    
    def select_library(self):
        path = filedialog.askopenfilename(
            title="写真ライブラリを選択",
            filetypes=[("Photos Library", "*.photoslibrary")]
        )
        if path:
            self.library_path.set(path)
    
    def select_output(self):
        path = filedialog.askdirectory(title="出力先フォルダを選択")
        if path:
            self.output_path.set(path)
    
    def log(self, message):
        """ログメッセージをキューに追加"""
        self.queue.put(('log', message))
    
    def update_progress(self, value, max_value):
        """プログレスバーの更新をキューに追加"""
        self.queue.put(('progress', (value, max_value)))
    
    def update_status(self, status):
        """ステータスの更新をキューに追加"""
        self.queue.put(('status', status))
    
    def update_queue(self):
        """キューからUIを更新"""
        try:
            while True:
                item = self.queue.get_nowait()
                if item[0] == 'log':
                    self.log_text.insert(tk.END, item[1] + '\n')
                    self.log_text.see(tk.END)
                elif item[0] == 'progress':
                    value, max_value = item[1]
                    self.progress['maximum'] = max_value
                    self.progress['value'] = value
                elif item[0] == 'status':
                    self.status_label['text'] = item[1]
                elif item[0] == 'done':
                    self.migration_done()
        except queue.Empty:
            pass
        
        self.root.after(100, self.update_queue)
    
    def start_migration(self):
        if self.is_running:
            return
        
        # パスの確認
        if not Path(self.library_path.get()).exists():
            messagebox.showerror("エラー", "写真ライブラリが見つかりません")
            return
        
        # 実行確認
        result = messagebox.askyesno(
            "確認", 
            f"移行を開始しますか？\n\n"
            f"元: {self.library_path.get()}\n"
            f"先: {self.output_path.get()}"
        )
        
        if not result:
            return
        
        # UI更新
        self.is_running = True
        self.start_button['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.log_text.delete(1.0, tk.END)
        
        # 移行スレッド開始
        self.thread = threading.Thread(target=self.migration_worker)
        self.thread.start()
    
    def stop_migration(self):
        if messagebox.askyesno("確認", "移行を中止しますか？"):
            self.is_running = False
            self.log("移行を中止しています...")
    
    def migration_done(self):
        self.is_running = False
        self.start_button['state'] = 'normal'
        self.stop_button['state'] = 'disabled'
        messagebox.showinfo("完了", "移行が完了しました！")
    
    def get_unique_path(self, path):
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
    
    def copy_with_metadata(self, source_path, dest_path, photo):
        """メタデータを保持しながらファイルをコピー"""
        try:
            # ファイルをコピー
            shutil.copy2(source_path, dest_path)
            
            # EXIF情報を保持（JPEGの場合）
            if source_path.suffix.lower() in ['.jpg', '.jpeg']:
                try:
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
                        self.stats['metadata_preserved'] += 1
                except Exception:
                    pass
            
            # ファイル日時を撮影日時に設定
            if photo.date:
                timestamp = photo.date.timestamp()
                os.utime(dest_path, (timestamp, timestamp))
            
            return True
        except Exception as e:
            self.log(f"コピーエラー: {e}")
            return False
    
    def migration_worker(self):
        """移行処理のワーカースレッド"""
        try:
            # 統計情報リセット
            for key in self.stats:
                self.stats[key] = 0
            
            errors = []
            
            self.log(f"写真ライブラリを開いています: {self.library_path.get()}")
            self.update_status("ライブラリを読み込み中...")
            
            # osxphotosでライブラリを開く
            photosdb = osxphotos.PhotosDB(self.library_path.get())
            photos = photosdb.photos()
            
            self.stats['total'] = len(photos)
            self.log(f"合計 {self.stats['total']:,} 枚の写真/動画が見つかりました")
            
            # 出力ディレクトリ作成
            Path(self.output_path.get()).mkdir(parents=True, exist_ok=True)
            
            # 各写真を処理
            start_time = datetime.now()
            
            for idx, photo in enumerate(photos, 1):
                if not self.is_running:
                    break
                
                try:
                    # ファイル情報取得
                    if not photo.path or not Path(photo.path).exists():
                        self.stats['skipped'] += 1
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
                        out_dir = Path(self.output_path.get()) / "RAW" / year / month
                        self.stats['raw_copied'] += 1
                    else:
                        out_dir = Path(self.output_path.get()) / year / month
                    
                    out_dir.mkdir(parents=True, exist_ok=True)
                    
                    # ファイル名（元のファイル名を使用）
                    filename = photo.original_filename or source_path.name
                    output_path = out_dir / filename
                    output_path = self.get_unique_path(output_path)
                    
                    # メタデータを保持してコピー
                    if self.copy_with_metadata(source_path, output_path, photo):
                        self.stats['success'] += 1
                    else:
                        self.stats['failed'] += 1
                    
                    # 進捗更新
                    self.update_progress(idx, self.stats['total'])
                    
                    # 状態更新（100枚ごと）
                    if idx % 100 == 0:
                        elapsed = (datetime.now() - start_time).total_seconds()
                        rate = idx / elapsed if elapsed > 0 else 0
                        remaining = (self.stats['total'] - idx) / rate if rate > 0 else 0
                        
                        status = f"進捗: {idx:,}/{self.stats['total']:,} ({idx/self.stats['total']*100:.1f}%) - 残り約 {int(remaining/60)} 分"
                        self.update_status(status)
                        self.log(status)
                
                except Exception as e:
                    self.stats['failed'] += 1
                    errors.append({
                        'index': idx,
                        'path': str(photo.path) if photo.path else 'Unknown',
                        'error': str(e)
                    })
            
            # 完了処理
            elapsed = (datetime.now() - start_time).total_seconds()
            
            self.log("\n" + "="*50)
            self.log("移行完了！")
            self.log(f"総ファイル数: {self.stats['total']:,}")
            self.log(f"成功: {self.stats['success']:,}")
            self.log(f"失敗: {self.stats['failed']:,}")
            self.log(f"スキップ: {self.stats['skipped']:,}")
            self.log(f"RAWファイル: {self.stats['raw_copied']:,}")
            self.log(f"位置情報保持: {self.stats['metadata_preserved']:,}")
            self.log(f"処理時間: {int(elapsed/60)} 分 {int(elapsed%60)} 秒")
            
            # レポート保存
            report = {
                'migration_date': datetime.now().isoformat(),
                'source': self.library_path.get(),
                'destination': self.output_path.get(),
                'statistics': self.stats,
                'processing_time_seconds': elapsed,
                'heic_conversion': False,
                'errors': errors[:100]
            }
            
            report_path = Path(self.output_path.get()) / "migration_report_gui.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            
            self.log(f"\n移行レポートを保存しました: {report_path}")
            
            if errors:
                self.log(f"\n⚠️  {len(errors)} 件のエラーが発生しました。")
            
            self.queue.put(('done', None))
            
        except Exception as e:
            self.log(f"\n重大なエラーが発生しました: {e}")
            self.queue.put(('done', None))

def main():
    root = tk.Tk()
    app = PhotoMigratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()