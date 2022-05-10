#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""The moo script."""

import sys
from . import moo

if __name__ == "__main__":
    print(moo(*sys.argv[1:] or ["Hello"]))
