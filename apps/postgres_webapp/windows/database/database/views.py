import logging
import traceback

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

from .modules import query


# ロガーの設定
logger = logging.getLogger("app")


def select_data(request):
    result = query.select_data()

    return HttpResponse(result)


@csrf_exempt
def insert_data(request):
    try:
        result = query.insert_data(request.POST.get("data"))

        return JsonResponse(result, safe=False)

    except Exception:
        logger.error("Exception occored.")
        logger.error(traceback.format_exc())
