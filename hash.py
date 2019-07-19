#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
ComandoDDZERO="md5sum menu.py"
md5=os.system(ComandoDDZERO)
print(md5)
def esterilizar():	
	ComandoDDZERO="md5sum "
	md5=os.system(ComandoDDZERO)
	print(md5)