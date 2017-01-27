#!/usr/bin/python3
# sharedev/testLangForProject.py

""" Check functioning of get_lang_for_project. """

import time
import unittest

from rnglib import SimpleRNG
from projlocator import get_lang_for_project


class TestLangForProject(unittest.TestCase):
    """ Check functioning of get_lang_for_project. """

    def setUp(self):
        self.rng = SimpleRNG(time.time())

    def tearDown(self):
        pass

    # utility functions #############################################

    # actual unit tests #############################################
    def test_mapping(self):
        """
        Various tests of get_lang_for_project(), some with expected
        results, some expected to fail.
        """

        # dir -> lang tests -----------------------------------------
        try:
            get_lang_for_project(None)
            self.fail("didn't catch missing project name")
        # pylint: disable=bare-except
        except:
            pass

        # failure to match should return ""
        self.assertEqual(get_lang_for_project('/'), "")
        self.assertEqual(get_lang_for_project('foo'), "")

        # these names must be filtered out
        self.assertEqual(get_lang_for_project('dot'), "")
        self.assertEqual(get_lang_for_project('ghp.css'), "")
        self.assertEqual(get_lang_for_project('img'), "")
        self.assertEqual(get_lang_for_project('LICENSE.md'), "")
        self.assertEqual(get_lang_for_project('TODO'), "")

        # these are real project names
        self.assertEqual(get_lang_for_project('xlreg_c'), 'c')
        self.assertEqual(get_lang_for_project('xlreg_cpp'), 'cpp')
        self.assertEqual(get_lang_for_project('xlreg_java'), 'java')
        self.assertEqual(get_lang_for_project('cryptoserver_go'), 'go')
        self.assertEqual(get_lang_for_project('cryptoserver_go'), 'go')
        self.assertEqual(get_lang_for_project('ctries_go'), 'go')
        self.assertEqual(get_lang_for_project('gotwitgo'), 'go')
        self.assertEqual(get_lang_for_project('xgo_go'), 'go')
        self.assertEqual(get_lang_for_project('xlreg_ml'), 'ml')
        self.assertEqual(get_lang_for_project('merkletree'), 'py')
        self.assertEqual(get_lang_for_project('rnglib'), 'py')
        self.assertEqual(get_lang_for_project('xlreg_py'), 'py')
        self.assertEqual(get_lang_for_project('xlreg_rb'), 'rb')

        # top-level project(s)
        self.assertEqual(get_lang_for_project('xlattice'), 'top')

if __name__ == '__main__':
    unittest.main()
