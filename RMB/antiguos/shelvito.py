# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:24:58 2019

@author: MPAZ
"""

import shelve

obj=shelve.open('shelvetest')
obj['nombre']='Plin Martinez'
obj.close
