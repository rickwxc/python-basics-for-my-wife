import logging

FORMAT = '%(asctime)-15s  %(ip)-16s %(user)-5s %(message)s'
FORMAT = ('%(levelname)-8s %(asctime)s %(name)s %(funcName)s '
              ' %(lineno)-3d: %(message)s')
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


d = {'ip': '127.0.0.1', 'user': 'rick'}
logger = logging.getLogger('tcpserver')
logger.debug('debug : %s', 'connection reset', extra=d)
logger.info('info : %s', 'connection reset', extra=d)
logger.warning('warning: %s', 'connection reset', extra=d)
d = {'ip': '255.255.255.100', 'user': 'rick'}
logger.debug('debug : %s', 'connection reset', extra=d)
logger.info('info : %s', 'connection reset', extra=d)
logger.warning('warning: %s', 'connection reset', extra=d)

"""
CRITICAL 50
ERROR 40
WARNING 30
INFO 20
DEBUG 10
NOTSET 0
"""
