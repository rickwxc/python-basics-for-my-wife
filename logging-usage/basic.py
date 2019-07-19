import logging
logging.warning('Watch out!')  # will print a message to the console
logging.warning('%s before you %s', 'Look', 'leap!')
logging.info('I told you so')


"""
The INFO message doesn’t appear because the default level is WARNING.
The printed message includes the indication of the level and the description of the event provided in the logging call, i.e. ‘Watch out!’.
"""
