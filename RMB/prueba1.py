# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:44:52 2019

@author: MPAZ
"""

import shelve

db=shelve.open('tablas') 
pares_buenos=db['pares_vivos']

par=pares_buenos[0]

bueno=par.split('/')

	
bueno2=bueno[0]+bueno[1]


pares_lisos=[]

for par in pares_buenos:
    duo=par.split('/')
    union=duo[0]+duo[1]
    pares_lisos.append(union)
