# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

"""
Spyder Editor

This is a temporary script file.
"""
eje_x = []
eje_y = []
eje_z = []
tiempo = []







def segundos(hora):
    hh = float(hora[0] + hora[1])
    #print(hh * 3600)
    mm = float(hora[3] + hora[4])
    ss = float(hora[6:])
    #print(ss)
    segundostotales=(hh*3600)+(mm*60)+ss
    return segundostotales

def leertxt(file):
    """
    Funcion que le pasamos un archivo .txt y devuelve ordenados por tiempo 
    eje x,y,z el lado derecho y del lado izquierdo donde 1 es izquierda y 2 es
    derecha. Tambien devuelve el header del file y el tiempo
    
    Parameters
    ----------
    file: str
        fichero que tenemos que procesar para ordenar y sacar los ejes x,y,z 
    de los lados derecho e izquierdo, tiempo y header
    
    Returns
    -------
    tiempo_1, tiempo_2: str
        array np donde estan los tiempo de izquierda y derecha
    eje_x_1,eje_y_1,eje_z_1,eje_x_2,eje_y_2,eje_z_2 : float 
        ejes de tiempo de la izquierda y derecha 
    """
    
    f = open (file,'r')
    #mensaje = f.read()
    
    #inicialization time and axes
    
    #second sensor
    
    header = []
    ejex_cd = []
    ejey_cd = []
    ejez_cd = []
    ejex_ci = []
    ejey_ci = []
    ejez_ci = []
    ejex_pd = []
    ejey_pd = []
    ejez_pd = []
    ejex_pi = []
    ejey_pi = []
    ejez_pi = []
    tiempo_cd = []
    tiempo_ci = []
    tiempo_pd = []
    tiempo_pi = []
    
    #mac identifying which sensor. The file is suppose to have the information 
    #from two different sensor, placed in the same high in the body, e.g., foot (two sensors),
    #, hip(two sensor)
    
    #TODO verify the MAC address for each sensor and the location of the sensors
    
    #if the sensor is in the hip
    if file[-5] == 'C':
        sen_addr_ci = "0014.4F01.0000.76D8" #left-hip
        sen_addr_cd = "0014.4F01.0000.7B06" #right-hip
    #if the sensor is in the foot
    elif file[-5] == "P":
        sen_addr_pi = "0014.4F01.0000.7E23 " #left-foot
        sen_addr_pd = "0014.4F01.0000.7EB9" #rigth-foot
        
    
    with open(file) as archivo:
        #read line by line the file.
        
        #TO_DO: read and save the header information
        
        for linea in archivo:
            #print(linea)
            
            if linea[1] != 't':
                header.append(linea)
            
            if linea[1] == 't':
                
                #find sensor MAC addres in this line
                aux_sen_addr = linea[linea.find("s")+2:linea.find("X")-3]
                print(aux_sen_addr)
                # get values from line corresponding to sensor 1
                if sen_addr_ci == aux_sen_addr:
                    segs= segundos(linea[3:15])
                    tiempo_ci.append(segs)
                    ejex_ci.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    ejey_ci.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    ejex_ci.append(linea[linea.find("Z")+2:linea.find("q")-2])
                # get values form the line corresponding to sensor 2
                elif  sen_addr_cd == aux_sen_addr: 
                    segs= segundos(linea[3:15])
                    tiempo_cd.append(segs)
                    ejex_cd.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    ejey_cd.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    ejez_cd.append(linea[linea.find("Z")+2:linea.find("q")-2])
                # get values from line corresponding to sensor 1
                elif sen_addr_pi == aux_sen_addr:
                    segs= segundos(linea[3:15])
                    tiempo_pi.append(segs)
                    ejex_pi.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    ejey_pi.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    ejex_pi.append(linea[linea.find("Z")+2:linea.find("q")-2])
                # get values form the line corresponding to sensor 2
                elif  sen_addr_pd == aux_sen_addr: 
                    segs= segundos(linea[3:15])
                    tiempo_pd.append(segs)
                    ejex_pd.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    ejey_pd.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    ejez_pd.append(linea[linea.find("Z")+2:linea.find("q")-2])
    #fs = 50 #Hz
    #t = np.arange(0,len(eje_x))/fs
    #plt.figure(figsize=(8,10))
    #plt.plot(t,eje_x)
    #plt.plot(t,eje_y)
    #plt.plot(t,eje_z)
    
    #converting into numpy
    tiempo_ci = np.array(tiempo_ci)
    ejex_ci = np.array(ejex_ci,dtype = 'float')
    ejey_ci = np.array(ejey_ci,dtype = 'float')
    ejez_ci = np.array(ejez_ci,dtype = 'float')
    
    tiempo_cd = np.array(tiempo_cd)
    ejex_cd = np.array(ejex_cd,dtype = 'float')
    ejey_cd = np.array(ejey_cd,dtype = 'float')
    ejez_cd = np.array(ejez_cd,dtype = 'float') 

    tiempo_pi = np.array(tiempo_ci)
    ejex_pi = np.array(ejex_pi,dtype = 'float')
    ejey_pi = np.array(ejey_pi,dtype = 'float')
    ejez_pi = np.array(ejez_pi,dtype = 'float')
    
    tiempo_pd = np.array(tiempo_cd)
    ejex_pd = np.array(ejex_pd,dtype = 'float')
    ejey_pd = np.array(ejey_pd,dtype = 'float')
    ejez_pd = np.array(ejez_pd,dtype = 'float') 
    
    
    #Sorting out arrays
    idx_sort_ci = np.argsort(tiempo_ci)
    tiempo_ci = tiempo_ci[idx_sort_ci]
    ejex_ci = ejex_ci[idx_sort_ci]
    ejey_ci = ejey_ci[idx_sort_ci]
    ejez_ci = ejez_ci[idx_sort_ci]
    
    idx_sort_cd = np.argsort(tiempo_cd)
    tiempo_cd = tiempo_cd[idx_sort_cd]
    ejex_cd = ejex_cd[idx_sort_cd]
    ejey_cd = ejey_cd[idx_sort_cd]
    ejez_cd = ejez_cd[idx_sort_cd]
    
    idx_sort_pi = np.argsort(tiempo_pi)
    tiempo_pi = tiempo_ci[idx_sort_pi]
    ejex_pi = ejex_ci[idx_sort_pi]
    ejey_pi = ejey_ci[idx_sort_pi]
    ejez_pi = ejez_ci[idx_sort_pi]
    
    idx_sort_pd = np.argsort(tiempo_pd)
    tiempo_pd = tiempo_pd[idx_sort_pd]
    ejex_pd = ejex_pd[idx_sort_pd]
    ejey_pd = ejey_pd[idx_sort_pd]
    ejez_pd = ejez_pd[idx_sort_pd]
    
    f.close()   
    
    return tiempo_ci,ejex_ci,ejey_ci,ejez_ci,tiempo_cd,ejex_cd,ejey_cd,ejez_cd,tiempo_pi,ejex_pi,ejey_pi,ejez_pi,tiempo_pd,ejex_pd,ejey_pd,ejez_pd

