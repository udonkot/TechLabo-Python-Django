import os
import logging
import traceback
import requests
import ast

IP_DATABASE = os.environ.get("ip_database")
PORT_DATABASE = os.environ.get("port_database")
PATH_DATABASE_DATA = os.environ.get("path_database_data")
PATH_DATABASE_REG_DATA = os.environ.get("path_database_reg_data")


'''
HTTP通信のGETリクエストで「database」からデータを取得
'''
def get_data():
    logger = logging.getLogger("app")

    try:
        logger.info("Start get data.")

        database_url = f"http://{IP_DATABASE}:{PORT_DATABASE}/{PATH_DATABASE_DATA}"
        params = ""
        logger.debug(f"url: {database_url}")
        logger.debug(f"params: {params}")

        response = requests.get(database_url, params)
        logger.debug(f"status_code: {response.status_code}")
        if response.status_code != 200:
            raise Exception
        else:
            pass

        result = ast.literal_eval(response.text)
        logger.debug(f"result: {result}")
        if result["result"] is False:
            raise Exception
        else:
            pass

        logger.info("End get data.")

        return result["data"]

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())

        raise Exception("Failed gat data.")


'''
HTTP通信のPOSTリクエストで「database」にデータを登録
'''
def register_data(data):
    logger = logging.getLogger("app")

    try:
        logger.info("Start register data.")

        database_url = f"http://{IP_DATABASE}:{PORT_DATABASE}/{PATH_DATABASE_REG_DATA}"
        params = {
            "data": data
        }
        logger.debug(f"url: {database_url}")
        logger.debug(f"params: {params}")

        response = requests.post(database_url, data=params)
        logger.debug(f"status_code: {response.status_code}")
        if response.status_code != 200:
            raise Exception
        else:
            pass

        result = response.json()
        logger.debug(f"result: {result}")
        if result["result"] is False:
            raise Exception
        else:
            pass

        logger.info("End register data.")

        return result["data"]

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())

        raise Exception("Failed register data.")
