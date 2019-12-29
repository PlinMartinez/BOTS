# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:30:56 2019

@author: MPAZ

SE CONECTA A BINANCE, TOMA LAS ORDENES DEL PAR ADAETH Y LO EXPORTA CADA 5 
MINUTOS EN UN CSV

(DESPUES VENDRA LA LOGICA DE ACCION)
PASO 1 

"""

from funciones.panditas import ordenes_binance
from funciones.panditas import ordenar_df1
from datetime import date
from datetime import datetime
import time


par='ADAETH'

df=ordenes_binance(par)
df=ordenar_df1(df)

hoy=date.today()
año,mes,dia=hoy.year,hoy.month,hoy.day

nombre=str(año)+str(mes)+str(dia)+par+'.csv'

#ruta='C:\RMB_v2\\ficheros\\'+nombre
ruta=nombre


df.to_csv(ruta)
print ('Grabado fichero '+ruta)

while True:
    
    
    print ('A dormir 30 segundos')
    time.sleep(30)
    print ('Al ataque!!!')
    
    ultima_orden=df['id'].iloc[-1]
    
    # MIRA A VER QUE MOMENTO ES PARA QUITAR LO QUE TENGA MAS DE 24 HORAS
    now=datetime.now()
    timestamp=datetime.timestamp(now)
    timestamp2=round(timestamp*1000,0)
    dia=1000*60*60*24
    solucion=timestamp2-dia
    
    
    df2=ordenes_binance(par)
    df2=ordenar_df1(df2)
    
    df =df[(df['timestamp']>solucion)]
    df2=df2[(df2['id']>ultima_orden)]
    df=df.append(df2)
    
    
    hoy=date.today()
    año,mes,dia=hoy.year,hoy.month,hoy.day
    
    nombre=str(año)+str(mes)+str(dia)+par+'.csv'
    
    #ruta='C:\RMB_v2\\ficheros\\'+nombre
    ruta=nombre
    
    df.to_csv(ruta)
    print(datetime.now())
    print ('Grabado fichero '+ruta)
    



