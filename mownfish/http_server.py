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
import mownfish.handlers

define('multiports', default=True)
define('num_process', default=1)

class TApplication(tornado.web.Application):

    def __init__(self, application_name):
        debug = options.env == "debug"
        app_settings = { 
                'gzip': 'on',
                'static_path': os.path.join(os.path.dirname(__file__),
                            "static"),
                'debug':debug if options.multiports else False,
                }

        self._start_time = time.time()

        tornado.web.Application.__init__(self, 
                                    mownfish.handlers.ROUTES[application_name],
                                    **app_settings)

    def stat_info(self):
        handlers = len(tornado.ioloop.IOLoop.instance()._handlers)
        return {'handlers': handlers, 
                'uptime': (time.time() - self._start_time)}
        

class Server(object):

    def __init__(self, application, prepare, log_list):
        self.application = application
        self.prepare = prepare
        self.log_list = log_list

    def start(self):

        def kill_server(sig, frame):

            LOG.warning( 'Catch SIG: %d' % sig )

            tornado.ioloop.IOLoop.instance().stop()


        # ignore Broken Pipe signal
        signal.signal(signal.SIGPIPE, signal.SIG_IGN);
                            
        # catch kill signal
        signal.signal(signal.SIGINT, kill_server)
        signal.signal(signal.SIGQUIT, kill_server)
        signal.signal(signal.SIGTERM, kill_server)
        signal.signal(signal.SIGHUP, kill_server)

        for log_name in self.log_list:
            mownfish.util.log.setup(log_name)

        LOG.info('START TORNADO WEB SERVER ...')

        version_new = True
        if [int(v_bit) for v_bit in tornado.version.split('.')] <= [2,4,1]:
            version_new = False

        for key, value in sorted(options.items(), key=lambda d:d[0]):
            value = value if version_new else value.value()
            if key not in ('help', 'log_file_prefix', 'log_to_stderr') \
                    and value is None:
                sys.stderr.write('must specify %s\n' % key)
                options.print_help()
                sys.exit(0)
            LOG.info('Options: (%s, %s)', key, value)

        try:
            sockets = tornado.netutil.bind_sockets(options.port,
                    address=options.bind_ip,
                    backlog=128)

            if not options.multiports:
                task_id = tornado.process.fork_processes(options.num_process)
            
            http_server =  \
                tornado.httpserver.HTTPServer(xheaders=True,
                                            request_callback=self.application)
            http_server.add_sockets(sockets)

            self.prepare()

            tornado.ioloop.IOLoop.instance().start()

            http_server.stop()
            tornado.ioloop.IOLoop.instance().stop()

            LOG.info('STOP TORNADO WEB SERVER ...')
        except socket.error as e:
            LOG.warning('Socket Error: %s' % str(e))
        except KeyboardInterrupt as e:
            LOG.warning('Gently Quit')
        except Exception as e:
            LOG.error('UnCaught Exception: %s' % e, exc_info=True)



    def hup(self):
        pass

