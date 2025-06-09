#!/bin/bash
# macOSアプリのビルドスクリプト

echo "Mac Photo Migratorアプリをビルドしています..."

# 必要なパッケージをインストール
echo "必要なパッケージをインストールしています..."
pip3 install -r requirements.txt

# py2appがインストールされているか確認
if ! pip3 show py2app > /dev/null 2>&1; then
    echo "py2appをインストールしています..."
    pip3 install py2app
fi

# 古いビルドファイルを削除
rm -rf build dist

# アプリをビルド
python3 setup.py py2app

# ビルドが成功したか確認
if [ -d "dist/Mac Photo Migrator.app" ]; then
    echo "✅ ビルド成功！"
    echo "アプリの場所: dist/Mac Photo Migrator.app"
    echo ""
    echo "アプリを開くには:"
    echo "open dist/Mac\ Photo\ Migrator.app"
else
    echo "❌ ビルド失敗"
    exit 1
fi