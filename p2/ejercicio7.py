import ejercicio5
import random 
import ejercicio6
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def nrmsd (vectorVerdaderos,vectorErrores):
    return np.sqrt(np.mean(np.square(vectorErrores))) / np.mean(vectorVerdaderos) #chatgpt


def q7(n,epsilon):
 for i in n:
    results_verdaderos = {
        i:{
            "Q1": [0] * i,  
            "Q2": [0] * i,  
            "Q3": {"g1":[0] * i, "g2":[0] * i},  
            "Q4": [0] * i   
        }
    }   
    results_privados = {
         i:{
            "Q1": [0] * i,  
            "Q2": [0] * i,  
            "Q3": {"g1":[0] * i, "g2":[0] * i},  
            "Q4": [0] * i  
        } 
    }
    results_NRMSD = {
        i:{ 
            "Q1": [0] * i,  
            "Q2": [0] * i,  
            "Q3": {"g1":[0] * i, "g2":[0] * i},    
            "Q4": [0] * i  
        } 
    }
    for m in range(101):
        bd = ejercicio5.bd_aleatoria(i)
 
        results_verdaderos[i]["Q1"][m-1],results_privados[i]["Q1"][m-1] = ejercicio6.q1(bd,epsilon)
        results_verdaderos[i]["Q2"][m-1],results_privados[i]["Q2"][m-1]= ejercicio6.q2(bd,epsilon)
        results_verdaderos[i]["Q3"]["g1"][m-1],  results_verdaderos[i]["Q3"]["g2"][m-1],results_privados[i]["Q3"]["g1"][m-1], results_privados[i]["Q3"]["g2"][m-1] = ejercicio6.q3(bd,epsilon)
        results_verdaderos[i]["Q4"][m-1],results_privados[i]["Q4"][m-1]= ejercicio6.q4(bd,epsilon)
        
        #NRMSD
        results_NRMSD[i]["Q1"][m-1] = nrmsd(results_verdaderos[i]["Q1"][m-1],results_privados[i]["Q1"][m-1])
        results_NRMSD[i]["Q2"][m-1] = nrmsd(results_verdaderos[i]["Q2"][m-1],results_privados[i]["Q2"][m-1])
        results_NRMSD[i]["Q3"]["g1"][m-1] = nrmsd(results_verdaderos[i]["Q3"]["g1"][m-1],results_privados[i]["Q3"]["g1"][m-1])
        results_NRMSD[i]["Q3"]["g2"][m-1] = nrmsd(results_verdaderos[i]["Q3"]["g2"][m-1],results_privados[i]["Q3"]["g2"][m-1])
        results_NRMSD[i]["Q4"][m-1] = nrmsd(results_verdaderos[i]["Q4"][m-1],results_privados[i]["Q4"][m-1])

 # Dibujo de NRMSD -chatgpt
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.plot(results_NRMSD[i]["Q1"], label='NRMSD Q1', color='b')
    plt.title(f'NRMSD Q1 for size {i}')
    plt.xlabel('Experimentos')
    plt.ylabel('NRMSD')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(results_NRMSD[i]["Q2"], label='NRMSD Q2', color='g')
    plt.title(f'NRMSD Q2 for size {i}')
    plt.xlabel('Experimentos')
    plt.ylabel('NRMSD')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(results_NRMSD[i]["Q3"]["g1"], label='NRMSD Q3 g1', color='r')
    plt.plot(results_NRMSD[i]["Q3"]["g2"], label='NRMSD Q3 g2', color='m')
    plt.title(f'NRMSD Q3 for size {i}')
    plt.xlabel('Experimentos')
    plt.ylabel('NRMSD')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(results_NRMSD[i]["Q4"], label='NRMSD Q4', color='c')
    plt.title(f'NRMSD Q4 for size {i}')
    plt.xlabel('Experimentos')
    plt.ylabel('NRMSD')
    plt.legend()

    plt.tight_layout()
    plt.show()  


if __name__ == "__main__":
    n = [101,1001,10001]
    epsilon = float(input("\nIntroduce el valor de epsilon:"))
    q7(n,epsilon)