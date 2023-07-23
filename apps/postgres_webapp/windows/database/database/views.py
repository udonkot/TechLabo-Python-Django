from django.http import HttpResponse
from .modules import query


def data(request):
    result = query.select_data()

    return HttpResponse(result)
