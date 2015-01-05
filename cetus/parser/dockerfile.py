#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'baohua'

from cetus.util.log import warn, debug

class DockerFileParser(object):
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.valid_starters = ['CMD', 'ENV', 'EXPOSE', 'FROM', 'RUN', 'VOLUME']
        self.parsed_ins = []

    def import_file(self, file_name):
        """
        Indicate which file will be processed
        :param file_name:
        :return:
        """
        self.file_name = file_name
        return self.file_name

    def parse(self):
        """
        Parse the dockerfile, return a list of dict
        [
        {'FROM':'debian:wheezy'},...
        ]
        :return:
        """
        if not self.file_name:
            warn('DockerFileParser cannot find file when parse()\n')
        with open(self.file_name) as f:
            cmb_str = ''
            intrution_list = []
            for l in f.readlines():
                l = l.lstrip(' ').lstrip('\t')
                if not l.startswith('\n') and not l.startswith('#'):
                    l = l.rstrip('\n')
                    if l.endswith('\\'):
                        l = l.rstrip('\\')
                        cmb_str += l
                    elif cmb_str:
                        cmb_str += l
                        intrution_list.append(cmb_str)
                        cmb_str = ''
                    else:
                        intrution_list.append(l)
        for i in intrution_list:
            hdr = i.split()[0]
            payload = i.split()[1:]
            if hdr in self.valid_starters:
                self.parsed_ins.append({hdr:payload})

        debug('parsed successfully list =', intrution_list, '\n')
        return self.parsed_ins
