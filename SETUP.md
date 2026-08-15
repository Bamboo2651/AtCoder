# 別のPCでAtCoder環境を使えるようにする手順

この手順は、Windowsの別PCにこのリポジトリをcloneし、`acc new abcXXX`、サンプルテスト、提出準備を使える状態にするまでを説明します。上から順番に実行してください。

## 最初に知っておくこと

GitHubから共有されるものと、PCごとに作り直すものは異なります。

| GitHubから取得するもの | PCごとに作るもの |
| --- | --- |
| 解答コード | `myenv`（Python仮想環境） |
| VS Codeのタスク | グローバルの`acc` |
| セットアップスクリプト | `acc`の設定 |
| Pythonテンプレート | AtCoderのログインCookie |

`myenv`には作成したPCのPythonへの絶対パスが記録されます。そのため、ほかのPCからコピーした`myenv`は使用できません。GitHubからも共有せず、各PCで`setup-atcoder.ps1`を使って作成します。

AtCoderのログインCookieも秘密情報なので、GitHub、チャット、スクリーンショットでは共有しません。

## 1. 必要なソフトを確認する

別PCに次のソフトをインストールしておきます。

- Git
- Node.js（`npm`を含む）
- Python 3
- Visual Studio Code

PowerShellを開き、次を1行ずつ実行します。

```powershell
git --version
node --version
npm --version
py --version
code --version
```

すべてバージョンが表示されれば次へ進みます。

`py`だけが見つからず、次のコマンドでPython 3のバージョンが表示される場合は問題ありません。

```powershell
python --version
```

コマンドが見つからない場合は対応するソフトをインストールし、PowerShellを閉じて開き直してから再確認します。

## 2. リポジトリをcloneする

以下は `C:\DEV\AtCoder` に配置する例です。

```powershell
New-Item -ItemType Directory -Path C:\DEV -Force
Set-Location C:\DEV
git clone https://github.com/Bamboo2651/AtCoder.git
Set-Location .\AtCoder
```

すでにclone済みの場合は、cloneし直さず最新版を取得します。

```powershell
Set-Location C:\DEV\AtCoder
git pull --ff-only
```

## 3. cloneしたリポジトリにいることを確認する

```powershell
Get-Location
Test-Path .\setup-atcoder.ps1
Test-Path .\set-acc-session.ps1
```

確認する内容は次のとおりです。

- `Get-Location`がcloneしたAtCoderリポジトリを示している
- 2つの`Test-Path`が両方とも `True` になる

`False`になる場合は、AtCoderリポジトリへ移動してからやり直します。

```powershell
Set-Location C:\DEV\AtCoder
```

## 4. このPC用の環境を作る

AtCoderリポジトリ直下で次を実行します。

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```

このスクリプトが行う処理は次のとおりです。

1. `atcoder-cli` v2.2.0をグローバルインストールする
2. リポジトリ内に、このPC用の`myenv`を作成する
3. `online-judge-tools` v11.5.1をインストールする
4. AtCoderの`MiB`表記に対応する互換修正を適用する
5. `acc`が`myenv\Scripts\oj.exe`を使うように設定する
6. 全問題、`test`フォルダ、空の`main.py`を作るPythonテンプレートを登録する

インストールには数分かかる場合があります。途中に`npm warn deprecated`と表示されても、最後まで処理が続いていれば待ちます。

最後に次が表示されれば、このPC用の環境作成は成功です。

```text
[AtCoder] Local setup completed.
```

`myenv`を手動で有効化する必要はありません。VS Codeのタスクが`myenv`内のPythonと`oj`を直接使用します。

## 5. ブラウザでAtCoderへログインする

ChromeまたはEdgeで[AtCoderのログインページ](https://atcoder.jp/login)を開き、普段どおりログインします。ログイン後、AtCoderのホーム画面が表示されることを確認します。

`acc login`は使用しません。AtCoderのCloudflare確認によって、自動ログインが`login failed`になる場合があるためです。

## 6. ブラウザのログインCookieをコピーする

AtCoderへログインしたブラウザで次の操作を行います。

1. `F12`を押して開発者ツールを開く
2. 開発者ツール上部の「Application」を開く
3. 左側の「Storage」→「Cookies」→`https://atcoder.jp`を開く
4. Cookie一覧から`REVEL_SESSION`を選ぶ
5. `Value`列の値だけをコピーする

