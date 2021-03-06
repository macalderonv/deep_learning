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
    #print(mensaje)
    
    #inicialization time and axes
    
    #second sensor
    tiempo_1 = []
    eje_x_1 = []
    eje_y_1 = []
    eje_z_1 = []
    
    #first sensor
    tiempo_2 = []
    eje_x_2 = []
    eje_y_2 = []
    eje_z_2 = []
    
    header = []
    
    #mac identifying which sensor. The file is suppose to have the information 
    #from two different sensor, placed in the same high in the body, e.g., foot (two sensors),
    #, hip(two sensor)
    
    #TODO verify the MAC address for each sensor and the location of the sensors
    
    #if the sensor is in the hip
    if file[-5] == 'C':
        sen_addr_1 = "0014.4F01.0000.76D8" #left-hip
        sen_addr_2 = "0014.4F01.0000.7B06" #right-hip
    #if the sensor is in the foot
    elif file[-5] == "P":
        sen_addr_1 = "0014.4F01.0000.7E23 " #left-foot
        sen_addr_2 = "0014.4F01.0000.7EB9" #rigth-foot
        
    
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
                
                # get values from line corresponding to sensor 1
                if sen_addr_1 == aux_sen_addr:
                    segs= segundos(linea[3:15])
                    tiempo_1.append(segs)
                    eje_x_1.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    eje_y_1.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    eje_z_1.append(linea[linea.find("Z")+2:linea.find("q")-2])
                
                # get values form the line corresponding to sensor 2
                elif  sen_addr_2 == aux_sen_addr: 
                    segs= segundos(linea[3:15])
                    tiempo_2.append(segs)
                    eje_x_2.append(linea[linea.find("X")+2:linea.find("Y")-3])
                    eje_y_2.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                    eje_z_2.append(linea[linea.find("Z")+2:linea.find("q")-2])
                

    #fs = 50 #Hz
    #t = np.arange(0,len(eje_x))/fs
    #plt.figure(figsize=(8,10))
    #plt.plot(t,eje_x)
    #plt.plot(t,eje_y)
    #plt.plot(t,eje_z)
    
    #converting into numpy
    tiempo_1 = np.array(tiempo_1)
    eje_x_1 = np.array(eje_x_1,dtype = 'float')
    eje_y_1 = np.array(eje_y_1,dtype = 'float')
    eje_z_1 = np.array(eje_z_1,dtype = 'float')
    
    tiempo_2 = np.array(tiempo_2)
    eje_x_2 = np.array(eje_x_2,dtype = 'float')
    eje_y_2 = np.array(eje_y_2,dtype = 'float')
    eje_z_2 = np.array(eje_z_2,dtype = 'float')  
    
    
    #Sorting out arrays
    idx_sort_1 = np.argsort(tiempo_1)
    tiempo_1 = tiempo_1[idx_sort_1]
    eje_x_1 = eje_x_1[idx_sort_1]
    eje_y_1 = eje_y_1[idx_sort_1]
    eje_z_1 = eje_z_1[idx_sort_1]
    
    idx_sort_2 = np.argsort(tiempo_2)
    tiempo_2 = tiempo_2[idx_sort_2]
    eje_x_2 = eje_x_2[idx_sort_2]
    eje_y_2 = eje_y_2[idx_sort_2]
    eje_z_2 = eje_z_2[idx_sort_2]
    
    f.close()   
    
    return tiempo_1,eje_x_1,eje_y_1,eje_z_1,tiempo_2,eje_x_2,eje_y_2,eje_z_2

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
        
        if filename[-5] == 'C':
            print("cadera")
            tiempo_ci.append(response[0])
            ejex_ci.append(response[1]) 
            ejey_ci.append(response[2])
            ejez_ci.append(response[3])
            tiempo_cd.append(response[4])
            ejex_cd.append(response[5])
            ejey_cd.append(response[6]) 
            ejez_cd.append(response[7])
        #si es pie
        elif filename[-5] == "P":
            print("pies")
            
            [tiempo_pi,ejex_pi,ejey_pi,ejez_pi,tiempo_pd,ejex_pd,ejey_pd,ejez_pd]= leertxt(filename)
            print("tiempo_pi")
            print(tiempo_pi)
            print("ejex_pi")
            print(ejex_pi)
            print("ejey_pi")
            print(ejey_pi)
            print("ejez_pi")
            print(ejez_pi)
            print("tiempo_pd")
            print(tiempo_pd)
            print("ejex_pd")
            print(ejex_pd)
            print("ejey_pd")
            print(ejey_pd)
            print("ejez_pd")
            print(ejez_pd)
            
        
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
