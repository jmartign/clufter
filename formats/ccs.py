# -*- coding: UTF-8 -*-
# Copyright 2012 Red Hat, Inc.
# Part of clufter project
# Licensed under GPLv2 (a copy included | http://gnu.org/licenses/gpl-2.0.txt)
"""Cluster configuration system (ccs) format"""
__author__ = "Jan Pokorný <jpokorny at redhat dot com>"

from ..format import XML


class ccs(XML):
    """Cman-based cluster stack configuration (cluster.conf)

    Sometimes called Cluster Configuration System (ccs).
    """
    # XML
    root = 'cluster'


class ccsflat(ccs):
    """Cman-based cluster stack configuration (cluster.conf)

    Sometimes (ehm, exclusively by me) called Cluster Configuration System Flat.
    """
    pass
