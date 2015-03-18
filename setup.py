from setuptools import setup, find_packages
from glob import glob



setup(
    name='barcodes',
    version='0.0',
    py_modules=['barcodes'],
    install_requires=[
        'Click',
        'reportlab',
        'pandas'
    ],
    packages=find_packages(),
    scripts=glob("scripts/*"),
    entry_points='''
        [console_scripts]
        BC-generator=scripts.barcodes:cli
    ''',
    test_suite='nose.collector',
    extras_require={'test': ["nose >= 0.10.1", "pep8", "flake8"]},

)
