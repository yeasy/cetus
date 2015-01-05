#!/usr/bin/env python

"""Setuptools params"""

from setuptools import setup, find_packages
from os.path import join

# Get version number from source tree
import sys
sys.path.append('.')
from cetus.util.common import VERSION

scripts = [join('bin', fn) for fn in ['cetus-client', 'cetus-server']]

modname = distname = 'cetus'

setup(
    name=distname,
    version=VERSION,
    description='Docker visualization',
    author='Baohua Yang',
    author_email='yangbaohua@gmail.com',
    packages=find_packages(),
    long_description="""
        https://github.com/yeasy/cetus
        """,
    classifiers=[
        "License :: N/A :: TBD License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: TBD",
        ],
    keywords='Docker Visualization',
    license='TBD',
    install_requires=[
        'pygraphviz>=1.0',
        'setuptools>=1.0',
    ],
    scripts=scripts,
)
