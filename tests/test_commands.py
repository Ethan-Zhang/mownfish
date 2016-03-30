import sys
import os
import subprocess
import tempfile
import shutil
import unittest



class CommandsTest(unittest.TestCase):
    project_name = 'testproject'

    def setUp(self):
        self.temp_path = tempfile.mkdtemp()
        self.proj_path = os.path.join(self.temp_path, self.project_name)
        self.proj_mod_path = os.path.join(self.proj_path, self.project_name)

    def tearDown(self):
        shutil.rmtree(self.temp_path)

    def call(self, **kwargs):
        with tempfile.TemporaryFile() as out:
            args =  ('fishing', self.project_name)
            return subprocess.call(args, stdout=out, stderr=out,
                                   cwd=self.temp_path, **kwargs)
    def test_fishing(self):
        self.assertEqual(0, self.call())

        assert os.path.exists(os.path.join(self.proj_path, self.project_name))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'cmd'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'cmd',
                                           '__init__.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'cmd',
                                           'mownfishd.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'db.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'error.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path,
                                           'http_server.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path,
                                           'timer_task.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'handlers'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'handlers',
                                           'base_handler.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'handlers',
                                           'index_handler.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'handlers',
                                           'statinfo_handler.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'handlers',
                                           '__init__.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util',
                                           '__init__.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util',
                                           'config.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util',
                                           'commonutils.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util',
                                           'log.py'))
        assert os.path.exists(os.path.join(self.proj_mod_path, 'util',
                                           'multiprocesslogging.py'))


if __name__ == '__main__':
    unittest.main()

