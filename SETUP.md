# 別のPCでAtCoder環境をセットアップする

この手順はWindowsのPowerShellを前提にしています。GitHubからリポジトリをクローンしただけでは、PC固有の `acc`、Python仮想環境、AtCoderログイン情報は引き継がれないため、使用するPCごとに一度だけセットアップします。

## 1. 必要なソフトをインストールする

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

## 2. GitHubからリポジトリを取得する

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

## 3. 現在地を確認する

```powershell
Get-Location
Test-Path .\setup-atcoder.ps1
```

`Get-Location`がAtCoderリポジトリを示し、`Test-Path`が `True` になれば次へ進みます。

## 4. セットアップスクリプトを実行する

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

## 5. AtCoderへログインする

同じPowerShellで次を実行し、表示に従ってAtCoderのユーザー名とパスワードを入力します。

```powershell
acc login
```

ログインできたことを確認します。

```powershell
acc session
```

`OK`と表示されればログイン済みです。AtCoderのログインCookieはGitHubへ保存されないため、PCごとにこの操作が必要です。

## 6. `acc`の設定を確認する

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

## 7. VS Codeでリポジトリ全体を開く

```powershell
code .
```

VS Codeでは `C:\DEV\AtCoder` のようなAtCoderリポジトリ全体を開いてください。`abcXXX`などのコンテストフォルダだけを開くと、リポジトリに登録されているテスト・提出タスクを利用できません。

これで初期セットアップは完了です。コンテスト開始後の操作は[README.md](./README.md)を参照してください。

## セットアップ中によくあるエラー

### `acc`を実行できない

PowerShellを開き直してから、もう一度 `acc --version` を実行します。スクリプト実行が禁止されているというエラーの場合は、PowerShell用スクリプトではなくWindowsコマンド版を使用できます。

```powershell
acc.cmd --version
acc.cmd login
acc.cmd new abcXXX
```

### `py`または`python`が見つからない

Python 3をインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

### `npm`が見つからない

Node.jsをインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

### セットアップが途中で失敗した

原因を修正したあと、リポジトリ直下で同じスクリプトをもう一度実行できます。`myenv`や設定が途中まで作成されていても、基本的には続きから再設定されます。

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```
