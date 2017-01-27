#!/usr/bin/python3
# testProjdirFromName.py

""" Verify correct results from proj_dir_from_name(). """

import time
import unittest

from rnglib import SimpleRNG
from projlocator import proj_dir_from_name


class TestProjDirFromName(unittest.TestCase):
    """ Verify correct results from proj_dir_from_name(). """

    def setUp(self):
        self.rng = SimpleRNG(time.time())

    def tearDown(self):
        pass

    def test_mapping(self):
        """
        Check functionality with cases expected to succeed and other
        cases expected to fail.
        """

        # dir -> lang tests -----------------------------------------
        try:
            proj_dir_from_name(None)
            self.fail("didn't catch missing project name")
        # pylint: disable=bare-except
        except:
            pass

        # failure to match should return ""
        self.assertEqual(proj_dir_from_name('/'), "")
        self.assertEqual(proj_dir_from_name('foo'), "")

        # these names must be filtered out
        self.assertEqual(proj_dir_from_name('dot'), "")
        self.assertEqual(proj_dir_from_name('ghp.css'), "")
        self.assertEqual(proj_dir_from_name('img'), "")
        self.assertEqual(proj_dir_from_name('LICENSE.md'), "")
        self.assertEqual(proj_dir_from_name('TODO'), "")

        # these are real project names
        self.assertEqual(proj_dir_from_name('alertz'),
                         '/home/jdd/dev/py/alertz')

        self.assertEqual(proj_dir_from_name('buildlist'),
                         '/home/jdd/dev/py/buildlist')

        self.assertEqual(proj_dir_from_name('bindex'),
                         '/home/jdd/dev/py/bindex')

        self.assertEqual(proj_dir_from_name('cryptoserver_go'),
                         '/home/jdd/dev/go/src/github.com/jddixon/cryptoserver_go')

        self.assertEqual(proj_dir_from_name('fieldz'),
                         '/home/jdd/dev/py/fieldz')

        self.assertEqual(proj_dir_from_name('gotwitgo'),
                         '/home/jdd/dev/go/src/github.com/jddixon/gotwitgo')

        self.assertEqual(proj_dir_from_name('pzog'),
                         '/home/jdd/dev/py/pzog')

        self.assertEqual(proj_dir_from_name('ringd'),
                         '/home/jdd/dev/py/ringd')

        self.assertEqual(proj_dir_from_name('xgo_go'),
                         '/home/jdd/dev/go/src/github.com/jddixon/xgo_go')

        self.assertEqual(proj_dir_from_name('xlreg_ml'),
                         '/home/jdd/dev/ocaml/xlreg_ml')

        self.assertEqual(proj_dir_from_name('magicsack'),
                         '/home/jdd/dev/py/magicsack')

        self.assertEqual(proj_dir_from_name('merkletree'),
                         '/home/jdd/dev/py/merkletree')

        self.assertEqual(proj_dir_from_name('nlhtree_py'),
                         '/home/jdd/dev/py/nlhtree_py')

        self.assertEqual(proj_dir_from_name('rnglib'),
                         '/home/jdd/dev/py/rnglib')

        self.assertEqual(proj_dir_from_name('xl_test_data'),
                         '/home/jdd/dev/dat/xl_test_data')

        self.assertEqual(proj_dir_from_name('xlreg_c'),
                         '/home/jdd/dev/c/xlreg_c')

        self.assertEqual(proj_dir_from_name('xlreg_cpp'),
                         '/home/jdd/dev/cpp/xlreg_cpp')

        self.assertEqual(proj_dir_from_name('xlreg_java'),
                         '/home/jdd/dev/java/xlreg_java')

        self.assertEqual(proj_dir_from_name('xlreg_rb'),
                         '/home/jdd/dev/ruby/xlreg_rb')

        # TOP LEVEL PROJECT(S)
        self.assertEqual(proj_dir_from_name('xlattice'),
                         '/home/jdd/dev/xlattice')

        # these have been returned incorrectly ======================

if __name__ == '__main__':
    unittest.main()
