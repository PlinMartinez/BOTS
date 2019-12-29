# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 07:08:16 2019

@author: MPAZ

SE CONECTA A BINANCE CADA 5 MINUTOS Y TOMA LAS ULTIMAS 1000 ORDENES

CADA DIA GENERA UN NUEVO ARCHIVO CSV

"""

from funciones.panditas import ordenes_binance
from funciones.panditas import ordenar_df1
import time

par='ADAETH'

df=ordenes_binance(par)
df=ordenar_df1(df)

# CADA 5 MINUTOS EXPORTAR FICHERO CSV

from datetime import date

hoy=date.today()
año,mes,dia=hoy.year,hoy.month,hoy.day

nombre=str(año)+str(mes)+str(dia)+par+'.csv'

ruta='C:\RMB_v2\\ficheros\\'+nombre

df.to_csv(ruta)

primera_orden=df['id'].iloc[0]
ultima_orden=df['id'].iloc[-1]

inicio=df['fecha'].iloc[0]
dia_inicio=inicio.day


print ('A dormir 30 segundos')
time.sleep(30)
print ('Al ataque!!!')

df2=ordenes_binance(par)
df2=ordenar_df1(df2)


import shelve

with shelve.open('variables') as db:
    db['df2'] = df
    








