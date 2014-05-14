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
DB code sample

from tornado.options import define, options
import tornadoasyncmemcache
import redis
from sqlalchemy import create_engine
from sqlalchemy import text

define("db_addr_list", type=list, default=['192.168.0.176:19803'])
define("redis_ip", type=str, default='192.168.1.96')
define("redis_port", type=int, default=19821)
define("mysqldb_engine", type=str,
        default='mysql://root:ktep@192.168.0.27:3306/KTEP')

class MemcachedClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                tornadoasyncmemcache.ClientPool(options.db_addr_list,
                                                maxclients=100)
        return cls._instance

class RedisClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                redis.StrictRedis(host=options.redis_ip,
                                    port=options.redis_port, 
                                    db=0)
        return cls._instance

class MySQLClient(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = \
                    create_engine(options.mysqldb_engine, echo=True)
        return cls._instance

def get_memcached(key, callback):
    MemcachedClient().get(key, callback=callback)

def get_redis(key):
    RedisClient().get(key)

def set_redis(key, value):
    RedisClient().set(key, value)

def get_mysql(param):
    sql="select * from table_name where param=:param";
    result = MySQLClient().execute(text(sql), {'param':param}).fetchall()
    return result
'''
