from django.shortcuts import render

from .modules import request as req


def data(request):
    try:
        data = {
            "data": req.get_data()
        }
        return render(request, "data.html", data)
    except Exception as ex:
        message = {
            "message": str(ex.args[0])
        }
        print("【application log】message=" + str(message))
        return render(request, "error.html", message)
