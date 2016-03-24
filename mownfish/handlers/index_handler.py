# -*- coding: utf-8 -*-

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
            self.finish({'code': e.e_code, 'msg': '%s' % e})
        except Exception as e:
            LOG.error(e, exc_info=True)
            self.finish({'code': ECODE.DEFAULT, 'msg': 'Unknown'})

        finally:
            self.write_accesslog()
