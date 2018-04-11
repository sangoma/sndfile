#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return open(file_path, encoding='utf-8').read()


setup(
    name='sndfile',
    version='0.1',
    description='A CFFI wrapper around libsndfile',
    author='Simon Gomizelj',
    author_email='simon@vodik.xyz',
    url='https://github.com/sangoma/sndfile',
    packages=find_packages(),
    setup_requires=[
        'cffi>=1.0.0',
    ],
    install_requires=[
        'cffi>=1.0.0',
    ],
    cffi_modules=[
        'sndfile/build.py:ffi'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities'
    ],
)
