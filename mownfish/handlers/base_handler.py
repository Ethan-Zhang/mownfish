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

'''BaseRequestHandler
'''

import os
import logging

from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado.options import define, options

from mownfish.util.log import LOG
from mownfish.error import ParameterEmptyError
from mownfish.error import ParameterTypeError
from mownfish.util import commonutils


class BaseHandler(RequestHandler):

    def __init__(self, *args, **kwargv):
        super(BaseHandler, self).__init__(*args, **kwargv)
        self._logger = logging.getLogger('Access')
        self._log_item = []
        self._default_log_item = {}

    def set_default_headers(self):
        self.set_header('Server', options.server_name)

    def prepare(self):
        self._default_log_item['start_time'] = commonutils.format_timestamp(
            self.request._start_time)
        self._default_log_item['version'] = 'V1'
        self._default_log_item['ip'] = self.request.remote_ip
        self._default_log_item['url'] = self.request.uri
        self._default_log_item['status'] = 'FAILED'
        self._default_log_item['request_time'] = 0

    def on_connection_close(self):
        LOG.info('connection close.')

    def on_finish(self):
        self.set_accesslog_item('request_time', self.request.request_time())

    def add_accesslog_item(self, item='', style='s'):
        self._log_item.append((item, style))

    def set_accesslog_item(self, item_name, item):
        if item_name in self._default_log_item:
            self._default_log_item[item_name] = item

    def write_accesslog(self):
        default_log = '%s`%s`%s`%s`%s`%.3f' % \
                        (self._default_log_item['start_time'],
                         self._default_log_item['version'],
                         self._default_log_item['ip'],
                         self._default_log_item['url'],
                         self._default_log_item['status'],
                         self._default_log_item['request_time'],)
        access_item_s = '`'.join(['%%%s' % item[1]
                                 for item in self._log_item]) % tuple(
                                    [item[0] for item in self._log_item])
        self._logger.info('%s`%s' % (default_log, access_item_s))

    def _check_argument(self, parameter_name,
                        default_value=None, expect_types=()):
        try:
            if not default_value:
                v = self.get_argument(parameter_name)
            else:
                v = self.get_argument(parameter_name, default_value)
        except HTTPError as e:
            raise ParameterEmptyError(parameter_name)

        if expect_types and not isinstance(v, expect_types):
            raise ParameterTypeError(parameter_name)
        return v
