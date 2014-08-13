#!/usr/bin/env python

import sys
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

import radicale

radicale.config.read("./config")

from radicale.__main__ import run

run()
