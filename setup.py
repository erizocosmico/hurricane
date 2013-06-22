#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from distutils.core import setup
from hurricane import __version__, __doc__

setup(
    name = "hurricane",
    version = __version__,
    description = "Hurricane is an attempt to make Tornado more friendly for API developers.",
    long_description = __doc__,
    author = "José Miguel Molina",
    author_email = "rd4091@gmail.com",
    py_modules = ['hurricane'],
    url = 'https://github.com/mvader/hurricane',
    classifiers = [],
)