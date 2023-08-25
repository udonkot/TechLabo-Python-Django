# TechLabo-Python-Django

## Python学習用アプリ

### 1. 前提条件
以下がローカルPCにインストールされていること
- Python(version 3以上) [URL](https://www.python.org/downloads/)
- VSCode [URL](https://code.visualstudio.com/download)
- Git [URL](https://git-scm.com/downloads)

### 2. インストール

#### 1. リモートリポジトリを作成

githubを別タグで開く
```
https://github.com/udonkot/TechLabo-Python-Django
```

プルダウン「master」 > View all branches > New branch

branch name 「feature-webapp-{ユーザ名}」 > source 「feature-webapp-sample」 > Create new branch

#### 2. ローカルリポジトリ用のフォルダを作成

ローカルにフォルダを作成（場所、名前は任意）

#### 3. リモートリポジトリをクローン

Git操作用のツールを起動（Git Bash, VScode, コマンドプロンプトなどツールは任意）

2.で作成したフォルダに移動

URLを指定してクローン
```
https://github.com/udonkot/TechLabo-Python-Django.git
```

#### 4. チェックアウト

1.で作成したブランチにチェックアウト
```
feature-webapp-{ユーザ名}
```

### 3．Python,Djangoのバージョン確認

#### 1. Python仮想環境を起動

VScodeを起動

「terminal」を開き、以下コマンドを実行（端末のOSがWindows以外の場合はパス区切り文字を適宜変更）
```
{2.で作成したフォルダ}\TechLabo-Python-Django\apps\venv\Scripts\activate.bat
```

【※補足】Python仮想環境を停止させる場合
```
{2.で作成したフォルダ}\TechLabo-Python-Django\apps\venv\Scripts\deactivate.bat
```

#### 2. バージョン確認

- Python
```
python -V
Python 3.10.1 (バージョン3であればOK)
```
- Django
```
python -m django --version
4.1.2 (バージョン4であればOK)
```