「Application」が見つからない場合は、開発者ツール上部の`>>`を押します。

`REVEL_SESSION`は、ログイン中のAtCoderアカウントを操作できる秘密情報です。ほかの場所へ貼り付けたり、ファイルとしてリポジトリ内へ保存したりしないでください。

## 7. Cookieを`acc`へ登録する

AtCoderリポジトリ直下のPowerShellで次を実行します。

```powershell
powershell -ExecutionPolicy Bypass -File .\set-acc-session.ps1
```

次の入力待ちになったら、手順6でコピーした`REVEL_SESSION`のValueを貼り付けてEnterを押します。

```text
REVEL_SESSION value:
```

貼り付けた文字は画面には表示されません。最後に次のように表示されれば登録成功です。

```text
check login status...
OK
[AtCoder] The login cookie was registered for acc.
```

CookieはそのPCの`atcoder-cli`設定フォルダにだけ保存されます。別PCでも同じ手順を個別に実行します。Cookieの期限が切れた場合も、手順5からやり直します。

## 8. セットアップ結果を確認する

次を1行ずつ実行します。

```powershell
acc --version
acc session
acc check-oj
acc config
acc templates
```

次の内容が確認できればセットアップ完了です。

```text
acc --version
  2.2.0

acc session
  OK

acc check-oj
  online-judge-tools is available

acc config
  default-task-choice: all
  default-test-dirname-format: test
  default-template: python

acc templates
  python / main.py
```

`oj-path`には、cloneしたリポジトリ内の`myenv\Scripts\oj.exe`が表示されます。たとえば`C:\DEV\AtCoder`へcloneした場合は次のパスです。

```text
C:\DEV\AtCoder\myenv\Scripts\oj.exe
```

## 9. VS Codeでリポジトリ全体を開く

```powershell
code .
```

VS CodeではAtCoderリポジトリ全体を開きます。`abcXXX`などのコンテストフォルダだけを別ウィンドウで開くと、リポジトリに登録されているテスト・提出タスクを利用できません。

これで別PCの初期セットアップは完了です。コンテスト開始後の操作は[README.md](./README.md)を参照してください。

## 2回目以降に別PCで作業を始めるとき

初回セットアップを毎回行う必要はありません。作業開始前に、ほかのPCの変更を取り込みます。

```powershell
Set-Location C:\DEV\AtCoder
git pull --ff-only
code .
```

その後、実際のコンテストIDを指定して`acc new`を実行します。

```powershell
acc new abcXXX
```

## トラブルが起きた場合

### `python.exe`が別のユーザーフォルダを参照している

次のように、存在しない別PCのパスが表示される場合があります。

```text
did not find executable at 'C:\Users\別のユーザー\...\python.exe'
```

これは、別PCで作成した`myenv`が残っている状態です。削除せずリポジトリの外へ退避し、このPC用に作り直します。

```powershell
Set-Location C:\DEV\AtCoder
Move-Item .\myenv ..\myenv-other-pc-backup
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```

セットアップ成功後も、退避したフォルダは自動削除されません。不要であることを確認できるまではそのまま残します。

### `acc login`が`login failed`になる

`acc login`は繰り返さず、手順5から手順7のブラウザCookie登録を行います。

### `acc`を実行できない

PowerShellを閉じて開き直し、もう一度確認します。

```powershell
acc --version
```

PowerShellスクリプトの実行が禁止されているというエラーの場合は、Windowsコマンド版を使用できます。

```powershell
acc.cmd --version
acc.cmd session
acc.cmd new abcXXX
```

### `py`または`python`が見つからない

このPCへPython 3をインストールし、PowerShellを閉じて開き直してから手順4を再実行します。

### `npm`が見つからない

このPCへNode.jsをインストールし、PowerShellを閉じて開き直してから手順4を再実行します。

### セットアップが途中で失敗した

エラーの原因を修正したあと、AtCoderリポジトリ直下でセットアップスクリプトを再実行します。

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```
