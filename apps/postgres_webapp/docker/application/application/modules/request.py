import requests
import ast
import traceback

DATABASE_URL = "http://127.0.0.1:8001/database/data/"


'''
HTTP通信のGETリクエストで「database」からデータを取得
'''
def get_data():
    try:
        response = requests.get(DATABASE_URL, params="")
        print("【application log】response=" + str(response.status_code))
        if response.status_code != 200:
            raise Exception
        else:
            pass
        result = ast.literal_eval(response.text)
        print("【application log】result=" + str(result["result"]))
        if result["result"] is False:
            raise Exception
        else:
            pass
        return result["data"]
    except Exception:
        print("【application log】Exception occored.")
        print(traceback.format_exc())
        raise Exception("Failed gat data.")
