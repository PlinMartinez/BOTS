# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:14:53 2019

@author: MPAZ

PASO 2

SE CONECTA A BINANCE, TOMA LAS ORDENES DE LOS PARES SELECCIONADOS EN PASO 1
 Y LO EXPORTA CADA 5 MINUTOS EN UN CSV

(DESPUES VENDRA LA LOGICA DE ACCION)

"""


from funciones.panditas import ordenes_binance
from funciones.panditas import ordenar_df1
from datetime import date
from datetime import datetime
import time
import shelve


db=shelve.open('tablas')

pares2=db['pares_vivos']  

pares=[]

for par in pares2:
    duo=par.split('/')
    union=duo[0]+duo[1]
    pares.append(union)


#pares=['ADAUSDT','ATOMBTC']

mega={}


for par in pares:
    
    try:
        
        # df=mega[par]  ¿no seria al reves y al final?
    
        df=ordenes_binance(par)
        df=ordenar_df1(df)
    
        hoy=date.today()
        año,mes,dia=hoy.year,hoy.month,hoy.day
        nombre=str(año)+str(mes)+str(dia)+par+'.csv'
        #ruta='C:\RMB_v2\\ficheros\\'+nombre
        ruta=nombre
        df.to_csv(ruta)
        print ('Grabado fichero '+ruta)
        
        mega[par]=df
    
    except:
        print ('fallo en par' + par)
        



while True:

    for par in pares:
        
        try:
        
            print ('A dormir 30 segundos')
            time.sleep(30)
            print ('Al ataque!!!')
            df=mega[par]
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
            print ('Grabado fichero par'+par+ruta)
        
        except:
            print ('Fallo en el par ' + par )
            
