# 別のPCでの初回セットアップ

Windowsの新しいPCで、上から順番に1回だけ行います。

## 1. 必要なソフトを入れる

- Git
- Node.js
- Python 3
- Visual Studio Code

## 2. リポジトリをcloneする

PowerShellで実行します。

```powershell
New-Item -ItemType Directory -Path C:\DEV -Force
Set-Location C:\DEV
git clone https://github.com/Bamboo2651/AtCoder.git
Set-Location .\AtCoder
```

## 3. セットアップする

```powershell
powershell -ExecutionPolicy Bypass -File .\setup-atcoder.ps1
```

`[AtCoder] Local setup completed.` と表示されれば成功です。
仮想環境を手動で有効化する必要はありません。

## 4. accとojにAtCoderのログイン情報を登録する

`acc new`は、フォルダ作成に`acc`、サンプルケースの取得に`oj`（online-judge-tools）を使います。
特にコンテスト開催中は、両方がAtCoderにログインしていないと、フォルダだけ作成されてサンプルケースを取得できないことがあります。

1. ブラウザで[AtCoder](https://atcoder.jp/login)へログインする
2. `F12`を押す
3. 「Application」→「Cookies」→`https://atcoder.jp`を開く
4. `REVEL_SESSION`の`Value`をコピーする
5. PowerShellで次を実行する

```powershell
powershell -ExecutionPolicy Bypass -File .\set-acc-session.ps1
```

入力待ちになったら、コピーした値を貼り付けてEnterを押します。入力した文字は画面に表示されません。
このスクリプトは、同じログイン情報を`acc`と`oj`の両方に登録します。`oj login`を別途実行する必要はありません。

> `REVEL_SESSION`はパスワードと同じ秘密情報です。GitHubや他人には共有しないでください。

## 5. 動作確認する

```powershell
acc session
acc check-oj
.\myenv\Scripts\oj.exe login --check --use-browser never https://atcoder.jp/
code .
```

- `acc session`が`OK`
- `acc check-oj`が`online-judge-tools is available`
- `oj`の確認が`You have already signed in.`

以上の3つが確認できれば完了です。

セットアップ後の使い方は[README.md](./README.md)を参照してください。

## うまくいかない場合

- `acc login`は使わず、手順4のCookie登録を行う
- `acc`はログイン済みなのに開催中の問題でテストケースが作成されない場合は、手順4をもう一度行い、`oj`のログイン確認も実行する
- `git`、`npm`、`py`が見つからない場合は、対応するソフトを入れてPowerShellを開き直す
- セットアップに失敗した場合は、原因を直して手順3をもう一度実行する
