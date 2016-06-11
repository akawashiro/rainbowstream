# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os


def get_realname():
    with open(os.path.expanduser('~')+"/.rainbow_realname.json") as f:
        d = json.load(f, "utf-8")
    return d

if __name__ == '__main__':
    print get_realname()
