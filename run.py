#!/usr/bin/env python

import radicale

radicale.config.read("./config")

from radicale.__main__ import run

run()
