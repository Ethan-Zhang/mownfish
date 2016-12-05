mownfish
==========
[![Build Status](https://travis-ci.org/Ethan-Zhang/mownfish.svg)](https://travis-ci.org/Ethan-Zhang/mownfish)

Overview
==========

The mownfish is a productional skeleton for tornado. It helps us making our own
application with tornado framework rapidly and normativity. Mownfish is
extremely lightweight, containing fewer addition with tornado.
The name of mownfish is comming from a crop I have ever worked with. The
crop had a fish mascot which face was very weird, so I named it mownfish and
for my project name.

Feature
==========

* A productional code structure. Let you focus more on the application code
  not the framework it self.
* Init your project with cmd `fishing`. Init your own project skeleton code which copied from mownfish, and replace everything with your project name. using one single cmd.
* A customized log module. For the Tornado v2.4 have not made its own log module yet, and in production env we want a customized access log to analyze the data. See more details and examples from [wiki](https://github.com/Ethan-Zhang/mownfish/wiki/Log).

Installation
------------
**Install from pypi:**

    pip install mownfish

**Install from source:**

    git clone https://github.com/Ethan-Zhang/mownfish.git
    cd mownfish
    python setup.py install

Init and Run your own project skeleton
------------
    fishing $project_name
    cd $project_name
    python $project_name/cmd/mownfishd --port=$port_num

Example
------------
1. add handler file in __project__/handlers/
2. modify the project's router in  __project__/handlers/\_\_init\_\_.py, add a route item.
3. add the prepareration including periodicity task in __project__/cmd/mownfishd file, modify the method `prepare()`

Requirements
------------
The following libraries are required

* [tornado](http://github.com/facebook/tornado)

*Compatibale with all versions of tornado, include 2.x, 3.x, 4.x. I have tested the performance between v2.4 and v3.x, and the version 2.4 have 30% enhance than version 3.1.*

Contributing
-----
All pull requests are welcome!

Issues
------

Please report any issues via [github issues](https://github.com/Ethan-Zhang/mownfish/issues)
