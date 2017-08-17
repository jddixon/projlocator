#!/usr/bin/python3
# test_rel_pathForProject.py
"""
Exercise the code which determines the relative path given a project name.
"""
import time
import unittest

from rnglib import SimpleRNG
from projlocator import proj_rel_path_from_name


class TestRelPathForProject(unittest.TestCase):
    """
    Exercise the code which determines the relative path given a project name.
    """

    def setUp(self):
        self.rng = SimpleRNG(time.time())

    def tearDown(self):
        pass

    # utility functions #############################################

    # actual unit tests #############################################
    def test_rel_path(self):

        # dir -> lang tests -----------------------------------------
        try:
            proj_rel_path_from_name(None)
            self.fail("didn't catch missing project name")
        # pylint: disable=bare-except
        except BaseException:
            pass

        try:
            proj_rel_path_from_name('')
            self.fail("didn't catch empty project name")
        # pylint: disable=bare-except
        except BaseException:
            pass

        # failure to match should return ""
        self.assertEqual(proj_rel_path_from_name('/'), "")
        self.assertEqual(proj_rel_path_from_name('foo'), "")

        # these names must be filtered out
        self.assertEqual(proj_rel_path_from_name('dot'), "")
        self.assertEqual(proj_rel_path_from_name('ghp.css'), "")
        self.assertEqual(proj_rel_path_from_name('img'), "")
        self.assertEqual(proj_rel_path_from_name('LICENSE.md'), "")
        self.assertEqual(proj_rel_path_from_name('TODO'), "")

        # these are real project names
        for pair in [
                ('cryptoserver_go',
                    'go/src/github.com/jddixon/cryptoserver_go'),
                ('ctries_go', 'go/src/github.com/jddixon/ctries_go'),
                ('merkletree', 'py/merkletree'),
                ('nlp', 'py/nlp'),
                ('projlocator', 'py/projlocator'),
                ('pysloc', 'py/pysloc'),
                ('rnglib', 'py/rnglib'),
                ('xgo_go', 'go/src/github.com/jddixon/xgo_go'),
                ('xlreg_c', 'c/xlreg_c'),
                ('xlreg_cpp', 'cpp/xlreg_cpp'),
                ('xlreg_java', 'java/xlreg_java'),
                ('xlreg_rb', 'rb/xlreg_rb'),
                ('xlreg_ml', 'ml/xlreg_ml'),
                ('xlreg_py', 'py/xlreg_py'),

                # top level project(s)
                ('xlattice', 'xlattice'),

        ]:
            self.assertEqual(proj_rel_path_from_name(pair[0]), pair[1])

        # these are phoney project names -- we want the system to guess
        for pair in [
            ('foo_c', 'c/foo_c'),
            ('foo_go', 'go/src/github.com/jddixon/foo_go'),
            ('foo_cpp', 'cpp/foo_cpp'),
            ('foo_java', 'java/foo_java'),
            ('foo_rb', 'rb/foo_rb'),
            ('foo_ml', 'ml/foo_ml'),
            ('foo_py', 'py/foo_py'),
        ]:
            self.assertEqual(proj_rel_path_from_name(pair[0]), pair[1])


if __name__ == '__main__':
    unittest.main()
