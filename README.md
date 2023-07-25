# TechLabo-Python-Django

## postgres_webapp (windows版)

### 1. 前提条件
以下がローカルPCにインストールされていること
- Python(version 3以上)
- VSCode 
- Git

### 2. インストール
1. githubに移動しブランチを作成

https://github.com/udonkot/TechLabo-Python-Django

「branches」
「New branch」
New branch name: feature-PostgresWebApp-{名字}
Source: feature-PostgresWebApp-okayasu
「Create new branch」

2. リポジトリ用のフォルダを作成、フォルダに移動（場所、名前は任意）

3. クローンを作成（Git Bash, VScode, コマンドプロンプトなどツールは任意）
```
git clone https://github.com/udonkot/TechLabo-Python-Django.git
```

4. 作成したブランチをチェックアウト
```
git checkout {作成したブランチ名}
```

### ３．アプリ起動

1. Python仮想環境を構築
ターミナル(（VScode, コマンドプロンプト)を開き、以下コマンドを実行
```
cd C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\application
python3 -m venv .venv

C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\application\.venv\Scripts\activate.bat

pip install --upgrade pip
pip install -r requirements.txt
```

別のウィンドウでターミナルを開き、以下コマンドを実行
```
cd C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\database
python3 -m venv .venv

C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\database\.venv\Scripts\activate.bat

pip install --upgrade pip
pip install -r requirements.txt
```

2. Djangoアプリケーションを起動
ターミナル#１で以下コマンドを実行
```
python manage.py runserver 127.0.0.1:8000
```

ターミナル#２で以下コマンドを実行
```
python manage.py runserver 127.0.0.1:8001
```

3. ブラウザからアクセス
[http://127.0.0.1:8000/application/get/data/](http://127.0.0.1:8000/application/get/data/)にアクセスし、画面が表示されれば成功！

### ４. ワーク

---

# TechLabo-Python-Django

## postgres_webapp (docker版)

### 1. 前提条件
コンテナ(Docker)を起動させる環境が構築されていること

以下がローカルPCにインストールされていること
- Git

### 2. インストール
1. githubに移動しブランチを作成

https://github.com/udonkot/TechLabo-Python-Django

「branches」
「New branch」
New branch name: feature-PostgresWebApp-{名字}
Source: feature-PostgresWebApp-okayasu
「Create new branch」

2. リポジトリ用のフォルダを作成、フォルダに移動（場所、名前は任意）

3. クローンを作成（Git Bash, VScode, コマンドプロンプトなどツールは任意）
```
git clone https://github.com/udonkot/TechLabo-Python-Django.git
```

4. 作成したブランチをチェックアウト
```
git checkout {作成したブランチ名}
```

5. チェックアウトした資材をLinux環境へ移動させる

### ５. ワーク
