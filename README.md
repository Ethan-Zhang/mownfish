mownfish
==========

The mownfish is a productional skeleton for tornado. It helps us making our own
application with tornado framework rapidly and normativity. Mownfish is
extremely lightweight, containing fewer addition with tornado.
The name of mownfish is comming from a crop I have ever worked with. The
crop had a fish mascot which face was very weird, so I named it mownfish and
for my project name.

feature
==========

* A productional code structure. Let you focus more on the application code
  not the framework it self.
* Init script **fishing**. Init your code from mownfish with its own package name
  and certain lisense, using one single cmd.
* Tornado version base on version 2.4. I have tested the performance between
  v2.4 and v3.x, and the version 2.4 have 30% enhance than version 3.1.
* A log model. Because Tornado v2.4 do not have its own log model yet, so I
  add a log model in mownfish.

Installation
------------
**Install from pypi:**

    pip install mownfish

**Install from source:**

    git clone https://github.com/Ethan-Zhang/mownfish.git
    cd mownfish
    python setup.py install

Init your code    
------------
    mownfish/script/fishing $dst_path -n $project_name -l $lisense_file

Example
------------

**code**

1. add your handler in project/domain/
2. modify the routes project/domain/__init__.py ROUTES
3. the prepareration include periodcallback timer before HTTPServer start 
   writes in project/cmd/project-bin prepare() method

**run**

    python $project_name/cmd/$project_name --port

Requirements
------------
The following libraries are required

* [tornado==2.4](http://github.com/facebook/tornado)

Issues
------

Please report any issues via [github issues](https://github.com/Ethan-Zhang/mownfish/issues)
