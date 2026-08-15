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

`myenv`はGitHubでは共有せず、各PCで同じ名前の仮想環境を個別に作成します。Python仮想環境には作成元PCの絶対パスが含まれるため、中身をPC間で共有することはできません。別PC由来で起動できない`myenv`が見つかった場合、スクリプトはそれを`myenv-broken-日時`へ退避してから、このPC用の`myenv`を作成します。

## 5. ブラウザのログインCookieを`acc`へ登録する

AtCoderのログイン画面にはCloudflareの確認が導入されているため、`acc login`によるユーザー名・パスワードの自動ログインは通らないことがあります。通常のブラウザでログインし、そのブラウザに保存された `REVEL_SESSION` を専用スクリプトで`acc`へ登録します。

### 5-1. ブラウザでAtCoderへログインする

ChromeまたはEdgeで[AtCoderのログインページ](https://atcoder.jp/login)を開き、普段どおりログインします。ログイン後にAtCoderのホーム画面が表示されることを確認してください。

### 5-2. `REVEL_SESSION`をコピーする

1. AtCoderを開いたタブで `F12` を押す
2. 開発者ツール上部の「Application」を開く
3. 左側の「Storage」→「Cookies」→`https://atcoder.jp`を開く
4. Cookie一覧から `REVEL_SESSION` を選ぶ
5. `Value`列の値だけをコピーする

「Application」が見つからない場合は、開発者ツール上部の `>>` を押すと表示されます。

`REVEL_SESSION`はログイン中のアカウントを操作できる秘密情報です。チャット、GitHub、スクリーンショットへ載せないでください。

### 5-3. 専用スクリプトへ貼り付ける

AtCoderリポジトリ直下のPowerShellで次を実行します。

```powershell
powershell -ExecutionPolicy Bypass -File .\set-acc-session.ps1
```

`REVEL_SESSION value:` と表示されたら、先ほどコピーした値を貼り付けてEnterを押します。入力内容は画面には表示されません。このスクリプトは、そのPCの`atcoder-cli`設定フォルダにある `session.json` のログインCookieを置き換えます。

最後に次のように表示されれば登録成功です。

```text
check login status...
OK
[AtCoder] The login cookie was registered for acc.
```

念のため、もう一度確認できます。

```powershell
acc session
```

`OK`と表示されればログイン済みです。CookieはGitHubへ保存されないため、PCごとにこの操作が必要です。また、Cookieの期限が切れた場合も同じ手順で新しい値を登録します。

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
acc.cmd session
acc.cmd new abcXXX
```

### `acc login`が`login failed`になる

パスワードを繰り返し入力せず、「5. ブラウザのログインCookieを`acc`へ登録する」の手順を実行してください。AtCoder側のCloudflare確認により、`acc login`の自動ログインが失敗する場合があります。

### `py`または`python`が見つからない

Python 3をインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

### `npm`が見つからない

Node.jsをインストールし、PowerShellを開き直してからセットアップスクリプトを再実行します。

### セットアップが途中で失敗した

原因を修正したあと、リポジトリ直下で同じスクリプトをもう一度実行できます。`myenv`や設定が途中まで作成されていても、基本的には続きから再設定されます。

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```
