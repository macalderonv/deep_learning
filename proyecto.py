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
tiempo_pi = []


def segundos(hora):
    hh = float(hora[0] + hora[1])
    #print(hh * 3600)
    mm = float(hora[3] + hora[4])
    ss = float(hora[6:])
    print(ss)
    segundostotales=(hh*3600)+(mm*60)+ss
    return segundostotales

def leertxt():
    f = open ('Acc_Data_2018_10_19_12_04_19_P.txt','r')
    mensaje = f.read()
    #print(mensaje)
    
    
    with open('Acc_Data_2018_10_19_12_04_19_P.txt') as archivo:
        
        for linea in archivo:
            #print(linea)
            if linea[1] == 't':
                #print('Tiempo:' + linea[3:15])
                segs= segundos(linea[3:15])
                tiempo.append(segs)
                
                
                #print('Dispositivo: ' + linea[34:38])
                #eje_x.append(linea[linea.find("X")+2:linea.find("Y")-3])
                #eje_y.append(linea[linea.find("Y")+2:linea.find("Z")-3])
                #eje_z.append(linea[linea.find("Z")+2:linea.find("q")-2])
            #print('--------------------------------------------------------------')
    print(tiempo)
    sorted(tiempo)
    print('--------------------------------------------------------------')
    print(tiempo)
    #print(len(eje_x))
    #print(len(eje_y))
    #fs = 50 #Hz
    #t = np.arange(0,len(eje_x))/fs
    #plt.figure(figsize=(8,10))
    #plt.plot(t,eje_x)
    #plt.plot(t,eje_y)
    #plt.plot(t,eje_z)
    
    f.close()   


def main():
    leertxt()
    
    #milista = [4,1,8,2,9]
    #print sorted(milista)
    
    
main()