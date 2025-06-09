# Mac Photo Migrator - クイックスタートガイド

## 🎯 すぐに使いたい方へ

### 最も簡単な方法（コマンドライン不要）

1. このフォルダ内の `run.sh` をダブルクリック
2. メニューから「1」を選択してGUI版を起動
3. 写真ライブラリと出力先を選択して「移行開始」

### macOSアプリとしてビルド

```bash
# アイコンを作成
./create_icns.sh

# アプリをビルド
./build_app.sh

# アプリを起動
open dist/Mac\ Photo\ Migrator.app
```

## 📱 GitHubリポジトリ

https://github.com/mintiasaikoh/mac-photo-migrator

## 🔧 開発者向け

```bash
# 依存関係のインストール
pip install -r requirements.txt

# 直接実行
python scripts/migrate_photos_gui.py
```

## 📝 ライセンス

MIT License - 自由に使用・改変できます