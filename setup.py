from setuptools import setup
from glob import glob



setup(
    name='generate-barcodes',
    version='0.0',
    py_modules=['barcodes'],
    install_requires=[
        'Click',
        'reportlab',
        'pandas'
    ],
    engine='python',
    scripts=glob("scripts/*"),
    entry_points='''
        [console_scripts]
        BC-generator=scripts.barcodes:cli
    ''',
    test_suite='nose.collector',
    extras_require={'test': ["nose >= 0.10.1", "pep8", "flake8"]},

)
