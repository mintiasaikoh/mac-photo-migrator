# Release Notes / リリースノート

<div align="center">
  <h1>Mac Photos to Windows - Release Notes</h1>
  <p>
    <strong>🇯🇵 <a href="#japanese">日本語</a></strong> | <strong>🇬🇧 <a href="#english">English</a></strong>
  </p>
</div>

---

<a name="japanese"></a>
## 🇯🇵 日本語版リリースノート

### v1.0.0 - 初回リリース 🎉
*リリース日: 2025年6月9日*

#### 🚀 リリース内容

**Mac Photos to Windows v1.0.0** をリリースしました！

このアプリケーションは、Macの写真.appライブラリからWindowsへ、位置情報や撮影日時などの重要なメタデータを保持したまま写真を移行するためのツールです。

#### ✨ 主な機能

- **📸 メタデータ完全保持**
  - EXIF情報（カメラ設定、レンズ情報など）
  - 撮影日時（元の日時を正確に保持）
  - GPS位置情報（ジオタグ）
  
- **📁 スマート整理機能**
  - 年/月フォルダで自動分類
  - RAWファイルは別フォルダに整理
  - 重複ファイルの自動検出
  
- **🖼️ 最新フォーマット対応**
  - HEIC形式をそのまま保存
  - Windows 10/11での表示に対応
  - RAWファイル（DNG、CR2、NEF等）サポート
  
- **🎨 直感的なインターフェース**
  - わかりやすいGUI
  - ドラッグ&ドロップ対応
  - 日本語メニュー
  
- **📊 詳細な処理情報**
  - リアルタイム進捗表示
  - 処理済み/エラー件数の表示
  - 移行結果の詳細レポート（JSON形式）

#### 📥 ダウンロード方法

1. [Releases](https://github.com/mintiasaikoh/mac-photo-migrator/releases)ページにアクセス
2. `Mac.Photo.Migrator.v1.0.0.zip` (23.2MB) をダウンロード
3. ZIPファイルを解凍
4. `Mac Photo Migrator.app`をApplicationsフォルダに移動
5. アプリを起動

#### 💻 システム要件

- **OS**: macOS 10.15 Catalina以降
- **メモリ**: 4GB以上推奨
- **ストレージ**: 写真ライブラリの約2倍の空き容量
- **権限**: 写真.appへのアクセス許可

#### ⚠️ 既知の問題と回避方法

1. **初回起動時のセキュリティ警告**
   - 右クリック→「開く」で起動
   - またはシステム環境設定でアプリを許可

2. **大量写真の処理時間**
   - 10,000枚以上: 数時間かかる場合があります
   - 処理中はMacをスリープさせないでください

3. **メモリ使用量**
   - 大きなライブラリでは一時的にメモリを多く使用します
   - 他のアプリを終了してから実行を推奨

#### 🔧 トラブルシューティング

問題が発生した場合は、以下を確認してください：

1. 写真.appのライブラリへのアクセス権限
2. 出力先の空き容量
3. `/logs`フォルダ内のエラーログ

#### 📝 次回アップデート予定

- クラウドストレージ連携機能
- バッチ処理の最適化
- 選択的移行機能

---

<a name="english"></a>
## 🇬🇧 English Release Notes

### v1.0.0 - Initial Release 🎉
*Release Date: June 9, 2025*

#### 🚀 About This Release

**Mac Photos to Windows v1.0.0** is now available!

This application transfers photos from Mac Photos app to Windows while preserving all important metadata including location information and timestamps.

#### ✨ Key Features

- **📸 Complete Metadata Preservation**
  - EXIF information (camera settings, lens info, etc.)
  - Original timestamps (accurately preserved)
  - GPS location data (geotags)
  
- **📁 Smart Organization**
  - Auto-sort by Year/Month folders
  - Separate RAW file organization
  - Automatic duplicate detection
  
- **🖼️ Modern Format Support**
  - Preserves HEIC format
  - Compatible with Windows 10/11
  - RAW file support (DNG, CR2, NEF, etc.)
  
- **🎨 Intuitive Interface**
  - User-friendly GUI
  - Drag & drop support
  - Localized menus
  
- **📊 Detailed Processing Info**
  - Real-time progress display
  - Processed/error count display
  - Detailed migration report (JSON format)

#### 📥 How to Download

1. Visit the [Releases](https://github.com/mintiasaikoh/mac-photo-migrator/releases) page
2. Download `Mac.Photo.Migrator.v1.0.0.zip` (23.2MB)
3. Extract the ZIP file
4. Move `Mac Photo Migrator.app` to Applications folder
5. Launch the app

#### 💻 System Requirements

- **OS**: macOS 10.15 Catalina or later
- **Memory**: 4GB+ recommended
- **Storage**: Approximately 2x your photo library size
- **Permissions**: Photos app access permission

#### ⚠️ Known Issues and Workarounds

1. **Security Warning on First Launch**
   - Right-click → "Open" to launch
   - Or allow the app in System Preferences

2. **Processing Time for Large Libraries**
   - 10,000+ photos: May take several hours
   - Keep Mac awake during processing

3. **Memory Usage**
   - Large libraries temporarily use significant memory
   - Recommended to close other apps during migration

#### 🔧 Troubleshooting

If you encounter issues, please check:

1. Photos app library access permissions
2. Available space at destination
3. Error logs in `/logs` folder

#### 📝 Planned Updates

- Cloud storage integration
- Batch processing optimization
- Selective migration feature

---

## 📊 Version History / バージョン履歴

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | 2025-06-09 | 🇯🇵 初回リリース<br>🇬🇧 Initial release |

---

## 🐛 Feedback / フィードバック

### 🇯🇵 日本語
問題の報告や機能要望は[Issues](https://github.com/mintiasaikoh/mac-photo-migrator/issues)でお知らせください。

### 🇬🇧 English
Please report bugs and feature requests at [Issues](https://github.com/mintiasaikoh/mac-photo-migrator/issues).

---

## ⚠️ Important Notice / 重要なお知らせ

### 🇯🇵 日本語
**使用前に必ず写真ライブラリのバックアップを取ってください。**  
このアプリケーションは読み取り専用で動作しますが、万が一に備えてバックアップを推奨します。

### 🇬🇧 English
**Always backup your photo library before using this application.**  
While this app operates in read-only mode, we recommend backing up as a precaution.

---

<div align="center">
  <p>
    <strong>Thank you for using Mac Photos to Windows!</strong><br>
    <strong>Mac Photos to Windowsをご利用いただきありがとうございます！</strong>
  </p>
</div>