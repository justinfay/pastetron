#!/usr/bin/env python

from __future__ import with_statement

from setuptools import setup, find_packages
from buildkit import *


META = get_metadata('pastetron/__init__.py')


setup(
    name='pastetron',
    version=META['version'],
    description='A pastebin application',
    long_description=read('README'),
    url='https://github.com/kgaughan/pastetron/',
    license='MIT',
    packages=find_packages(exclude='tests'),
    zip_safe=False,
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,

    entry_points={
        'console_scripts': [
        ],
        'paste.app_factory': [
            'main=pastetron:paste',
        ],
    },

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    author=META['author'],
    author_email=META['email']
)
