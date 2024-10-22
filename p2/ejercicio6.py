import ejercicio5
import random 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def generar_bd(n):
    return ejercicio5.bd_aleatoria(n)

def q1(bd, epsilon):
    n = len(bd["Edad"])
    mediaEdades = np.mean(bd["Edad"])
    sensibilidad = 125/n
    ruido = np.random.laplace(loc = 0,scale=sensibilidad/epsilon)
    print (ruido)
    mediaDP = mediaEdades + ruido
    print("Media: ", mediaEdades)
    print("Media privada:", mediaDP)
    
    return mediaEdades,mediaDP
    
def q2(bd, epsilon):
    n = len(bd["Edad"])
    if(n%2==0):
        n += 1 
    medianaEdades = np.median(bd["Edad"])
    sensibilidad = 125
    ruido = np.random.laplace(loc = 0,scale=sensibilidad/epsilon)
    medianaDP = medianaEdades + ruido
    print("Mediana: ", medianaEdades)
    print("Mediana privada:", medianaDP)
    
    return medianaEdades, medianaDP

def q3(bd,epsilon):
    g1 = bd["SB1"].sum()#chatGPT
    g2 = bd["SB2"].sum()
    
    if g1 + g2 == len(bd):
       sensibilidad = 0
    else: 
        sensibilidad = 2
        
    ruido_g1 = np.random.laplace(loc = 0,scale=sensibilidad/epsilon)
    ruido_g2 = np.random.laplace(loc = 0,scale=sensibilidad/epsilon)
   
    G1 = g1 + ruido_g1
    G2 = g2 + ruido_g2
    
    print("Número de 1s en SB1 - privado:",G1)
    print("Número de 1s en SB2 - privado:",G2)
    
    return g1,g2,G1,G2

def q4(bd,epsilon):
    histograma = np.histogram(bd["Edad"],bins=range(127))[0]#chatGPT
    
    sensibilidad = 2
    ruido_hist = np.random.laplace(loc = 0,scale=sensibilidad/epsilon,size=histograma.shape)
    
    histFinal = histograma + ruido_hist

    print("Histograma:",histFinal)
    
    return histograma, histFinal
  


if __name__ == "__main__":
    print("Práctica #2: Mecanismo Laplaciano\n")
    n = int(input("\nIntroduce el valor de n:"))
    epsilon = float(input("\nIntroduce el valor de epsilon:"))
    bd = generar_bd(n)
    
    print(bd)
    
    print("\nEjercicio1")
    q1(bd,epsilon)
    
    print("\nEjercicio2")
    q2(bd,epsilon)
    
    print("\nEjercicio3")
    q3(bd,epsilon)
    
    print("\nEjercicio4")
    q4(bd,epsilon)