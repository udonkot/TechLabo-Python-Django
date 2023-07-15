def select_data():
    # DBのコネクション取得
    connection = _get_connection()

    # Select実行
    result = [
        {"data": "sample data"},
        ]
    print("result=" + str(result))
    return result


def _get_connection():
    #TODO データベース接続を実装
    connection = "connection"
    return connection
