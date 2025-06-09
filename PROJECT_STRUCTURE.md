# 📁 プロジェクト構造 / Project Structure

```
mac_photos_to_windows/
├── 📄 README.md           # メインドキュメント (Main documentation)
├── 📄 RELEASE_NOTES.md    # リリースノート (Release notes)
├── 📄 LICENSE             # MITライセンス (MIT License)
├── 📄 requirements.txt    # Python依存関係 (Python dependencies)
├── 📄 setup.py           # アプリビルド設定 (App build config)
├── 🚀 start.py           # アプリ起動スクリプト (App launcher)
├── 📂 scripts/           # メインスクリプト (Main scripts)
│   ├── migrate_photos_gui.py      # GUI版
│   ├── migrate_photos_no_heic.py  # HEIC変換なし版
│   ├── migrate_photos.py          # HEIC変換あり版
│   └── migrate_photos_auto.py     # 自動実行版
├── 📂 heic_converters/   # HEIC変換ツール (HEIC converters)
├── 📂 build_tools/       # ビルド関連ツール (Build tools)
│   ├── build_app.sh      # アプリビルドスクリプト
│   ├── create_icns.sh    # アイコン作成スクリプト
│   ├── create_icon.py    # アイコン生成Python
│   └── *.spec           # PyInstallerスペック
└── 📂 logs/             # ログファイル (Log files)
```

## 🚀 クイックスタート / Quick Start

```bash
# GUI版を起動 / Launch GUI version
python start.py

# または直接実行 / Or run directly
python scripts/migrate_photos_gui.py
```