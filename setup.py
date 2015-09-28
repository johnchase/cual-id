#!/usr/bin/env python
# copied and modified from https://github.com/biocore/scikit-bio
from setuptools import find_packages, setup
from glob import glob
__version__ = "0.0.1-dev"


description = ('Make a pdf out of barcodes')

with open('README.md') as f:
    long_description = f.read()

setup(name='Cual-ID',
      version=__version__,
      description=description,
      long_description=long_description,
      test_suite='nose.collector',
      packages=find_packages(),
      scripts=glob("scripts/*"),
      install_requires=['click', 'reportlab']
      )
