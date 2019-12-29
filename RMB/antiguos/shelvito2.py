# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 06:41:18 2019

@author: MPAZ
"""

import shelve

obj=shelve.open('variables')

df=obj['df']
df2=obj['df2']

df=df.append(df2)

