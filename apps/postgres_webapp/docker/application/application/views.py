import logging

from django.shortcuts import render

from .modules import request as req


def data(request):
    logger = logging.getLogger("app")

    try:
        data = {
            "data": req.get_data()
        }
        logger.debug(f"data: {data}")

        return render(request, "data.html", data)

    except Exception as ex:
        message = {
            "message": str(ex.args[0])
        }
        logger.error(f"data: {message}")

        return render(request, "error.html", message)
