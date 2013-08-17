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

''' tornado web server
'''

import os
import sys
import time
import signal
import socket

import tornado.web
import tornado.httpserver
from tornado.options import define, options

from mownfish.util.log import LOG
import mownfish.domain
import timer_task

class TApplication(tornado.web.Application):

    def __init__(self):
        debug = options.env == "debug"
        app_settings = { 
                'gzip': 'on',
                'static_path': os.path.join(os.path.dirname(__file__),
                            "static"),
                'debug':debug,
                }

        handlers = [
            (r'/sayhi', mownfish.domain.HelloHandler),
        ]
        
        tornado.web.Application.__init__(self, handlers, **app_settings)

class Server(object):

    def __init__(self):
        pass

    def start(self):

        def kill_server(sig, frame):

            LOG.warning( 'Catch SIG: %d' % sig )
            
            tornado.ioloop.IOLoop.instance().stop()


        # 忽略Broken Pipe信号
        signal.signal(signal.SIGPIPE, signal.SIG_IGN);
                            
        # 处理kill信号
        signal.signal(signal.SIGINT, kill_server)
        signal.signal(signal.SIGQUIT, kill_server)
        signal.signal(signal.SIGTERM, kill_server)
        signal.signal(signal.SIGHUP, kill_server)

        LOG.info('START TORNADO WEB SERVER ...')

        for key, value in options.iteritems():
            LOG.info('Options: (%s, %s)', key, value.value())


        try:
            sockets = tornado.netutil.bind_sockets(options.port,
                    address=options.bind_ip,
                    backlog=128)

            http_server =  \
                tornado.httpserver.HTTPServer(xheaders=True, request_callback=TApplication())
            http_server.add_sockets(sockets)

            tt = timer_task.TimerTask()
            tt.start()

            tornado.ioloop.IOLoop.instance().start()

            http_server.stop()
            tornado.ioloop.IOLoop.instance().close()

            LOG.info('STOP TORNADO WEB SERVER ...')
        except socket.error as e:
            LOG.warning('Socket Error: %s', str(e))
        except KeyboardInterrupt as e:
            LOG.warning('Gently Quit')
        except Exception as e:
            LOG.error('UnCaught Exception: %s', e)



    def hup(self):
        pass

