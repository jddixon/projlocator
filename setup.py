#!/usr/bin/python3
# projlocator/setup.py

""" Set up distutils for projlocator. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('projlocator/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='projlocator',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      py_modules=[],
      packages=['projlocator', ],
      scripts=['pl_projects', 'pl_projRelPath', ],
      description='manage software projects organized by language',
      url='https://jddixon.github.com/projlocator',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
