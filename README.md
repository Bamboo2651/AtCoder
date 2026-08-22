# AtCoder環境の使い方

初回セットアップがまだの場合は、先に[SETUP.md](./SETUP.md)を実行してください。

## 使い方

PowerShellで最新の変更を取り込み、AtCoderリポジトリ全体をVS Codeで開きます。

```powershell
Set-Location C:\DEV\AtCoder
git pull
code .
```

コンテストが始まったら、VS Codeのターミナルで次を実行します。
`abcXXX`は参加するコンテストID（例：`abc471`）に置き換えてください。

```powershell
acc new abcXXX
```

1. 作成された`abcXXX\a\main.py`などを開いてコードを書く
2. `Ctrl+Shift+B`を押してサンプルテストを実行する
3. 全サンプルに通ったら、本番提出は`o`、練習提出は`p`を入力する
4. 開いたブラウザにコードを貼り付け、CPythonを選択して提出する

> VS Codeではコンテストフォルダだけでなく、AtCoderリポジトリ全体を開いてください。

## ログイン切れの場合

`acc session`が`not login`になった場合や、開催中の問題でテストケースを取得できない場合は、[SETUP.md](./SETUP.md)の「accとojにAtCoderのログイン情報を登録する」をもう一度行ってください。
