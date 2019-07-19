import logging
logging.basicConfig(format='%(asctime)s  %(levelname)s :%(message)s',
 datefmt='%m/%d/%Y %I:%M:%S %p'
,
level=logging.DEBUG)

logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')


logging.warning('is when this event was logged.')
