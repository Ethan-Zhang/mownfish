import sys
import os
import unittest

from tornado.options import define, options, Error

from mownfish.util import config


class ConfigTest(unittest.TestCase):

    def setUp(self):
        self.test_path = os.path.split(os.path.realpath(__file__))[0]
        self.test_config_file = os.path.join(self.test_path, 'etc',
                                             'mownfish.conf')
        self.test_log_path = os.path.join(self.test_path, 'log')
        sys.argv.append('--cfg_file=%s' % self.test_config_file)
        sys.argv.append('--port=8086')
        os.mkdir(self.test_log_path)
        sys.argv.append('--log_path=%s' % self.test_log_path)

    def tearDown(self):
        os.rmdir(self.test_log_path)

    def test_command_line(self):
        config.init_options()
        self.assertEqual(options.port, 8086)
        self.assertEqual(options.bind_ip, '127.0.0.1')
        

if __name__ == '__main__':
    unittest.main()

