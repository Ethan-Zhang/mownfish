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
import re

def format_timestamp(timestamp):
    time_format = time.strftime('%Y-%m-%d %H:%M:%S',
                                time.localtime(timestamp))
    return time_format

def format_timestamp_date(timestamp):
    date_format = time.strftime('%Y%m%d', time.localtime(timestamp))
    return date_format

def date_to_timestamp(date):   
    if re.match('\d{8}', date):
        return int(time.mktime(time.strptime(date, '%Y%m%d')))
    elif re.match('\d{4}-\d{2}-\d{2}', date):
        return int(time.mktime(time.strptime(date, '%Y-%m-%d')))
    else:
        raise ValueError('invaild date format')

def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

