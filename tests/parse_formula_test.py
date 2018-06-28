#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyparserchemicalformula.parser import parse_molecule


def test_water():
    assert parse_molecule('H2O') == {'H': 2, 'O': 1}


def test_magnesium_hydroxide():
    assert parse_molecule('Mg(OH)2') == {'Mg': 1, 'O': 2, 'H': 2}


def test_fremy_salt():
    assert parse_molecule('K4[ON(SO3)2]2') == {'K': 4, 'O': 14, 'N': 2, 'S': 4}
