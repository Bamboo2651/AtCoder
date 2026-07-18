# AtCoder環境の仕組みとトラブル対応

このファイルは、`C:\DEV\AtCoder`の構成やVS Codeタスクの動作を説明するための資料です。普段使うコマンドだけ確認したい場合は[README](../README.md)を参照してください。

## 使用しているツール

- `atcoder-cli`（`acc`）: コンテストフォルダ作成、問題追加、ログイン管理
- `online-judge-tools`（`oj`）: サンプルテストの実行
- Python仮想環境（`myenv`）: `oj`とテスト実行用Pythonを保持
- VS Code Tasks: 開いている`main.py`を基準にテストと提出準備を実行

## コンテスト生成の仕組み

現在の`atcoder-cli`設定は次のとおりです。

```text
default-contest-dirname-format: {ContestID}
default-task-dirname-format: {tasklabel}
default-test-dirname-format: test
default-task-choice: all
default-template: python
```

そのため、次のコマンドだけで全問題のPythonファイルとサンプルが生成されます。

```powershell
acc new abc467
```

`contest.acc.json`にはコンテストID、問題ID、問題フォルダ、提出対象ファイルが記録されます。VS Codeの提出準備タスクもこの情報から対象問題を判定します。

## `Ctrl+Shift+B`の動作

1. VS Codeで現在開いているPythonファイルを取得
2. 同じフォルダにある`test`を確認
3. `myenv\Scripts\oj.exe`でサンプルテストを実行
4. テストに失敗した場合は終了
5. 全件ACの場合は`o`、`p`、キャンセルを質問
6. 選択したモードとコンテストの開催時刻を照合
7. コードをクリップボードへコピー
8. 対象問題を選択したブラウザ提出画面を開く

処理は主に次のファイルにあります。

- `.vscode/tasks.json`
- `.vscode/atcoder-test.ps1`
- `.vscode/atcoder-submit.ps1`
- `.vscode/atcoder-contest-phase.py`

## 本番提出と練習提出

AtCoderには、本番提出と練習提出を切り替えるPOSTパラメータはありません。同じ提出画面から送信し、AtCoderがコンテスト開催時刻を基準に扱いを決めます。

- `o`: 開催中のみ許可。本番提出として順位に影響する
- `p`: 終了後のみ許可。練習提出となり順位には影響しない

開始前や、開催状況と選択が一致しない場合は提出画面を開きません。

## ブラウザで最後の提出を行う理由

現在のAtCoder提出フォームでは、問題ごとの言語選択欄がJavaScriptで動的に設定されます。古い`online-judge-tools 11.5.1`による自動POSTはAtCoder側から`Error`として拒否されるため、VS Codeタスクは次の安全なところまで自動化します。

1. 提出対象問題を判定
2. 本番／練習の開催時刻を検証
3. コードをクリップボードへコピー
4. 対象問題を選択済みの提出画面を開く

ブラウザではコードを貼り付け、`Python (CPython ...)`を選択して提出ボタンを押します。

## 仮想環境を有効化しなくてよい理由

VS Codeタスクは次のファイルを絶対パスで直接実行します。

```text
C:\DEV\AtCoder\myenv\Scripts\oj.exe
C:\DEV\AtCoder\myenv\Scripts\python.exe
```

そのため、普段は`Activate.ps1`を実行する必要がありません。ただし現在の設定では、`myenv`フォルダ自体は必要です。

## `MiB`互換修正

新しいAtCoder問題では、メモリ制限が`MB`ではなく`MiB`で表示されます。古い`online-judge-tools`はこの表記を解析できないため、`.vscode/patch-onlinejudge-mib.ps1`が次を認識できるよう互換修正します。

```text
KB / KiB / MB / MiB
```

仮想環境を作り直して修正が消えた場合も、提出準備スクリプトの起動時に再適用されます。

## トラブル対応

### `Test directory not found`

開いているPythonファイルと同じフォルダに`test`がありません。`acc new`で生成された問題フォルダの`main.py`を開いてください。

### `contest.acc.json not found`

提出対象を判定できません。次の形式になっているか確認してください。

```text
abc467/
├─ contest.acc.json
└─ a/
   └─ main.py
```

古い`460/a.py`のような構成は、現在の提出準備タスクでは自動判定できません。

### `Official submission is available only during the contest`

終了済みコンテストで`o`を選択しています。練習提出する場合は`p`を選択してください。

### `Practice submission is available only after the contest`

開催前または開催中に`p`を選択しています。開催中の本番提出なら`o`を選択してください。

### `AssertionError` / `parsed_memory_limit`

`online-judge-tools`が`MiB`を解析できていません。次を実行して互換修正を再適用します。

```powershell
cd C:\DEV\AtCoder
.\.vscode\patch-onlinejudge-mib.ps1
```

### ログインできない

`acc`の状態を確認します。

```powershell
acc session
acc login
```

ブラウザ提出の場合は、開いたブラウザ側でもAtCoderにログインしてください。
