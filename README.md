# Mac Photo Migrator

<div align="center">
  <h1>Mac写真移行ツール</h1>
  <p>Macの写真.appライブラリからWindowsへ、メタデータを保持したまま写真を移行</p>
  
  [![GitHub release](https://img.shields.io/github/v/release/mintiasaikoh/mac-photo-migrator)](https://github.com/mintiasaikoh/mac-photo-migrator/releases)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Platform](https://img.shields.io/badge/platform-macOS-blue.svg)](https://www.apple.com/macos/)
  
  <p>
    <strong>最新バージョン: v1.0.0</strong> | 
    <a href="https://github.com/mintiasaikoh/mac-photo-migrator/releases/latest">ダウンロード (23.2MB)</a>
  </p>
</div>

## ✨ 特徴

- 📸 **メタデータ保持**: EXIF情報、撮影日時、GPS位置情報を維持
- 📁 **自動整理**: 年/月フォルダで自動分類
- 🖼️ **HEIC対応**: HEIC形式のまま保存（Windows 10/11対応）
- 🎨 **使いやすいGUI**: グラフィカルインターフェースで簡単操作
- 📊 **進捗表示**: リアルタイムで処理状況を確認
- 📝 **詳細レポート**: 移行結果をJSON形式で保存

## 🚀 インストール

### 方法1: リリース版アプリを使用（推奨）

1. [最新リリース](https://github.com/mintiasaikoh/mac-photo-migrator/releases/latest)から`Mac.Photo.Migrator.app.zip`をダウンロード
2. ダウンロードしたZIPファイルを解凍
3. `Mac Photo Migrator.app`をApplicationsフォルダにドラッグ
4. アプリを起動（初回起動時は右クリック→「開く」を選択）

> **注意**: macOSのセキュリティ機能により、初回起動時は警告が表示されます。  
> システム環境設定 > セキュリティとプライバシー で許可するか、右クリック→「開く」で起動してください。

### 方法2: ソースコードから実行

```bash
# リポジトリをクローン
git clone https://github.com/mintiasaikoh/mac-photo-migrator.git
cd mac-photo-migrator

# 必要なパッケージをインストール
pip install -r requirements.txt

# GUIアプリを起動
python scripts/migrate_photos_gui.py
```

### 方法3: ソースコードからアプリをビルド

```bash
# リポジトリをクローン
git clone https://github.com/mintiasaikoh/mac-photo-migrator.git
cd mac-photo-migrator

# 必要なパッケージをインストール
pip install -r requirements.txt
pip install pyinstaller

# PyInstallerでアプリをビルド
pyinstaller --onefile --windowed --name "Mac Photo Migrator" scripts/migrate_photos_gui.py

# ビルドされたアプリを実行
open "dist/Mac Photo Migrator.app"
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

- macOS 10.15 Catalina以降
- Python 3.7以降（ソースコードから実行する場合）
- 写真.appのライブラリへのアクセス権限

> **注意**: リリース版のアプリ（.app）を使用する場合、Pythonのインストールは不要です。

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

## 🚀 リリース履歴

- **v1.0.0** (2025-06-09) - 初回リリース
  - GUI版アプリケーション
  - メタデータ保持機能
  - 年/月フォルダ自動整理
  - HEIC形式サポート

## 🤝 貢献

プルリクエストは歓迎します。大きな変更の場合は、まずissueを作成して変更内容について議論してください。

## 📧 サポート

問題が発生した場合は、[Issues](https://github.com/mintiasaikoh/mac-photo-migrator/issues)で報告してください。