def procesar_registro(ident):
    """
    Función que procesa una carpeta de id, que corresponde con un experimento completo.
    Asumimos que cada carpeta contiene dos ficheros de texto: uno con la información de la
    cadera y otro con la información de los pies
    
    
    Parameters
    ----------
    ident : str
        Identificador de experimento. Corresponde con una carpeta que tenemos que procesar
        
    Returns
    -------
    expr : dicctionary
        Diccionario que tenga toda la información correspondiente a un experimento.
        Header, y 16 series temporales (tiempo, eje x, eje y, eje z por cada mota).
    """
    #entrat dentro de la carpeat
    import os 
    import glob
    
    #recorrer los ficheros de la carpeta
    for filename in glob.glob('*.txt'):
        print(filename)
        #procesar cada fichero
        #si es cadera
        response = leertxt(filename)
        print(response)
        
        #si es pie
            
        
        
  #  cadera = leertxt(datos_cadera)
  #  pies = leertxt(datos_pies)
    
    
    
    #ordenar por tiempos, para sincronizar inicio y fin de los ficheros.
  #  return cadera, pies     
    
procesar_registro('./999/')
#running
data = leertxt('./999/Acc_Data_2019_02_06_17_56_37_C.txt')

#get sampling frequency

print("Sampling freq sensor 1: ",1/np.mean(np.diff(data[0])))
print("Sampling freq sensor 2: ",1/np.mean(np.diff(data[4])))
   
    
plt.plot(data[0],data[1])
plt.plot(data[4],data[5])

#remove means
plt.figure()
plt.plot(data[0],data[1]-np.mean(data[1]))
plt.plot(data[4],data[5]-np.mean(data[5]))

#TODO get data from both, C and P, and remove the parts, to have time series of
#the same length (front and rear).

    
    #milista = [4,1,8,2,9]
    #print sorted(milista)
    
 #dataset matriz para analizar datos    
