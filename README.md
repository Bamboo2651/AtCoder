# AtCoder Command Cheat Sheet

AtCoder作業用コマンドをすぐ確認するためのREADMEです。環境の仕組みやエラー対応は[環境解説](docs/atcoder-environment.md)を参照してください。

## コンテストを始める

AtCoderリポジトリへ移動します。

```powershell
cd C:\DEV\AtCoder
```

ログイン状態を確認します。

```powershell
acc session
```

コンテストフォルダを作成します。`abc467`の部分を参加するコンテストIDに変更してください。

```powershell
acc new abc467
```

現在の設定では、全問題の`main.py`とサンプルケースが自動生成されます。

```text
abc467/
├─ contest.acc.json
├─ a/
│  ├─ main.py
│  └─ test/
├─ b/
│  ├─ main.py
│  └─ test/
└─ ...
```

VS Codeでリポジトリを開きます。

```powershell
code C:\DEV\AtCoder
```

## テストと提出準備

テストしたい問題の`main.py`を開き、次のキーを押します。

```text
Ctrl+Shift+B
```

全サンプルがACすると提出モードを質問されます。

```text
o  コンテスト開催中の本番提出
p  コンテスト終了後の練習提出
Enter  キャンセル
```

正しいモードを選ぶと、コードがクリップボードへコピーされ、対象問題を選択したAtCoder提出画面が開きます。ブラウザでコードを貼り付け、CPythonを選択して提出します。

提出準備だけを実行する場合は、VS Codeで次を選びます。

```text
Ctrl+Shift+P
→ Tasks: Run Task
→ AtCoder: 提出
```

## atcoder-cli

### コンテスト作成

```powershell
acc new abc467
```

問題を選びながら作成する場合：

```powershell
acc new abc467 --choice inquire
```

サンプルをダウンロードせず作成する場合：

```powershell
acc new abc467 --no-tests
```

Pythonテンプレートを明示する場合：

```powershell
acc new abc467 --template python
```

### 既存コンテストへ問題を追加

```powershell
cd C:\DEV\AtCoder\abc467
acc add
```

未作成の問題をすべて追加する場合：

```powershell
acc add --choice rest
```

次の1問だけ追加する場合：

```powershell
acc add --choice next
```

### ログイン

```powershell
acc login
acc session
acc logout
```

### 設定確認

```powershell
acc config
acc templates
acc check-oj
acc config-dir
```

現在の主要設定：

```text
default-template: python
default-task-choice: all
default-test-dirname-format: test
oj-path: C:\DEV\AtCoder\myenv\Scripts\oj.exe
```

### コンテスト・問題URLを表示

```powershell
acc url abc467
acc url abc467 abc467_a
```

## online-judge-tools

通常は`Ctrl+Shift+B`を使うため、以下の手動コマンドは不要です。動作確認やトラブル調査時に使用します。

```powershell
cd C:\DEV\AtCoder\abc467\a
C:\DEV\AtCoder\myenv\Scripts\oj.exe test -c "C:\DEV\AtCoder\myenv\Scripts\python.exe main.py"
```

バージョン確認：

```powershell
C:\DEV\AtCoder\myenv\Scripts\oj.exe --version
C:\DEV\AtCoder\myenv\Scripts\python.exe --version
acc --version
```

## 仮想環境

手動で有効化せず、VS Codeタスクから直接利用します。調査などで有効化したい場合だけ次を実行します。

```powershell
cd C:\DEV\AtCoder
.\myenv\Scripts\Activate.ps1
```

終了：

```powershell
deactivate
```

## Git

変更確認：

```powershell
git status
git diff
```

コミットとプッシュ：

```powershell
git add <ファイル>
git commit -m "変更内容"
git push
```

最新状態を取得：

```powershell
git pull --ff-only
```

## 詳細

- [AtCoder環境の仕組みとトラブル対応](docs/atcoder-environment.md)
- [VS Codeタスク](.vscode/tasks.json)
- [テストスクリプト](.vscode/atcoder-test.ps1)
- [提出準備スクリプト](.vscode/atcoder-submit.ps1)
