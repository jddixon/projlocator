#!/usr/bin/python3
# testDirLangMaps.py

""" Verify functioning of get_lang_from_dir(). """

import time
import unittest

from rnglib import SimpleRNG
from projlocator import get_dir_for_lang, get_lang_for_dir


class TestMaps(unittest.TestCase):
    """ Verify functioning of get_lang_from_dir(). """

    def setUp(self):
        self.rng = SimpleRNG(time.time())

    def tearDown(self):
        pass

    def test_maps(self):
        """
        Actual test of get_lang_from_dirs(), which examines a path to
        determine the main language of a package.
        """

        # dir -> lang tests -----------------------------------------
        try:
            get_lang_for_dir(None)
            self.fail("didn't catch missing directory name")
        # pylint: disable=bare-except
        except BaseException:
            pass

        try:
            get_lang_for_dir('foo/bar')
            self.fail("didn't catch relative path")
        # pylint: disable=bare-except
        except BaseException:
            pass

        # failure to match just returns None
        self.assertEqual(get_lang_for_dir('/'), None)
        self.assertEqual(get_lang_for_dir('/foo'), None)

        self.assertEqual(
            get_lang_for_dir('/home/jdd/dev/gh-pages/projects/'), 'G')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/c/'), 'c')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/cpp/'), 'cpp')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/java/'), 'java')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/node/'), 'js')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/py/'), 'py')
        self.assertEqual(
            get_lang_for_dir('/home/jdd/dev/go/src/github.com/jddixon/'), 'go')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/ml/'), 'ml')
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/rb/'), 'rb')

        # dummy 'top' language
        self.assertEqual(get_lang_for_dir('/home/jdd/dev/'), 'top')

        # lang -> dir tests -----------------------------------------
        self.assertEqual(get_dir_for_lang('foo'), None)
        self.assertEqual(
            get_dir_for_lang('G'),
            '/home/jdd/dev/gh-pages/projects/')
        self.assertEqual(get_dir_for_lang('c'), '/home/jdd/dev/c/')
        self.assertEqual(get_dir_for_lang('cpp'), '/home/jdd/dev/cpp/')
        self.assertEqual(get_dir_for_lang('java'), '/home/jdd/dev/java/')
        self.assertEqual(get_dir_for_lang('js'), '/home/jdd/dev/node/')
        self.assertEqual(get_dir_for_lang('py'), '/home/jdd/dev/py/')
        self.assertEqual(get_dir_for_lang('go'),
                         '/home/jdd/dev/go/src/github.com/jddixon/')
        self.assertEqual(get_dir_for_lang('ml'), '/home/jdd/dev/ml/')
        self.assertEqual(get_dir_for_lang('rb'), '/home/jdd/dev/rb/')

        # dummy 'top' language
        self.assertEqual(get_dir_for_lang('top'), '/home/jdd/dev/')


if __name__ == '__main__':
    unittest.main()
