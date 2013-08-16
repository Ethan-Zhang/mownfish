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

