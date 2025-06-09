# Mac Photos to Windows

<div align="center">
  <h1>Mac Photos to Windows</h1>
  <p>
    <strong>🇯🇵 日本語</strong> | <a href="#english">🇬🇧 English</a>
  </p>
  
  [![GitHub release](https://img.shields.io/github/v/release/mintiasaikoh/mac-photo-migrator)](https://github.com/mintiasaikoh/mac-photo-migrator/releases)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Platform](https://img.shields.io/badge/platform-macOS-blue.svg)](https://www.apple.com/macos/)
  
  <p>
    <strong>最新バージョン: v1.0.0</strong> | 
    <a href="https://github.com/mintiasaikoh/mac-photo-migrator/releases/latest">ダウンロード (23.2MB)</a>
  </p>
</div>

---

## 🇯🇵 日本語

### 📝 概要

Mac Photos to Windowsは、Macの写真.appライブラリからWindowsへ、位置情報や撮影日時などのメタデータを保持したまま写真を移行するためのアプリケーションです。

### ✨ 特徴

- 📸 **メタデータ保持**: EXIF情報、撮影日時、GPS位置情報を完全に維持
- 📁 **自動整理**: 年/月フォルダで自動的に分類・整理
- 🖼️ **HEIC対応**: HEIC形式のまま保存（Windows 10/11対応）
- 🎨 **使いやすいGUI**: グラフィカルインターフェースで直感的な操作
- 📊 **進捗表示**: リアルタイムで処理状況を確認可能
- 📝 **詳細レポート**: 移行結果をJSON形式で保存

### 🚀 インストール方法

#### 方法1: リリース版アプリを使用（推奨）

1. [最新リリース](https://github.com/mintiasaikoh/mac-photo-migrator/releases/latest)から`Mac.Photo.Migrator.app.zip`をダウンロード
2. ダウンロードしたZIPファイルを解凍
3. `Mac Photo Migrator.app`をApplicationsフォルダにドラッグ
4. アプリを起動（初回起動時は右クリック→「開く」を選択）

> **注意**: macOSのセキュリティ機能により、初回起動時は警告が表示されます。  
> システム環境設定 > セキュリティとプライバシー で許可するか、右クリック→「開く」で起動してください。

#### 方法2: ソースコードから実行

```bash
# リポジトリをクローン
git clone https://github.com/mintiasaikoh/mac-photo-migrator.git
cd mac-photo-migrator

# 必要なパッケージをインストール
pip install -r requirements.txt

# GUIアプリを起動
python scripts/migrate_photos_gui.py
```

### 📖 使い方

1. **アプリを起動**
2. **「写真ライブラリ」** で移行元の`.photoslibrary`ファイルを選択
3. **「出力先」** で保存先フォルダを選択
4. **「移行開始」** をクリック

### 📁 出力構造

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

### ⚙️ システム要件

- macOS 10.15 Catalina以降
- Python 3.7以降（ソースコードから実行する場合）
- 写真.appのライブラリへのアクセス権限
- 十分なストレージ容量（写真ライブラリの約2倍を推奨）

### ⚠️ 注意事項

- 初回実行時は写真ライブラリの解析に時間がかかります
- 大量の写真がある場合、処理に数時間かかることがあります
- 移行先に十分な空き容量があることを確認してください
- WindowsでHEICファイルを表示するには「HEIFイメージ拡張機能」が必要です
- **使用前に必ず写真ライブラリのバックアップを取ってください**

### 🐛 トラブルシューティング

#### 権限エラー
写真ライブラリへのアクセス権限を確認してください。
システム環境設定 > セキュリティとプライバシー > プライバシー > 写真

#### パッケージエラー
```bash
pip install -r requirements.txt --upgrade
```

---

<a name="english"></a>
## 🇬🇧 English

### 📝 Overview

Mac Photos to Windows is an application that transfers photos from Mac Photos app to Windows while preserving all metadata including location information and timestamps.

### ✨ Features

- 📸 **Metadata Preservation**: Maintains complete EXIF information, timestamps, and GPS location data
- 📁 **Auto-organization**: Automatically sorts photos into Year/Month folders
- 🖼️ **HEIC Support**: Keeps HEIC format intact (compatible with Windows 10/11)
- 🎨 **User-friendly GUI**: Intuitive graphical interface for easy operation
- 📊 **Progress Display**: Real-time processing status updates
- 📝 **Detailed Reports**: Saves migration results in JSON format

### 🚀 Installation

#### Option 1: Use Release Version (Recommended)

1. Download `Mac.Photo.Migrator.app.zip` from [Latest Release](https://github.com/mintiasaikoh/mac-photo-migrator/releases/latest)
2. Extract the downloaded ZIP file
3. Drag `Mac Photo Migrator.app` to Applications folder
4. Launch the app (Right-click → "Open" on first launch)

> **Note**: Due to macOS security features, a warning may appear on first launch.  
> Allow it in System Preferences > Security & Privacy, or right-click → "Open" to launch.

#### Option 2: Run from Source Code

```bash
# Clone repository
git clone https://github.com/mintiasaikoh/mac-photo-migrator.git
cd mac-photo-migrator

# Install required packages
pip install -r requirements.txt

# Launch GUI app
python scripts/migrate_photos_gui.py
```

### 📖 Usage

1. **Launch the app**
2. **Select source** `.photoslibrary` file in "Photo Library"
3. **Select destination** folder in "Output"
4. **Click "Start Migration"**

### 📁 Output Structure

```
Output/
├── 2024/
│   ├── 01_January/
│   ├── 02_February/
│   └── ...
├── RAW/
│   └── 2024/...
└── migration_report.json
```

### ⚙️ System Requirements

- macOS 10.15 Catalina or later
- Python 3.7+ (if running from source)
- Access permission to Photos app library
- Sufficient storage space (approximately 2x your photo library size)

### ⚠️ Important Notes

- Initial library analysis may take time
- Processing large photo collections (10,000+) may take several hours
- Ensure sufficient free space at destination
- Windows requires "HEIF Image Extensions" to view HEIC files
- **Always backup your photo library before using this application**

### 🐛 Troubleshooting

#### Permission Error
Check Photos library access permissions:
System Preferences > Security & Privacy > Privacy > Photos

#### Package Error
```bash
pip install -r requirements.txt --upgrade
```

---

## 📄 License / ライセンス

MIT License

## 🤝 Contributing / 貢献

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

プルリクエストは歓迎します。大きな変更の場合は、まずissueを作成して変更内容について議論してください。

## 📧 Support / サポート

- 🇬🇧 Report issues at [Issues](https://github.com/mintiasaikoh/mac-photo-migrator/issues)
- 🇯🇵 問題や要望は[Issues](https://github.com/mintiasaikoh/mac-photo-migrator/issues)でお知らせください