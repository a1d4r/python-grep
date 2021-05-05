from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name='mygrep',
    description='A command-line utility for searching plain-text data sets '
    'for lines that contain a specified substring',
    version='1.0',
    author='Aidar Garikhanov',
    author_email='a1d4r@yandex.ru',
    packages=find_packages(),
    install_requires=[
        'click==7.1.2',
        'click-pathlib==2020.3.13.0',
    ],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={'console_scripts': ['mygrep = myapp.app:run']},
)
