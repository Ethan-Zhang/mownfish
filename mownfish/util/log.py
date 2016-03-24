#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Ethan Zhang<http://github.com/Ethan-Zhang>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import os
import sys
import logging
import logging.handlers

from tornado.options import define, options
from mownfish.util.multiprocesslogging \
    import MultiProcessTimedRotatingFileHandler

LOG = logging.getLogger()


def _setup_logging_from_conf(name):
    if not options.log_path or not name:
        return

    if name == 'Main':
        _logger = logging.getLogger()
    else:
        _logger = logging.getLogger(name)

    if options.log_level == 'none':
        return

    if name == 'Access':
        _logger.setLevel(logging.INFO)
    else:
        _logger.setLevel(getattr(logging, options.log_level))

    formatter = logging.Formatter(
        '%(asctime)s\t%(levelname)s\t%(process)d\t\
        %(module)s.%(funcName)s:%(lineno)d\t%(message)s',
        '')
    _log_file = '%s/mownfish.%s.%s.log' % (options.log_path,
                                           name,
                                           options.port)
    if options.multiports:
        timelog = logging.handlers.TimedRotatingFileHandler(_log_file,
                                                            'midnight', 1, 0)
    else:
        timelog = MultiProcessTimedRotatingFileHandler(_log_file, 'midnight',
                                                       1, 0)
    if name == 'Main':
        timelog.setFormatter(formatter)
    _logger.addHandler(timelog)


def setup(name):
    _setup_logging_from_conf(name)
