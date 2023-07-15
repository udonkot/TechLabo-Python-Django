from django.shortcuts import render

from .modules import request as req


def data(request):
    res = req.get_data()
    context = {"data": res["sample"]}

    return render(request, 'data.html', context)
