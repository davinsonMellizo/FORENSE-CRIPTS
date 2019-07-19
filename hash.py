#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


ComandoHash="md5sum menu.py"
print("HASH:")
os.system(ComandoHash)

ComandoGrep='grep -r python /root/Documents/FORENSE/PARCIAL3'
print(ComandoGrep)
os.system(ComandoGrep)