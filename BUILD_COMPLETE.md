# Mac Photo Migratorアプリのビルド完了

ビルドが正常に完了しました！

## ビルドされたアプリケーションの場所

```
/Users/mymac/PhotoMigrationTool/dist/Mac Photo Migrator.app
```

## アプリケーションの使用方法

1. **アプリケーションの起動**
   - Finderで`dist`フォルダを開きます
   - `Mac Photo Migrator.app`をダブルクリックして起動します
   - 初回起動時はセキュリティ警告が表示される場合があります。その場合は：
     - アプリを右クリック → 「開く」を選択
     - 警告ダイアログで「開く」をクリック

2. **写真の移行手順**
   - アプリが起動したら、「写真ライブラリ選択」ボタンをクリック
   - Macの写真ライブラリ（.photoslibrary）を選択
   - 「出力先選択」ボタンをクリックして保存先フォルダを選択
   - 「移行開始」ボタンをクリックして処理を開始

3. **処理の確認**
   - 進行状況バーで処理の進捗を確認
   - ログエリアに詳細な処理内容が表示されます

## 注意事項

- 初回実行時は写真ライブラリへのアクセス許可が必要です
- 大量の写真がある場合、処理に時間がかかります
- 移行先に十分な空き容量があることを確認してください

## トラブルシューティング

もしアプリが起動しない場合は、以下をお試しください：

1. ターミナルで直接実行：
   ```bash
   /Users/mymac/PhotoMigrationTool/dist/Mac\ Photo\ Migrator.app/Contents/MacOS/Mac\ Photo\ Migrator
   ```

2. Pythonスクリプトを直接実行：
   ```bash
   cd /Users/mymac/PhotoMigrationTool/
   python3 scripts/migrate_photos_gui.py
   ```

## 配布について

このアプリを他のMacで使用する場合は、`Mac Photo Migrator.app`をそのままコピーして配布できます。
