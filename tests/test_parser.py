#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baohua'

from cetus.parser.dockerfile import DockerFileParser

if __name__ == '__main__':
    DockerFileParser('dockerfile_example').parse()