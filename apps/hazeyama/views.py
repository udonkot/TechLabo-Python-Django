import os
import traceback
import inspect
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect

from . import models
from apps.python_library.logging.logger import logger
from apps.python_library.request import request as python_library_requset
from apps.python_library.query import query

APP = os.environ.get('APP')
RENDER_TEMPLATE = {
   'user_page': f'apps/rooms/{APP}/user_page.html',
   'sample_data': f'apps/rooms/{APP}/sample_data.html',
   'error': f'apps/rooms/{APP}/error.html',
}
# 上手く動作できていないためコメントアウト
# REDIRECT_URL = {
#    'data_request': ('data/', 'data_request'),
# }


'''
ユーザ用のroomへ
'''
def user_page(request):
    context = {
        'message': "Hello user's Page!"
    }
    logger.debug('context=%s', context)
    return render(request, RENDER_TEMPLATE['user_page'], context)


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
                return render(request, RENDER_TEMPLATE['sample_data'], context)
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
                #return redirect('user_page:' + REDIRECT_URL['data_request'])

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

# def file_request(request):
#     path = os.environ['path_insert_file']
#     url = 'http://{}:{}/{}'
#     ip = os.environ['ip']
#     port = os.environ['port']
#     url = url.format(ip, port, path)
#     data = request.POST.get('data')
#     body = {
#         'data': data
#     }
#     response = python_library_requset.post(url, body)
#     if response['result'] is True:
#         context = {
#             'data': response['data']
#         }
#         logger.debug('context=%s', context)
#         logger.info('Success')

#         logger.info('End')

#         # 上手く動作できていないためコメントアウト
#         #return redirect('user_page:' + REDIRECT_URL['data_request'])

#         current_path = request.path
#         return redirect(current_path)

def upload_file(request):
    logger.info('upload_file')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        logger.debug('form=%s', request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            file_content = uploaded_file.read().decode('utf-8')
            logger.debug('file_content=%s', file_content)
            list_content = file_content.split(",")
            logger.debug('list_content=%s', list_content)
            for content in list_content:
                table = models.UploadedFile
                values = {
                    'user': content
                }
                result = query.insert(table, values)
                logger.debug('result=%s', result)
            return render(request, RENDER_TEMPLATE['sample_data'])
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

'''
SapmleTableのレコードを全件取得する
'''
def query_select_data(request):
  try:
    logger.info('Start')
    logger.debug('request=%s', request)

    table = models.HazeyamaTable
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

    table = models.HazeyamaTable
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
  
