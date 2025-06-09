# Mac Photo Migrator

<div align="center">
  <h1>Mac写真移行ツール</h1>
  <p>Macの写真.appライブラリからWindowsへ、メタデータを保持したまま写真を移行</p>
</div>

## ✨ 特徴

- 📸 **メタデータ保持**: EXIF情報、撮影日時、GPS位置情報を維持
- 📁 **自動整理**: 年/月フォルダで自動分類
- 🖼️ **HEIC対応**: HEIC形式のまま保存（Windows 10/11対応）
- 🎨 **使いやすいGUI**: グラフィカルインターフェースで簡単操作
- 📊 **進捗表示**: リアルタイムで処理状況を確認
- 📝 **詳細レポート**: 移行結果をJSON形式で保存

## 🚀 インストール

### 方法1: ソースコードから実行

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/mac-photo-migrator.git
cd mac-photo-migrator

# 必要なパッケージをインストール
pip install -r requirements.txt

# GUIアプリを起動
python scripts/migrate_photos_gui.py
```

### 方法2: macOSアプリとして実行（開発中）

```bash
# アプリをビルド
python setup.py py2app

# アプリを実行
open dist/Mac\ Photo\ Migrator.app
```

## 📖 使い方

### GUI版（推奨）

1. アプリを起動
2. 「写真ライブラリ」で移行元の`.photoslibrary`ファイルを選択
3. 「出力先」で保存先フォルダを選択
4. 「移行開始」をクリック

### コマンドライン版

```bash
# HEIC変換なし（高速）
python scripts/migrate_photos_no_heic.py

# HEIC→JPEG変換あり
python scripts/migrate_photos.py

# 自動実行版
python scripts/migrate_photos_auto.py
```

## 📁 出力構造

```
出力先/
├── 2024/
│   ├── 01_January/
│   ├── 02_February/
│   └── ...
├── RAW/
│   └── 2024/...
└── migration_report.json
```

## ⚙️ 設定

スクリプト内で以下の設定を変更できます：

```python
LIBRARY_PATH = "/Volumes/SSD/写真ライブラリ.photoslibrary"  # 移行元
OUTPUT_PATH = "/Volumes/SUNEAST/photo"  # 移行先
```

## 🛠️ 必要な環境

- macOS 10.15以降
- Python 3.7以降
- 写真.appのライブラリへのアクセス権限

## 📦 依存パッケージ

- osxphotos - Mac写真ライブラリへのアクセス
- piexif - EXIF情報の処理
- Pillow - 画像処理

## ⚠️ 注意事項

- 初回実行時は写真ライブラリの解析に時間がかかります
- 大量の写真がある場合、処理に数時間かかることがあります
- 移行先に十分な空き容量があることを確認してください
- WindowsでHEICファイルを表示するには「HEIFイメージ拡張機能」が必要です

## 🐛 トラブルシューティング

### 権限エラー
写真ライブラリへのアクセス権限を確認してください。
システム環境設定 > セキュリティとプライバシー > プライバシー > 写真

### パッケージエラー
```bash
pip install -r requirements.txt --upgrade
```

### パスエラー
ライブラリと出力先のパスが正しいか確認してください。

## 📄 ライセンス

MIT License

## 🤝 貢献

プルリクエストは歓迎します。大きな変更の場合は、まずissueを作成して変更内容について議論してください。

## 📧 サポート

問題が発生した場合は、[Issues](https://github.com/yourusername/mac-photo-migrator/issues)で報告してください。