# AtCoder環境の使い方

初期セットアップがまだの場合は、先に[SETUP.md](./SETUP.md)を上から順番に実行してください。このREADMEはセットアップ完了後の使い方を説明します。

## 作業を始める前に

別PCでの変更を取り込んでから、AtCoderリポジトリ全体をVS Codeで開きます。

```powershell
Set-Location C:\DEV\AtCoder
git pull
code .
```

## コンテストが始まったら

VS CodeでクローンしたAtCoderリポジトリを開いたまま、ターミナルで次のコマンドを実行します。`abcXXX` は参加するコンテストID（例: `abc471`）に置き換えてください。

```powershell
cd <AtCoderリポジトリのパス>
acc new abcXXX
```

`acc new` はPCにグローバルインストールされた `acc` を使うため、実行前に仮想環境を有効化する必要はありません。ただし、`Ctrl+Shift+B` のサンプルテストでは `myenv\Scripts\oj.exe`、提出準備では `myenv\Scripts\python.exe` を使うため、`myenv` フォルダ自体は必要です。

現在の設定では全問題が自動的に作成されます。作成された `abcXXX\a\main.py` などを開いてコードを書き、`Ctrl+Shift+B` でサンプルテストと提出準備を実行します。

AtCoderリポジトリ全体を開いたVS Codeウィンドウをそのまま使ってください。作成された `abcXXX` フォルダだけを別のVS Codeウィンドウで開くと、このリポジトリのテスト・提出タスクを利用できません。

VS Codeから、問題フォルダへの移動や仮想環境の有効化をせずにサンプルテストと提出準備を実行できます。

## サンプルテスト

1. テストしたい問題の `main.py` をVS Codeで開く
2. `Ctrl+Shift+B` を押す
3. ターミナルに表示される結果を確認する
4. 全サンプルがACすると、提出方法を質問される
5. コンテスト開催中の本番提出なら`o`、終了後の練習提出なら`p`を入力する

何も入力せずEnter、またはそれ以外を入力した場合は中止されます。テストに失敗した場合も提出されません。

AtCoderは開催時刻によって本番提出か練習提出かを自動決定します。`o`と`p`の選択が実際の開催状況と一致しない場合は、誤操作を防ぐため提出画面を開きません。

現在のAtCoder提出フォームは古い`online-judge-tools`からの自動送信を拒否するため、コードをクリップボードへコピーし、対象問題を選択したブラウザ提出画面を開きます。ブラウザでコードを貼り付け、CPythonを選択して提出ボタンを押してください。

開いているファイルと同じフォルダの `test` が自動的に使われます。

```text
abc466/
├─ contest.acc.json
└─ a/
   ├─ main.py       ← このファイルを開く
   └─ test/         ← この中のサンプルでテスト
```

## 提出だけを実行

1. 提出したい問題の `main.py` を開く
2. `Ctrl+Shift+P` を押す
3. `タスク: タスクの実行`（`Tasks: Run Task`）を選ぶ
4. `AtCoder: 提出`を選ぶ
5. `o`または`p`を選ぶ
6. 開いたブラウザでコードを貼り付け、CPythonを選択して提出する

提出先は、親フォルダにある `contest.acc.json` から自動的に判定されます。

## ログインエラーが出た場合

`acc session`が `not login`になる場合は、ブラウザでAtCoderへログインし直してからCookieを再登録します。詳しい取得手順は[SETUP.mdの「ブラウザのログインCookieをaccへ登録する」](./SETUP.md#5-ブラウザのログインcookieをaccへ登録する)を参照してください。

VS Codeから登録する場合は、次の順番で実行します。

1. `Ctrl+Shift+P`を押す
2. `タスク: タスクの実行`を選ぶ
3. `AtCoder: ログインCookieを設定`を選ぶ
4. ブラウザからコピーした `REVEL_SESSION` のValueを貼り付ける
5. `acc`を使う処理をもう一度実行する

ブラウザ提出では、開いたブラウザ側でもAtCoderへログインしてください。

## 仮想環境について

仮想環境を手動で有効化する必要はありません。

VS Codeのタスクが、次の実行ファイルを直接呼び出します。

```text
myenv\Scripts\oj.exe
myenv\Scripts\python.exe
```

そのため、`Activate.ps1`の実行は不要ですが、現在の設定では`myenv`フォルダ自体は必要です。

## 内部の仕組み

- `.vscode/tasks.json`: VS Codeにテスト・提出・ログインCookie設定のタスクを登録
- `set-acc-session.ps1`: ブラウザの `REVEL_SESSION` を画面へ表示せずに`acc`へ登録
- `.vscode/atcoder-test.ps1`: `oj test`を実行し、成功した場合だけ提出するか確認
- `.vscode/atcoder-submit.ps1`: 開催状況と提出先を確認し、コードをコピーしてブラウザ提出画面を開く
- `.vscode/atcoder-contest-phase.py`: AtCoderの開催時刻から本番提出か練習提出かを判定
- `.vscode/patch-onlinejudge-mib.ps1`: 新ジャッジの`MiB`表記に古い`online-judge-tools`を対応させる

## よくあるエラー

### `Test directory not found`

`test`フォルダがある問題の`main.py`を開いてから、もう一度`Ctrl+Shift+B`を押します。

### `contest.acc.json not found`

`acc new`で作成したコンテストフォルダ内の`main.py`を開いてください。古い形式の`460/a.py`のようなファイルは、現在の提出タスクでは提出先を自動判定できません。

### `online-judge-tools not found`

リポジトリ内の `myenv\Scripts\oj.exe` が存在するか確認します。存在しない場合は、リポジトリ直下で `powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1` を実行します。

### `assert parsed_memory_limit` / `AssertionError`

ABC466以降の新ジャッジでメモリ制限が`MiB`表記になったことによるエラーです。提出タスクが互換修正を自動適用します。
