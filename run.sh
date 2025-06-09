#!/bin/bash
# Mac写真移行ツール 実行メニュー

echo "========================================="
echo "Mac写真ライブラリ → Windows 移行ツール"
echo "========================================="
echo ""
echo "実行したい機能を選択してください："
echo ""
echo "1) GUI版で移行（推奨・使いやすい）"
echo "2) HEIC変換なしで移行（高速）"
echo "3) HEIC→JPEG変換ありで移行"
echo "4) HEICファイルのみ変換"
echo "5) 終了"
echo ""
read -p "選択 (1-5): " choice

case $choice in
    1)
        echo "GUI版を起動します..."
        python scripts/migrate_photos_gui.py
        ;;
    2)
        echo "HEIC変換なし版を起動します..."
        python scripts/migrate_photos_no_heic.py
        ;;
    3)
        echo "HEIC変換あり版を起動します..."
        python scripts/migrate_photos.py
        ;;
    4)
        echo "HEIC変換ツールを起動します..."
        python heic_converters/convert_heic_simple.py
        ;;
    5)
        echo "終了します。"
        exit 0
        ;;
    *)
        echo "無効な選択です。"
        exit 1
        ;;
esac