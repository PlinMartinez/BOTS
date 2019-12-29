# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 05:37:18 2019

@author: MPAZ
"""

from datetime import datetime, timedelta


'''

EJEMPLO CREAR UNA LISTA CON DATETIMES CON RANGO CREADO

def datetime_rango(inicio, fin, delta):
    actual  = inicio
    while actual < fin:
        yield actual
        actual += delta

dts=[dt.strftime('%Y-%m-%d T%H:%M Z') for dt in
     datetime_rango(datetime(2016,9,1,7),datetime(2016,9,1,9+12),
     timedelta(minutes=15))]
    
print (dts)

'''