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


from __future__ import print_function
import os
import re
import string
import importlib
import sys
import shutil
import re
import argparse

import mownfish

TEMPLATES_TO_RENDER = (
        ('${project_name}', 'http_server.py.tmpl'),
        ('${project_name}', 'timer_task.py.tmpl'),
        ('${project_name}', 'cmd', 'mownfishd.py.tmpl'),
        ('${project_name}', 'handlers', '__init__.py.tmpl'),
        ('${project_name}', 'handlers', 'base_handler.py.tmpl'),
        ('${project_name}', 'handlers', 'statinfo_handler.py.tmpl'),
        ('${project_name}', 'util', 'config.py.tmpl'),
        ('${project_name}', 'util', 'log.py.tmpl'),
        )
IGNORE = shutil.ignore_patterns('*.pyc', '.svn')

def _is_valid_name(project_name):
    def _module_exists(module_name):
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            return False

    if not re.search(r'^[_a-zA-Z]\w*$', project_name):
        print('Error: Project names must begin with a letter and contain'\
                ' only\nletters, numbers and underscores')
    elif os.path.exists(project_name):
        print('Error: Directory %r already exists' % project_name)
    elif _module_exists(project_name):
        print('Error: Module %r already exists' % project_name)
    else:
        return True
    return False

def render_templatefile(path, **kwargs):
    with open(path, 'rb') as fp:
        raw = fp.read().decode('utf-8')

    content = string.Template(raw).substitute(**kwargs)
    render_path = path[:-len('.tmpl')] if path.endswith('.tmpl') else path
    with open(render_path, 'wb') as fp:
        fp.write(content.encode('utf-8'))
    if path.endswith('.tmpl'):
        os.remove(path)

CAMELCASE_INVALID_CHARS = re.compile('[^a-zA-Z\d]')
def string_camelcase(string):
    """ Convert a word  to its CamelCase version and remove invalid chars

    >>> string_camelcase('lost-pound')
    'LostPound'
    
    >>> string_camelcase('missing_images')
    'MissingImages'
    """
    return CAMELCASE_INVALID_CHARS.sub('', string.title())

def main():

    parser = argparse.ArgumentParser(description='create new Tornado project')
    parser.add_argument("project_name", metavar='Name', type=str,
                        help="project name")
    args = parser.parse_args()

    project_name = args.project_name
    if not _is_valid_name(project_name):
        sys.exit(1)

    templates_dir = os.path.join(mownfish.__path__[0], 'templates')
    shutil.copytree(templates_dir, project_name, ignore=IGNORE)
    shutil.move(os.path.join(project_name, 'module'), os.path.join(project_name,
        project_name))
    
    for paths in TEMPLATES_TO_RENDER:
        path = os.path.join(*paths)
        tplfile = os.path.join(project_name,
                string.Template(path).substitute(project_name=project_name))
        render_templatefile(tplfile, project_name=project_name,
                ProjectName=string_camelcase(project_name))
    print("New Scrapy project %r, using template directory %r, created in:" % (project_name, 
                            templates_dir))
    print("    %s" % os.path.abspath(project_name))
    print("You can start your Tornado project with:")
    print("    cd %s" % project_name)
    print("    python %s/cmd/mownfishd.py --port=8086" % project_name)

if __name__ == '__main__':
    main()
