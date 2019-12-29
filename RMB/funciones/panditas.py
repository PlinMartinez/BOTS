# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:49:38 2019

@author: MPAZ
"""

import requests
import pandas as pd

def ordenes_binance(par):
    ''' EXTRAE DE BINANCE LAS ULTIMAS 1000 ORDENES DE 1 PAR'''
    url_binance='https://api.binance.com/api/v1/'
    url=url_binance+'trades?symbol={}&limit=1000'.format(par)
    datos=requests.get(url).json()
    df=pd.DataFrame(datos)
    return df

def ordenar_df1(df):
    
    ''' TOMA LAS ORDENES DE BINANCE Y LAS AGRUPA ORDENADAMENTE'''
    df.drop(['isBuyerMaker','isBestMatch'],axis='columns',inplace=True) #BORRA COLUMNAS
    df.columns=['id','precio','cant','coste','timestamp']# ORDENA COLUMNAS
    df['fecha']=pd.to_datetime(df['timestamp'],unit='ms') 
    columnas2=['timestamp','fecha','id','precio','cant','coste']
    df=df[columnas2]
    df['precio']=df['precio'].astype(float) #ASIGNA FORMATOS A COLUMNAS
    df['cant']=df['cant'].astype(float)
    df['coste']=df['coste'].astype(float)
    return df

def ordenar_df2(df):

    '''AGRUPAR POR MINUTOS EL DATAFRAME , SACAR MIN Y MAX'''
    df=df.set_index('fecha')
    ordenes=df['id'].resample('1min').count()
    minimo=df['precio'].resample('1min').min()
    maximo=df['precio'].resample('1min').max()
    media=df['precio'].resample('1min').mean()
    variacion=round((maximo-minimo)/minimo*100,1)
    ultimo=df['precio'].resample('1min').last()
    series=[ordenes,minimo,maximo,media,variacion,ultimo]    
    df2=pd.DataFrame(series)
    df2=df2.T
    df2.columns=['ordenes','minimo','maximo','media','variacion','ultimo']
    return df2

def ordenar_csv(df):
    '''TOMA UN FICHERO CSV CON LAS ORDENES DEL DIA Y LO PASA AGRUPA
    EN PERIODOS DE 1 MINUTO SACANDO OHLCV'''
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

def ordenar_csv_15min(df):
    '''TOMA EL FICHERO CSV 20191217ADABTC Y LO AGRUPA EN PERIODOS
    DE 15 MINUTOS SACANDO OHLCV'''
    #del df['Unnamed: 0']
    #del df['timestamp']
    df['fecha']=pd.to_datetime(df['fecha'])
    df=df.set_index('fecha')
    ordenes=df['id'].resample('15min').count()
    minimo=df['precio'].resample('15min').min()
    maximo=df['precio'].resample('15min').max()
    media=df['precio'].resample('15min').mean()
    variacion=round((maximo-minimo)/minimo*100,1)
    primero=df['precio'].resample('15min').first()
    ultimo=df['precio'].resample('15min').last()
    series=[ordenes,minimo,maximo,media,variacion,primero,ultimo] 
    df2=pd.DataFrame(series)
    df2=df2.T
    df2.columns=['ordenes','minimo','maximo','media','variacion','primero','ultimo']
    return df2



