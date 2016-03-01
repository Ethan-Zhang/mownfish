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

'''Define Error 
'''

class ErrorCode(object):
    DEFAULT = 0xff
    SUCCESS = 0x00

    PARAMETERS = 100 
    PARAMETERS_EMPTY = 101 
    PARAMETERS_TYPE = 102 
    PARAMETERS_DATA = 103 

    TCP = 500 
    HTTP = 501 

    DB_ERROR = 300 
    DB_EMPTY = 301 

class ErrorMessage(object):
    SUCCESS = 'SUCCESS'
    pass

class BaseError(Exception):
    def __init__(self, msg='Default'):
        self.e_code = ErrorCode.DEFAULT
        self.e_msg = 'Uncaught Exception: %s' % Exception.message

    def __str__(self):
        return self.e_msg 
    pass

class ParameterError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Invalid Parameter: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterEmptyError(ParameterError):
    def __init__(self, parameter_name=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Parameter[%s] Can\'t Be NULL' % parameter_name.upper()
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterTypeError(ParameterError):
    def __init__(self, parameter_name=''):
        self.e_code = ErrorCode.PARAMETERS
        self.e_msg = 'Parameter[%s]\'type Is Invalid' % parameter_name.upper()
        pass

    def __str__(self):
        return self.e_msg 
    pass

class ParameterDataError(ParameterError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.PARAMETERS_DATA 
        self.e_msg = 'Invalid Date: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class DBError(BaseError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_ERROR 
        self.e_msg = 'DB Error: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class DBEmpty(DBError):
    def __init__(self, msg=''):
        self.e_code = ErrorCode.DB_EMPTY 
        self.e_msg = 'DB Empty: %s' % msg
        pass

    def __str__(self):
        return self.e_msg 
    pass

class NetworkError(BaseError):
    def __init__(self, msg=''):
        self.e_code = 500
        self.e_msg = 'Network IO Error: %s' % msg

    def __str__(self):
        return self.e_msg

class HttpError(NetworkError):
    def __init__(self, msg=''):
        self.e_code = 502
        self.e_msg = 'Client Http Error: %s' % msg

    def __str__(self):
        return self.e_msg

class ServiceError(NetworkError):
    def __init__(self, msg=''):
        self.e_code = 503
        self.e_msg = 'Client Service Error: %s' % msg

    def __str__(self):
        return self.e_msg
