#!/usr/bin/env python3
"""
Mac Photo Migrator - Simple App Launcher
アプリケーションとして実行するためのシンプルなランチャー
"""

import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

def main():
    # アプリケーションのベースディレクトリを取得
    if getattr(sys, 'frozen', False):
        # py2appでビルドされた場合
        app_dir = Path(sys.executable).parent.parent / "Resources"
    else:
        # 通常のPython実行の場合
        app_dir = Path(__file__).parent
    
    # スクリプトのパスを設定
    gui_script = app_dir / "scripts" / "migrate_photos_gui.py"
    
    # GUIスクリプトが存在しない場合の対処
    if not gui_script.exists():
        # 開発環境の場合
        gui_script = Path(__file__).parent / "scripts" / "migrate_photos_gui.py"
    
    if not gui_script.exists():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "エラー",
            f"移行スクリプトが見つかりません:\n{gui_script}"
        )
        sys.exit(1)
    
    # Pythonコマンドを決定
    python_cmd = sys.executable
    
    # GUIスクリプトを実行
    try:
        subprocess.run([python_cmd, str(gui_script)], check=True)
    except subprocess.CalledProcessError as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "エラー",
            f"アプリケーションの起動に失敗しました:\n{e}"
        )
        sys.exit(1)
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "エラー",
            f"予期しないエラーが発生しました:\n{e}"
        )
        sys.exit(1)

if __name__ == "__main__":
    main()