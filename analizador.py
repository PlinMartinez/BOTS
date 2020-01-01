# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:28:18 2019

@author: MPAZ

ANALIZADOR GENERICO DE FICHEROS CSV CON VENTAS PARA VALORAR COMO GANAR 
AL MERCADO


"""

import pandas as pd

fichero='20191229ADAUSDT.csv'

df=pd.read_csv(fichero)

def ordenar_csv(df):
    del df['Unnamed: 0']
    del df['timestamp']
    df['fecha']=pd.to_datetime(df['fecha'])
    df=df.set_index('fecha')
    ordenes=df['id'].resample('1min').count()
    minimo=df['precio'].resample('1min').min()
    maximo=df['precio'].resample('1min').max()
    media=df['precio'].resample('1min').mean()
    variacion=round((maximo-minimo)/minimo*100,1)
    primero=df['precio'].resample('1min').first()
    ultimo=df['precio'].resample('1min').last()
    series=[ordenes,minimo,maximo,media,variacion,primero,ultimo] 
    df2=pd.DataFrame(series)
    df2=df2.T
    df2.columns=['ordenes','minimo','maximo','media','variacion','primero','ultimo']
    return df2


df=ordenar_csv(df)
df=df.dropna()
df['media2']=df['media'].shift(1)
df['media3']=df['media'].shift(-1)
df=df.dropna()

if df.iloc[0,6] < df.iloc[0,7]:
    print ('bien')

df['max']=0
df['min']=0

for i in range(1,len(df)):
    if df.iloc[i,3] > df.iloc[i,7] and df.iloc[i,3] > df.iloc[i,8]:
        df.iloc[i,9]=df.iloc[i,3]
        print ('maximo')
    if df.iloc[i,3] < df.iloc[i,7] and df.iloc[i,3] < df.iloc[i,8]:
        df.iloc[i,10]=df.iloc[i,3]
        print ('minimo')
        
    
df['mix']=df['min']+df['max']
df2=df[df['mix']>0]

df2['min']=df2['min'].shift(1)

df2=df2[df2['max']>0]

df2['beneficio']=df2['max']-df2['min']
df2['porcentaje']=df2['beneficio']/df2['min']


df2=df2[df2['porcentaje'] > 0.002]


