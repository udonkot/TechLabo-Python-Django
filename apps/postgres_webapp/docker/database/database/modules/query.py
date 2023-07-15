import os
import psycopg2
import configparser
import traceback

from psycopg2.extras import DictCursor

from .. import settings


'''
「data」テーブルからレコードを全件取得
'''
def select_data():
    result = {
        "result": True,
        "data": None
    }
    try:
        connection = _get_connection()
        with connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                sql = "SELECT * FROM data"
                cursor.execute(sql)
                rows = cursor.fetchall()
            connection.commit()
        print("【database log】data=" + str(rows))
        result["data"] = [
            rows[row][0] for row in range(len(rows))]
        print("【database log】result=" + str(result))
        return str(result)
    except Exception:
        print("【database log】Exception occored.")
        print(traceback.format_exc())
        result["result"] = False
        return result


'''
「postgres」データベースの接続を取得
'''
def _get_connection():
    config = configparser.ConfigParser()
    file_path = os.path.join(settings.BASE_DIR, 'database', 'config', 'config.ini')
    config.read(file_path, "UTF-8")
    connection = psycopg2.connect(
        host=config['database_settings']['host'],
        user=config['database_settings']["user"],
        password=config["database_settings"]["password"],
        database=config["database_settings"]["database"])
    return connection
