# TechLabo-Java-Django

## 1. 前提条件
以下がローカルPCにインストールされていること

- Python 3.10.1
- Git
- IDE
  - VSCode 

## 2. 実行方法
1. コマンドプロンプトを起動
2. リポジトリのクローンを作成

```
git clone https://github.com/udonkot/TechLabo-Python-Django.git
```

3. クローンしたフォルダに移動し、developブランチをチェックアウト
```
cd TechLabo-Python-Django
git checkout develop
```

4. 以下コマンドを実行
```
cd C:{ クローン先のパス }\TechLabo-Python-Django\apps\venv\Scripts\
activate.bat

cd C:{ クローン先のパス }\TechLabo-Python-Django
pip install -r requirements.txt

「.env」ファイルを作成
※ファイルの内容はセキュリティの関係でチャットのメッセージで送ります

python manage.py runserver
```

5. [localhost:8000/apps/home](http://localhost:8000/apps/home)にアクセスし、画面が表示されれば成功！

## 3. 利用方法(初回：featureブランチ作成～作業用フォルダ作成)

1. featureブランチを作成する。GitHub上で操作するとやりやすい

![img.png](img/readme/img01_createbranch.png)

```
ブランチ名は「feature-[ユーザ名]」
```

2. 作成したfeatureブランチをローカルリポジトリにチェックアウトする。
```
cd TechLabo-Java-SpringBoot
git checkout [featureブランチ名]
```

3. ユーザ向けのviewsを新規作成する。<br/>
以下クラスファイルを参考に作成
```
TechLabo-Python-Django\apps
views.pyに自分の名前のメソッドを追加する（sampleメソッドを参考に）
```

4. ユーザ向けのhtmlファイルを新規作成する。<br/>
以下htmlファイルを参考に作成
```
TechLabo-Python-Django\apps\templates\apps\rooms
※ユーザ名のフォルダ、main.htmlを作成する。
※main.htmlの"Template Room Main"を任意の値に修正する
```

5. テンプレートファイルを更新する。<br/>
以下htmlファイルを修正する
```
TechLabo-Python-Django\apps\templates\apps\rooms\sidebar.html
※aタグを追加する。href属性名は"/rooms/[ユーザ名]" 
```

6. 「3．～5．」で作成、更新したファイルをfeatureブランチにコミット／プッシュする<br/>
developブランチで作業していた場合はブランチを切り替えること

7. プルリクエストを作成する。マージ先はdevelopブランチ
