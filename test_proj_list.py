#!/usr/bin/python3
# testProjList.py

""" Verify that the project list is correct and is read correctly. """

import unittest

from projlocator import PROJ_LIST_MAP, add_to_proj_list
# from rnglib import SimpleRNG


class TestProjList(unittest.TestCase):
    """ Verify that the project list is correct and is read correctly. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check(self, project, rel_path):
        """ Verify the relative path for the project is as expected. """

        self.assertEqual(PROJ_LIST_MAP[project], rel_path)

    def test_proj_adder(self):
        """ Verify that the add_to_proj_list() funtion works correctly. """

        self.assertEqual(add_to_proj_list('foo_c'), 'c/foo_c')
        self.assertEqual(add_to_proj_list('foo_cpp'), 'cpp/foo_cpp')
        self.assertEqual(add_to_proj_list('foo_go'),
                         'go/src/github.com/jddixon/foo_go')
        self.assertEqual(add_to_proj_list('foo_java'), 'java/foo_java')
        self.assertEqual(add_to_proj_list('foo_ml'), 'ml/foo_ml')
        self.assertEqual(add_to_proj_list('foo_py'), 'py/foo_py')
        self.assertEqual(add_to_proj_list('foo_rb'), 'rb/foo_rb')

        try:
            # pylint: disable=no-value-for-parameter
            add_to_proj_list()                     # missing required parameter
            self.fail('succesfully added project without name')
        except TypeError:
            pass

        try:
            add_to_proj_list('foo')                # missing relPath
            self.fail('succesfully added project without relPath')
        except RuntimeError:
            pass

        try:
            add_to_proj_list('foo_py', 'foo.cpp')  # wrong relPath
            self.fail('succesfully added project without relPath')
        except RuntimeError:
            pass

        try:
            add_to_proj_list('pysloc', 'py')        # existing project
            self.fail('succesfully added existing project!')
        except RuntimeError:
            pass

    def test_proj_list_map(self):
        """ Verift that existing projects have the correct relative path. """

        self.check('alertz', 'py/alertz')
        self.check('gotwitgo', 'go/src/github.com/jddixon/gotwitgo')
        self.check('xlattice', 'xlattice')


if __name__ == '__main__':
    unittest.main()
