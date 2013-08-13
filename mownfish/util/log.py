import os
import sys
import logging
import logging.handlers

from tornado.options import define, options

LOG = logging.getLogger()

def _setup_logging_from_conf(name):
    if not options.log_path or not name:
        return

    _logger = logging.getLogger()

    if options.log_level == 'none':
        return
    _logger.setLevel(getattr(logging, options.log_level))
    
    formatter = logging.Formatter('%(asctime)s    %(levelname)s    %(module)s.%(funcName)s:%(lineno)d    %(message)s', '')
    _log_file = '%s/%s.Main.log' % (options.log_path, name)
    timelog = logging.handlers.TimedRotatingFileHandler(_log_file,
            'midnight', 1, 0)
    timelog.setFormatter(formatter)
    _logger.addHandler(timelog)

def setup(name):
    _setup_logging_from_conf(name)

