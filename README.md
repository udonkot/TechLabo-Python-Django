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

2. 設定ファイルを作成
以下ファイルを作成
C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\application\application\config\config.ini

ファイルの中身 ※パスを各自の環境に合わせて変更する
```
;ログの設定
[log_setting]
log_file_app=C:\\{作成したリポジトリ}\\TechLabo-Python-Django\\apps\\postgres_webapp\\windows\\application\\application\\logs\\app.log
log_file_django=C:\\{作成したリポジトリ}\\TechLabo-Python-Django\\apps\\postgres_webapp\\windows\\application\\application\\logs\\django.log

;インタフェース設定
[if_setting]
ip_database=127.0.0.1
port_database=8001
path_database_data=database/get/data/
path_database_reg_data=database/register/data/
```

以下ファイルを作成
C:\{作成したリポジトリ}\TechLabo-Python-Django\apps\postgres_webapp\windows\database\database\config\config.ini

ファイルの中身 ※パスを各自の環境に合わせて変更する 
```
;ログの設定
[log_setting]
log_file_app=C:\\{作成したリポジトリ}\\TechLabo-Python-Django\\apps\\postgres_webapp\\windows\\database\\database\\logs\\app.log
log_file_django=C:\\{作成したリポジトリ}\\TechLabo-Python-Django\\apps\\postgres_webapp\\windows\\database\\database\\logs\\django.log
```

3. Djangoアプリケーションを起動
ターミナル#１で以下コマンドを実行
```
python manage.py runserver 127.0.0.1:8000
```

ターミナル#２で以下コマンドを実行
```
python manage.py runserver 127.0.0.1:8001
```

4. ブラウザからアクセス
[http://127.0.0.1:8000/application/get/data/](http://127.0.0.1:8000/application/get/data/)にアクセスし、画面が表示されれば成功！

![画面イメージ](screen_image.PNG)

### ４. ワーク
1. Djangoの概要の説明を受ける

2. DBへデータ登録するの機能を実装する

- 修正対象のソースは以下
TechLabo-Python-Django\apps\postgres_webapp\windows\database\database\query.py
⇒メソッド：「insert_data」に登録処理を実装
※『models.py　データ登録　手順』で検索

TechLabo-Python-Django\apps\postgres_webapp\windows\database\database\urls.py
⇒URL"database/register/data/"を追加する

3. DBにカラムを追加し、追加した情報を画面のテーブルに表示させる機能を実装する

説明を作成中...

---

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

### ３. ワーク
1. コンテナの起動テスト 

- ディレクトリ移動
cd /home/shinji/TechLabo-Python-Django/apps/postgres_webapp/docker/application
- Dockerfileからイメージを作成する（コンテナ名とタグは自由）
- コンテナを起動する
- コンテナを停止する
- コンテナを削除する
- イメージを削除する

2. コンテナの構成について説明を受ける

口頭で説明

3. コンテナ間通信を実装

作成中
