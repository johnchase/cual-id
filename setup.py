#!/usr/bin/env python
# copied and modified from https://github.com/biocore/scikit-bio
from setuptools import find_packages, setup
from glob import glob
__version__ = "0.9.1"

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Intended Audience :: Science/Research
    Topic :: Utilities
    Topic :: Scientific/Engineering
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
    Operating System :: Microsoft :: Windows
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('A package for creating and managing sample identifiers in'
               ' comparative -omics datasets.')

with open('README.rst') as f:
    long_description = f.read()

setup(name='cual-id',
      author="John Chase",
      author_email="chasejohnh@gmail.com",
      url="https://github.com/johnchase/cual-id",
      classifiers=classifiers,
      version=__version__,
      description=description,
      long_description=long_description,
      test_suite='nose.collector',
      packages=find_packages(),
      scripts=glob("scripts/*"),
      install_requires=['click', 'reportlab']
      )
