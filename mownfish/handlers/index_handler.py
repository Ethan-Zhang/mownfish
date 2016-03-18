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
import time

import tornado.web
from tornado.web import HTTPError
from tornado.httpclient import AsyncHTTPClient

from mownfish.util.log import LOG

from base_handler import BaseHandler 
from mownfish.error import ErrorCode as ECODE
from mownfish.error import ErrorMessage as EMSG
from mownfish.error import BaseError


class IndexHandler(BaseHandler):

    def get(self):
        try:
            result = ('<h2>Hello Mownfish</h2>'
                      ' It has never been so easy to create a tornado project')
            self.finish(result)
            self.set_accesslog_item('status', 'SUCCESS')

        except BaseError as e:
            LOG.error(e, exc_info=True)
            self.finish({'code':e.e_code, 'msg': '%s' % e})
        except Exception as e:
            LOG.error(e, exc_info=True)
            self.finish({'code':ECODE.DEFAULT, 'msg':
                'Unknown'})

        finally:
            self.write_accesslog()


