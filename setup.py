from setuptools import setup


setup(
    name='generate-barcodes',
    version='0.0',
    py_modules=['barcodes'],
    install_requires=[
        'Click',
        'reportlab'
    ],
    entry_points='''
        [console_scripts]
        BC-generator=barcodes:cli
    '''
)
