import os
import unittest


def test_mownfish():
    loader = unittest.TestLoader()
    test_path = os.path.split(os.path.realpath(__file__))[0]
    all_tests = loader.discover(test_path)
    suite = unittest.TestSuite()
    suite.addTests(all_tests)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test_mownfish()
