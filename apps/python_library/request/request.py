import os
import traceback
import requests
import ast

from apps.python_library.logging.logger import logger

IP_DATABASE = os.environ.get('ip_database')
PORT_DATABASE = os.environ.get('port_database')
PATH_DATABASE_DATA = os.environ.get('path_database_data')
PATH_DATABASE_REG_DATA = os.environ.get('path_database_reg_data')


'''
HTTP通信のGETリクエストを実行
結果を返却
'''
def get(url: str, params: dict):
    response_success = {
        'result': True,
        'message': 'GET request success.',
        'data': {},
    }
    response_falure = {
        'result': False,
        'message': 'GET request falure.',
        'data': None,
    }

    try:
        logger.info('Start')

        logger.debug('url=%s', url)
        logger.debug('params=%s', params)
        response = requests.get(url, params=params)
        logger.debug('response=%s', response)
        status_code = response.status_code
        logger.debug('status_code=%s', status_code)
        result = ast.literal_eval(response.text)
        logger.debug('result=%s', result)

        if status_code != 200:
            raise Exception('HTTP request error.')
        else:
            pass

        if result['result'] is True:
            logger.info('Success')
            response_success['data'] = result['data']
            logger.debug('response_success=%s', response_success)
            logger.info('End')
            return response_success

        else:
            logger.warning('Falure')
            logger.debug('response_falure=%s', response_falure)
            logger.info('End')
            return response_falure

    except Exception:
        logger.error('Error')
        logger.error(traceback.format_exc())

        logger.debug('response_falure=%s', response_falure)
        return response_falure


'''
HTTP通信のPOSTリクエストを実行
結果を返却
'''
def post(url: str, data: dict):
    response_success = {
        'result': True,
        'message': 'Post request success.',
        'data': {},
    }
    response_falure = {
        'result': False,
        'message': 'Post request falure.',
        'data': None,
    }

    try:
        logger.info('Start')

        logger.debug('url=%s', url)
        logger.debug('data=%s', data)
        response = requests.post(url, data=data)
        logger.debug('response=%s', response)
        status_code = response.status_code
        logger.debug('status_code=%s', status_code)
        result = ast.literal_eval(response.json())
        logger.debug('result=%s', result)

        if status_code != 200:
            raise Exception('HTTP request error.')
        else:
            pass

        if result['result'] is True:
            logger.info('Success')
            response_success['data'] = result['data']

            logger.debug('response_success=%s', response_success)
            logger.info('End')
            return response_success

        else:
            logger.warning('Falure')

            logger.debug('response_falure=%s', response_falure)
            logger.info('End')
            return response_falure

    except Exception:
        logger.info('Error')
        logger.error(traceback.format_exc())

        logger.debug('response_falure=%s', response_falure)
        return response_falure
