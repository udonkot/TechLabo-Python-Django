from django.http import HttpResponse
from .modules import query


def data(request):
    result = query.select_data()

    return HttpResponse(result)

def insertData(request):
    # 登録
    query.insert_data(request)
    # 再検索
    result = query.select_data()

    return HttpResponse(result)

