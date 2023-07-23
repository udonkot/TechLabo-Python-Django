import logging
import os
import psycopg2
import traceback

from psycopg2.extras import DictCursor


'''
「data」テーブルからレコードを全件取得
'''
def select_data():
    logger = logging.getLogger("app")

    sql = "SELECT * FROM data;"

    result = {
        "result": True,
        "data": None
    }

    try:
        logger.info("Start select data.")

        connection = _get_connection()
        with connection:
            with connection.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                logger.debug(f"rows: {rows}")
            connection.commit()

        result["data"] = [
            rows[row][0] for row in range(len(rows))
        ]
        logger.debug(f"result: {result}")

        logger.info("End select data.")
 
        return str(result)

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())

        result["result"] = False
        logger.debug(f"result: {result}")

        return str(result)


'''
「postgres」データベースの接続を取得
'''
def _get_connection():
    connection = psycopg2.connect(
        host=os.environ.get("host"),
        user=os.environ.get("user"),
        password=os.environ.get("password"),
        database=os.environ.get("database"),
    )

    return connection
