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

'''
localtion
----------
* /hello

feature
----------
* Process-level global variable
* Asynchronous Http Request 
* Decorator Demo
'''

import os
import time

import tornado.web
from tornado.web import HTTPError
from tornado.httpclient import AsyncHTTPClient

from mownfish.util.log import LOG

from base_handler import BaseHandler 
from mownfish.error import ErrorCode as ECODE
from mownfish.error import BaseError


class HelloHandler(BaseHandler):

    @tornado.web.asynchronous
    def get(self):
        try:
            # 只检查参数,不作业务逻辑处理
            name = self._check_argument('name', expect_types=(str, unicode))

            self.finish({'code': ECODE.SUCCESS, 'msg': u'Hello! %s' % name})

            if __debug__:
                LOG.debug(self)

        except BaseError, e:
            LOG.error(e, exc_info=True)
            self.finish({'code':e.e_code, 'msg': '%s' % e})
        except Exception, e:
            LOG.error(e, exc_info=True)
            self.finish({'code':ECODE.DEFAULT, 'msg':
                'Unknown'})


