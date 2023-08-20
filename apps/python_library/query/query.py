import os
import traceback

from apps.python_library.logging.logger import logger

# 返却する結果
result = {
    'result': True,
    'data': None
}


'''
レコードを全件取得する
'''
def select(table):
    try:
        logger.info('Start')
        rdbms = os.environ['rdbms']

        if rdbms == 'sqlite':
            database = os.environ['database_sqlite']
            objects = table.objects.using(database).all()
            logger.debug('objects=%s', objects)
            recodes = list()
            for recode in objects:
                logger.debug(f'recode=%s: ', recode)
                recodes.append(str(recode))
            logger.debug('recodes=%s', recodes)
            result['data'] = recodes
            logger.debug('result=%s', result)
            logger.info('Success')

            logger.info('End')
            return str(result)

        elif rdbms == 'postgres':
            pass

        else:
            raise Exception

    except Exception:
        logger.error('Error')
        logger.error(traceback.format_exc())

        result['result'] = False
        logger.debug('result=%s', result)

        return str(result)


'''
データを登録する
'''
def insert(table, values: dict):
    try:
        logger.info('Start')
        rdbms = os.environ['rdbms']

        if rdbms == 'sqlite':
            logger.debug('table=%s', table)
            logger.debug('values=%s', values)
            sample_table = table(**values)
            logger.debug('sample_table=%s', sample_table)
            database = os.environ['database_sqlite']
            sample_table.save(using=database)
            logger.info('Success')

            logger.info('End')
            return str(result)

        elif rdbms == 'postgres':
            pass

        else:
            raise Exception

    except Exception:
        logger.error('Error')
        logger.error(traceback.format_exc())

        result['result'] = False
        logger.debug('result=%s', result)
        return str(result)
