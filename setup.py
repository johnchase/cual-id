from setuptools import setup
from glob import glob



setup(
    name='generate-barcodes',
    version='0.0',
    py_modules=['barcodes'],
    install_requires=[
        'Click',
        'reportlab'
    ],
    scripts=glob("scripts/*"),
    entry_points='''
        [console_scripts]
        BC-generator=scripts.barcodes:cli
    '''
)
