# AtCoder環境の使い方

## 別のPCで最初に行うセットアップ

この手順はWindowsのPowerShellを前提にしています。GitHubからリポジトリをクローンしただけでは、PC固有の `acc`、Python仮想環境、AtCoderログイン情報は引き継がれないため、使用するPCごとに一度だけセットアップします。

### 1. 必要なソフトをインストールする

先に次のソフトをインストールします。

- Git
- Node.js（`npm`を含む）
- Python 3
- Visual Studio Code

インストール後はPowerShellをいったん閉じて開き直し、次のコマンドを1行ずつ実行します。

```powershell
git --version
node --version
npm --version
py --version
```

すべてのコマンドでバージョンが表示されれば準備完了です。`py`だけが見つからず、`python --version`でPython 3のバージョンが表示される場合は、そのまま次へ進めます。

### 2. GitHubからリポジトリを取得する

以下は `C:\DEV\AtCoder` に配置する例です。

```powershell
New-Item -ItemType Directory -Path C:\DEV -Force
Set-Location C:\DEV
git clone https://github.com/takehiro-2006/AtCoder.git
Set-Location .\AtCoder
```

すでに別PCへクローン済みの場合は、クローンし直さず最新版を取得します。

```powershell
Set-Location C:\DEV\AtCoder
git pull
```

### 3. 現在地を確認する

```powershell
Get-Location
Test-Path .\setup-atcoder.ps1
```

`Get-Location`がAtCoderリポジトリを示し、`Test-Path`が `True` になれば次へ進みます。

### 4. セットアップスクリプトを実行する

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```

このスクリプトは次の処理を順番に実行します。

1. `atcoder-cli` v2.2.0をグローバルインストールする
2. リポジトリ内にPython仮想環境 `myenv` を作成する
3. `online-judge-tools` v11.5.1を `myenv` にインストールする
4. 新ジャッジの `MiB` 表記に対応する互換修正を適用する
5. `acc`がリポジトリ内の `myenv\Scripts\oj.exe` を使うように設定する
6. 全問題、`test`フォルダ、空の`main.py`を作成するPythonテンプレートを登録する

最後に `[AtCoder] Local setup completed.` と表示されれば完了です。仮想環境を手動で有効化する必要はありません。

### 5. AtCoderへログインする

同じPowerShellで次を実行し、表示に従ってAtCoderのユーザー名とパスワードを入力します。

```powershell
acc login
```

ログインできたことを確認します。

```powershell
acc session
```

`OK`と表示されればログイン済みです。AtCoderのログインCookieはGitHubへ保存されないため、PCごとにこの操作が必要です。

### 6. `acc`の設定を確認する

```powershell
acc --version
acc check-oj
acc config
acc templates
```

次の内容が確認できれば、`acc new`を使用できます。

```text
acc: 2.2.0
online-judge-tools: available
default-task-choice: all
default-test-dirname-format: test
default-template: python
template: python / main.py
```

`oj-path`には、そのPCでクローンしたAtCoderリポジトリ内の `myenv\Scripts\oj.exe` が表示されます。

### 7. VS Codeでリポジトリ全体を開く

```powershell
code .
```

VS Codeでは `C:\DEV\AtCoder` のようなAtCoderリポジトリ全体を開いてください。`abcXXX`などのコンテストフォルダだけを開くと、リポジトリに登録されているテスト・提出タスクを利用できません。

### 8. コンテスト開始時に問題を作成する

VS CodeのターミナルがAtCoderリポジトリ直下にあることを確認し、実際のコンテストIDを指定します。

```powershell
acc new abcXXX
```

たとえばコンテストURLが `https://atcoder.jp/contests/abc123` なら、実行するコマンドは `acc new abc123` です。全問題のフォルダ、空の `main.py`、サンプルケースを格納した `test`フォルダが自動作成されます。

### 9. 別PCで作業を再開するとき

2回目以降はセットアップスクリプトを毎回実行する必要はありません。作業開始前にリポジトリを最新にします。

```powershell
Set-Location C:\DEV\AtCoder
git pull
code .
```

その後、必要なコンテストで `acc new abcXXX` を実行します。

### セットアップ中によくあるエラー

#### `acc`を実行できない

PowerShellを開き直してから、もう一度 `acc --version` を実行します。スクリプト実行が禁止されているというエラーの場合は、PowerShell用スクリプトではなくWindowsコマンド版を使用できます。

```powershell
acc.cmd --version
acc.cmd login
acc.cmd new abcXXX
```

#### `py`または`python`が見つからない

Python 3をインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

#### `npm`が見つからない

Node.jsをインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

#### セットアップが途中で失敗した

原因を修正したあと、リポジトリ直下で同じスクリプトをもう一度実行できます。`myenv`や設定が途中まで作成されていても、基本的には続きから再設定されます。

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
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

リポジトリ内の `myenv\Scripts\oj.exe` が存在するか確認します。存在しない場合は、リポジトリ直下で `powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1` を実行します。

### `assert parsed_memory_limit` / `AssertionError`

ABC466以降の新ジャッジでメモリ制限が`MiB`表記になったことによるエラーです。提出タスクが互換修正を自動適用します。
