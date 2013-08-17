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


import time

from tornado import ioloop

from mownfish.util.log import LOG

class TimerTask(object):
    def __init__(self):
        def _test_task():
            LOG.debug("PeriodicCallback")
        self._timer_task = \
                ioloop.PeriodicCallback(_test_task,20*1000)
    def start(self):
        self._timer_task.start()

    def stop(self):
        self._timer_task.stop()

