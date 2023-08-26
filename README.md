# TechLabo-Python-Django

## Python学習用アプリ

### 1. 事前準備
以下がローカルPCにインストールされていること
- Python (version 3以上) [URL](https://www.python.org/downloads/)
- VSCode (Extentions：Pylance, Git Graphをインストールしておく) [URL](https://code.visualstudio.com/download)
- Git [URL](https://git-scm.com/downloads)

事前に読んでおくと良い記事・動画
- Djangoとは [URL](https://itc.tokyo/django/what-is-django/)
- Gitの操作について [URL](https://www.youtube.com/watch?v=LDOR5HfI_sQ)

---

### 2. インストール

#### 1. リモートリポジトリを作成

githubを別タグで開く
```
https://github.com/udonkot/TechLabo-Python-Django
```

以下の操作を行う

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

---

### 3．Python,Djangoのバージョン確認

#### 1. Python仮想環境を起動

VScodeを起動、「terminal」を開き以下コマンドを実行（端末のOSがWindows以外の場合はパス区切り文字を適宜変更）
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

---

### 4. Djangoの設定

#### 1. ユーザごとのアプリケーションを追加
VScodeを起動、「terminal」を開く（端末のOSがWindows以外の場合はパス区切り文字を適宜変更）

アプリケーション配置用フォルダに移動
```
cd {クローン先のディレクトリ}\TechLabo-Python-Django\apps\
```

ユーザごとのアプリケーションを作成
```
django-admin startapp {ユーザ名}　（ユーザ名は名字のアルファベット）
```

ファイルを開く
```
TechLabo-Python-Django\facescore\settings.py
```

「INSTALLED_APPS」を検索、Listにアプリを追加 （アプリ名：app.{ユーザ名}）

#### 2. ルーティングの設定

ファイルを開く
```
TechLabo-Python-Django\apps\urls.py
```

「urlpatterns」を検索、ListにURLを追加
```
path('{ユーザ名}/', include('apps.{ユーザ名}.urls'))
```

ファイルを作成
```
・TechLabo-Python-Django\apps\{ユーザ名}\urls.py
・TechLabo-Python-Django\apps\{ユーザ名}\views.py
```

作成したファイルに、以下のファイルの内容をコピー
```
・TechLabo-Python-Django\apps\sample\urls.py
・TechLabo-Python-Django\apps\sample\views.py
```

#### 3. 画面の設定

フォルダを作成
```
TechLabo-Python-Django\apps\templates\apps\rooms\{ユーザ名}\
```

作成したフォルダに、以下のファイルをコピー
```
TechLabo-Python-Django\apps\templates\apps\rooms\sample\
・error.html
・sample_data.html
・user_page.html
```

コピーした3ファイルを開き、URLを修正
```
"http://127.0.0.1:8000/apps/sample/data/"
  ↓
"http://127.0.0.1:8000/apps/{ユーザ名}/data/"
```

ファイルを開き、リンクを追加
```
TechLabo-Python-Django\apps\templates\apps\sidebar.html
```
```
<a href="/apps/{ユーザ名}" class="dropdown-item">{ユーザ名}</a>
```

#### 4. 設定ファイル（Django用の設定）

ファイルを作成
```
TechLabo-Python-Django\.env
```

key情報と起動させるアプリを指定
```
KEY = "{※}"
KEY2 = "{※}"
ENDPOINT = "{※}"
LAUNCH_APP = "{ユーザ名}"

※セキュリティ情報のため、設定する値はSlackで連携します
```

#### 5. データベース(sqlite)の設定

ファイルを開く
```
TechLabo-Python-Django\apps\{ユーザ名}\models.py
```

以下のファイルの内容をコピー
```
TechLabo-Python-Django\apps\{ユーザ名}\models.py
```

以下のフォルダに移動
```
cd {クローン先のディレクトリ}\TechLabo-Python-Django\
```

データベースをセットアップ
```
python manage.py makemigrations {アプリ名}
```

ファイルを開く
```
TechLabo-Python-Django\facescore\settings.py
```

「DATABASES」を検索、データベースを追加
```
'{ユーザ名}_sqlite': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'apps/' '{ユーザ名}/' 'db.sqlite3',
}
```

データベースの設定を適用
```
python manage.py migrate {アプリ名} --database={ユーザ名}_sqlite
```

#### 6. データベース初期値の設定

以下のファイルを右クリック > Open Database
```
TechLabo-Python-Django\facescore\db.sqlite3
```

画面左下のタブ「SQLITE EXPLORER」を展開

{ユーザ名}_sampletable > 右クリック > Show Table

{ユーザ名}_sampletable > 右クリック > New Query [Select]

-- SQLiteファイルにSQLをコピー
```
INSERT INTO {ユーザ名}_sampletable (sample_data) VALUES ('data-1');
SELECT id, {ユーザ名}_sampletable FROM sample_table;

※デリート時に使用
DELETE FROM {ユーザ名}_sampletable WHERE id = '1';
DELETE FROM {ユーザ名}_sampletable;
```

INSERT分を選択 > 右クリック > Run Selected Query

SELECT分を選択 > 右クリック > Run Selected Query

レコードが追加されていることを確認

---

### 6. アプリケーションの起動

#### 1. 設定ファイル

ファイルを作成
```
TechLabo-Python-Django\apps\{ユーザ名}\config\config.ini
```

作成したファイルに、以下の内容をコピー 
```
'''データベース設定'''
[database_setting]

# 使用するRDBMS
rdbms=sqlite
;rdbms=postgres

# sqliteの設定
database_sqlite={ユーザ名}_sqlite

'''インタフェース設定'''
[interface_setting]
ip=localhost
port=8000
path_data=apps/{ユーザ名}/data/
path_select_data=apps/{ユーザ名}/select/data/
path_insert_data=apps/{ユーザ名}/insert/data/
```

#### 2. ログ出力ディレクトリ

ディレクトリを作成（ログファイルは起動時に自動で作成される）
```
TechLabo-Python-Django\apps\{ユーザ名}\logs\
```

#### 3. 不要な記述をコメントアウト

以下のファイルの中身を全てコメントアウトする
```
TechLabo-Python-Django\apps\okayasu\apps.py
```

#### 4. 起動 

以下のディレクトリに移動
```
cd {クローン先のディレクトリ}\TechLabo-Python-Django\
```

アプリケーション起動
```
python manage.py runserver 8000
```

#### 5. 画面操作

ブラウザで以下のURLにアクセス
```
http://127.0.0.1:8000/apps/home
```

以下の画面が表示されること

![image](https://github.com/udonkot/TechLabo-Python-Django/assets/40541121/65cee504-b0b7-4958-87ff-b9814eddd225)

左メニュー「Rooms」 > {ユーザ名}

以下の画面が表示されること

![image](https://github.com/udonkot/TechLabo-Python-Django/assets/40541121/eae4d7cf-c460-4446-acd2-44d62baf2fda)

SAMPLE DATA PAGE > 「SAMPLE DATA PAGE」に遷移

以下の画面が表示されること

![image](https://github.com/udonkot/TechLabo-Python-Django/assets/40541121/1c0df2af-c13b-422d-9803-15f63d2e16a8)

---

#### アプリ側でエラーが発生した場合

エラー内容は以下のログファイルを確認
```
TechLabo-Python-Django\apps\okayasu\logs\
・app.log（アプリケーションのログ）
・django.log（Django関連のログ）
```

---

### 6. リモートリポジトリへプッシュ

作成したブランチへプッシュ
```
feature-webapp-{ユーザ名}
```
