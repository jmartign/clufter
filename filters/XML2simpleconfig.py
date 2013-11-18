# -*- coding: UTF-8 -*-
# Copyright 2013 Red Hat, Inc.
# Part of clufter project
# Licensed under GPLv2 (a copy included | http://gnu.org/licenses/gpl-2.0.txt)

from clufter.filter import XMLFilter
from lxml import etree


@XMLFilter.deco('XML', 'simpleconfig')
def xml2simpleconfig(flt, in_obj):
    for context in etree.iterwalk(in_obj('etree'), events=('start', 'end')):
        pass
    pass
