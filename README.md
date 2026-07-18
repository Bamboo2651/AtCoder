# AtCoder環境の使い方

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

1. `Ctrl+Shift+P`を押す
2. `タスク: タスクの実行`を選ぶ
3. `AtCoder: ログインし直す`を選ぶ
4. `acc`を使う処理をもう一度実行する

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

- `.vscode/tasks.json`: VS Codeにテスト・提出・ログインのタスクを登録
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

`C:\DEV\AtCoder\myenv\Scripts\oj.exe`が存在するか確認します。

### `assert parsed_memory_limit` / `AssertionError`

ABC466以降の新ジャッジでメモリ制限が`MiB`表記になったことによるエラーです。提出タスクが互換修正を自動適用します。
