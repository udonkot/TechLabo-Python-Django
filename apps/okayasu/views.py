import os
import traceback
import inspect

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect

from apps.okayasu import models
from apps.python_library.logging.logger import logger
from apps.python_library.request import request as python_library_requset
from apps.python_library.query import query

RENDER_TEMPLATE = {
   'okayasu_page': 'apps/rooms/okayasu/page.html',
   'data': 'apps/rooms/okayasu/data.html',
   'error': 'apps/rooms/okayasu/error.html',
}
# 上手く動作できていないためコメントアウト
# REDIRECT_URL = {
#    'data_request': ('data/', 'data_request'),
# }

'''
ユーザ用のroomへ
'''
def okayasu_page(request):
    context = {
        'message': "Hello user's Page!"
    }
    logger.debug('context=%s', context)
    return render(request, RENDER_TEMPLATE['okayasu_page'], context)


'''
リクエストのメソッド(GET/POST)に応じてデータの要求を実行
要求結果がサクセスの場合はデータ表示画面へ、エラーの場合はエラー画面へ遷移
'''
def data_request(request):
    try:
        logger.info('Start')
        logger.debug('request=%s', request)

        method = request.method
        url = 'http://{}:{}/{}'
        ip = os.environ['ip']
        port = os.environ['port']
        response = None

        if method == 'GET':
            path = os.environ['path_select_data']
            url = url.format(ip, port, path)
            response = python_library_requset.get(url, params=None)
            if response['result'] is True:
                context = {
                    'data': response['data']
                }
                logger.debug('context=%s', context)
                logger.info('Success')

                logger.info('End')
                return render(request, RENDER_TEMPLATE['data'], context)
            else:
                logger.warning('Falure')

                context = {
                    'message': response['message']
                }
                logger.debug('context=%s', context)
                logger.info('End')
                return render(request, RENDER_TEMPLATE['error'], context)

        elif method == 'POST':
            path = os.environ['path_insert_data']
            url = url.format(ip, port, path)
            data = request.POST.get('data')
            body = {
               'data': data
            }
            response = python_library_requset.post(url, body)
            if response['result'] is True:
                context = {
                    'data': response['data']
                }
                logger.debug('context=%s', context)
                logger.info('Success')

                logger.info('End')
                # 上手く動作できていないためコメントアウト
                #return redirect('okayasu:' + REDIRECT_URL['data_request'])
                current_path = request.path
                return redirect(current_path)
            else:
                context = {
                    'message': response['message']
                }
                logger.debug('context=%s', context)
                logger.warning('Falure')

                logger.info('End')
                return render(request, RENDER_TEMPLATE['error'], context)

        else:
            context = {
                'message': 'Non-provided method is used.'
            }
            logger.info('End')
            return render(request, RENDER_TEMPLATE['error'], context)

    except Exception as ex:
        logger.error('Error')
        logger.error(traceback.format_exc())

        current_function_name = inspect.currentframe().f_code.co_name
        message = f'Exception occared in {current_function_name}. ' \
                    f'Message: {ex.args[0]}'
        context = {
            'message': message
        }
        logger.debug('context=%s', context)
        return render(request, RENDER_TEMPLATE['error'], context)


'''
SapmleTableのレコードを全件取得する
'''
def query_select_data(request):
  try:
    logger.info('Start')
    logger.debug('request=%s', request)

    table = models.SapmleTable
    result = query.select(table)
    logger.info('Success')

    logger.info('End')
    logger.debug('result=%s', result)
    return HttpResponse(result)

  except Exception:
    logger.error('Error')
    logger.error(traceback.format_exc())

    result = {
        'result': False,
        'data': None
    }
    return HttpResponse(result)


'''
SapmleTableにデータを登録する
'''
@csrf_exempt
def query_insert_data(request):
  try:
    logger.info('Start')
    logger.debug('request=%s', request)

    data = request.POST.get('data')
    logger.debug('data=%s', data)

    table = models.SapmleTable
    values = {
        'sample_data': data
    }
    result = query.insert(table, values)
    logger.info('Success')

    logger.info('End')
    logger.debug('result=%s', result)
    return JsonResponse(result, safe=False)

  except Exception:
    logger.error('Error')
    logger.error(traceback.format_exc())

    result = {
        'result': False,
        'data': None
    }
    return HttpResponse(result)
  