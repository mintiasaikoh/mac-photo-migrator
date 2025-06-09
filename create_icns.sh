#!/bin/bash
# アイコンからICNSファイルを作成

echo "アイコンを生成しています..."

# Pythonでアイコンを作成
python create_icon.py

# iconsetディレクトリを作成
mkdir -p icon.iconset

# 各サイズのアイコンをiconsetディレクトリにコピー
cp icon_16x16.png icon.iconset/icon_16x16.png
cp icon_32x32.png icon.iconset/icon_16x16@2x.png
cp icon_32x32.png icon.iconset/icon_32x32.png
cp icon_64x64.png icon.iconset/icon_32x32@2x.png
cp icon_128x128.png icon.iconset/icon_128x128.png
cp icon_256x256.png icon.iconset/icon_128x128@2x.png
cp icon_256x256.png icon.iconset/icon_256x256.png
cp icon_512x512.png icon.iconset/icon_256x256@2x.png
cp icon_512x512.png icon.iconset/icon_512x512.png

# ICNSファイルを作成
iconutil -c icns icon.iconset

# 一時ファイルを削除
rm -rf icon.iconset
rm icon_*.png

echo "✅ icon.icnsを作成しました"

# setup.pyを更新
sed -i '' "s/'iconfile': None,/'iconfile': 'icon.icns',/" setup.py

echo "✅ setup.pyを更新しました"