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

from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado.options import define, options

from mownfish.util.log import LOG
from mownfish.error import ParameterEmptyError
from mownfish.error import ParameterTypeError

class BaseHandler(RequestHandler):

    def set_default_headers(self):
        self.set_header('Server', options.server_name)

    def on_connection_close(self):
        LOG.info('connection close.')

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
