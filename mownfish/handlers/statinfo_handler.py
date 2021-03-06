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


class StatInfoHandler(BaseHandler):

    def get(self):
        try:
            result = {'code': ECODE.SUCCESS, 'msg': EMSG.SUCCESS}
            stat_info = self.application.stat_info()
            result['stat_info'] = {}
            result['stat_info']['handlers_n'] = stat_info['handlers']
            uptime = stat_info['uptime']
            up_day = uptime // 86400
            up_hour = (uptime - up_day*86400) // 3600
            up_minute = (uptime - up_day*86400 - up_hour*3600) // 60
            up_second = uptime - up_day*86400 - up_hour*3600 - up_minute*60
            result['stat_info']['uptime'] = "%ddays, %dhours, %dminute, \
                                             %.3fseconds" % (up_day, up_hour,
                                                             up_minute,
                                                             up_second)
            self.finish(result)
            self.set_accesslog_item('status', 'SUCCESS')

        except BaseError as e:
            LOG.error(e, exc_info=True)
            self.finish({'code': e.e_code, 'msg': '%s' % e})
        except Exception as e:
            LOG.error(e, exc_info=True)
            self.finish({'code': ECODE.DEFAULT, 'msg': 'Unknown'})

        finally:
            self.write_accesslog()
