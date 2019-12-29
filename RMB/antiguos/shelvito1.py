# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:36:54 2019

@author: MPAZ
"""

import shelve
import pandas as pd
from datetime import datetime
import gc

with shelve.open('variables') as db:
    df=db['df']
    df2=db['df2']

fin1=df['id'].iloc[-1]
fin2=df2['id'].iloc[-1]
inicio1=df['id'].iloc[0]
inicio2=df2['id'].iloc[0]

print(inicio2-fin1)

if inicio2-fin1 > 0 :
    print('se han perdido ordenes')
    
df3=df2[(df2['id']>9880110)]
prueba=df2.fecha

print (df.dtypes)


a=df3['fecha'].iloc[0]
print(a.hour)
'''
def saca_hora(ts):
    return ts.hour

df3['hora']=df3['fecha'].apply(saca_hora)
'''
df3['hora2']=df3['fecha'].apply(lambda x:x.hour)

df3=df3[(df3['hora2']>19)]
inicio=df3['timestamp'].iloc[0]

now=datetime.now()
timestamp=datetime.timestamp(now)
timestamp2=round(timestamp*1000)

dia=1000*60*60*24
solucion=timestamp2-inicio
solucion2=solucion/dia

ayer=timestamp2-dia


df3=df3[(df3['timestamp']>ayer)]

del [df3]
del [df2]
print (df)

