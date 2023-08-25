import logging
import traceback

from .. import models

# ロガーの設定
logger = logging.getLogger("app")

# 返却する結果
result = {
    "result": True,
    "data": None
}

'''
レコードを取得する
'''
def select_data():
    try:
        logger.info("Start select data.")

        sample_table = models.SapmleTable.objects.all()
        logger.debug(f"sample_table: {sample_table}")

        recodes = list()
        for recode in sample_table:
            logger.debug(f"recode: {recode}")
            recodes.append(str(recode))

        result["data"] = recodes
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
レコードを追加する
'''
def insert_data(data):
    try:
        logger.info("Start insert data.")

        # TODO レコードを追加する処理を実装

        sample_table = models.SapmleTable.objects.all()
        sample_table.create(id=100, sample_data='hoge-100')
        logger.info("End insert data.")

        return result

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())

        result["result"] = False
        logger.debug(f"result: {result}")


'''
レコードを変更する
'''
def update_data():
    try:
        logger.info("Start update data.")

        # TODO レコードを更新する処理を実装

        logger.info("End update data.")

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())


'''
レコードを削除する
'''
def delete_data():
    try:

        logger.info("Start delete data.")

        # TODO レコードを削除する処理を実装

        logger.info("End delete data.")

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())
