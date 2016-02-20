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

# If ../__init__.py exists, add ../ to Python search path, so that
# it will override what happens to be installed in /usr/(local/)lib/python...
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
                                   os.pardir,
                                    os.pardir,
                                    os.pardir))
if os.path.exists(os.path.join(possible_topdir, 'mownfish', '__init__.py')):
        sys.path.insert(0, possible_topdir)


import mownfish.util.config
from mownfish.util import log as logging
from mownfish import http_server
import mownfish.timer_task

def prepare():
    task = mownfish.timer_task.TimerTask()
    task.start()

def main():
    mownfish.util.config.init_options()
    log_list = ('Main','Access')

    server = http_server.Server(http_server.TApplication('mownfish'), prepare, log_list)
    server.start()

if __name__ == '__main__':
    main()
