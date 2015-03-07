#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.0.10'

setup(
    name='habits',
    version=version,
    description='A lightweight habit tracker with a simple REST API.',
    long_description=open('README.rst').read(),
    author='Christopher Su',
    author_email='chris+gh@christopher.su',
    license='GPL v3',
    keywords=['habits', 'quantified self', 'data', 'api'],
    url='http://github.com/csu/habits',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-RESTful',
        'dataset',
    ],
    entry_points={
        'console_scripts': [
            'habits=habits:production'
        ],
    }
)