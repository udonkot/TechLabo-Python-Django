import logging

from django.shortcuts import render

from .modules import request as req


'''
データを取得して返却する
'''
def get_data(request):
    logger = logging.getLogger("app")

    try:
        # データ取得
        data = {
            "data": req.get_data()
        }
        logger.debug(f"data: {data}")

        # 返却
        return render(request, "data.html", data)

    except Exception as ex:
        message = {
            "message": str(ex.args[0])
        }
        logger.error(f"data: {message}")

        return render(request, "error.html", message)


'''
データを登録後に、データを取得して返却する
'''
def register_data(request):
    logger = logging.getLogger("app")

    try:
        # データ登録
        logger.debug(f"request: {request}")
        req.register_data(request.POST.get("data"))

        # データ取得
        data = {
            "data": req.get_data()
        }
        logger.debug(f"data: {data}")

        # 返却
        return render(request, "data.html", data)

    except Exception as ex:
        message = {
            "message": str(ex.args[0])
        }
        logger.error(f"data: {message}")

        return render(request, "error.html", message)
