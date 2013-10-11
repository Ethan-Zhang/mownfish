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


from tornado.options import define, options
import tornadoasyncmemcache

define("db_addr_list", type=list, default=['192.168.0.176:19803'])

class MemcachedClient(object):
    @staticmethod
    def instance():
        if not hasattr(MemcachedClient, "_instance"):
            MemcachedClient._instance = \
                tornadoasyncmemcache.ClientPool(options.db_addr_list, 
                                                maxclients=100)
        return MemcachedClient._instance

def get(key, callback):
    MemcachedClient.instance().get(key, callback=callback)
