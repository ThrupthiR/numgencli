from setuptools import setup
setup(
    name = 'numgencli',
    version = '0.1.0',
    packages = ['numgencli'],
    entry_points = {
        'console_scripts': [
            'numgencli = numgencli.__main__:main'
        ]
    })