#!/usr/bin/python3
# projlocator/setup.py

""" Setuptools project configuration for projlocator. """

from os.path import exists
from setuptools import setup

long_desc = None
if exists('README.md'):
    with open('README.md', 'r') as file:
        long_desc = file.read()

setup(name='projlocator',
      version='0.0.11',
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      long_description=long_desc,
      packages=['projlocator'],
      package_dir={'': 'src'},
      py_modules=[],
      include_package_data=False,
      zip_safe=False,
      scripts=['src/pl_projects', 'src/pl_projRelPath'],
      ext_modules=[],
      description='manage software projects organized by language',
      url='https://jddixon.github.io/projlocator',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python 2',
          'Programming Language :: Python 2.7',
          'Programming Language :: Python 3',
          'Programming Language :: Python 3.5',
          'Programming Language :: Python 3.6',
          'Programming Language :: Python 3.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
