# -*- coding: UTF-8 -*-
# Copyright 2014 Red Hat, Inc.
# Part of clufter project
# Licensed under GPLv2+ (a copy included | http://gnu.org/licenses/gpl-2.0.txt)
"""Testing utils module"""
__author__ = "Jan Pokorný <jpokorny @at@ Red Hat .dot. com>"

from os.path import join, dirname as d; execfile(join(d(d((__file__))), '_go'))


from unittest import TestCase

from .utils import func_defaults_varnames


class FuncDefaultsVarnames(TestCase):
    """Test utils.func_defaults_varnames"""
    def _fnc(a, bar="ni"):
        z = 42  # previously errorneously included into varnames
        pass

    def _gen(a, bar="ni"):
        yield

    def test_std_func(self):
        defaults, varnames = func_defaults_varnames(self._fnc)
        self.assertTrue('a' in varnames)
        self.assertTrue('bar' in varnames)
        self.assertTrue(defaults['bar'] == "ni")
        self.assertEqual(len(varnames), 2)

    def test_std_func_skip(self):
        defaults, varnames = func_defaults_varnames(self._fnc, skip=1)
        self.assertTrue("ni" in defaults.values())
        self.assertTrue('bar' in varnames)
        self.assertEqual(len(varnames), 1)

    def test_generator(self):
        _, varnames = func_defaults_varnames(self._gen)
        self.assertEqual(len(varnames), 2)


from os.path import join, dirname as d; execfile(join(d(d(__file__)), '_gone'))
