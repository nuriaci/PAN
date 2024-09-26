import random 
import numpy as np
import matplotlib.pyplot as plt



def aux(p,y):
    n = 1000
    acertar = np.random.binomial(1, p, n) #p
    acertar = np.mean(acertar)
    
    trampa =  np.random.binomial(1, y, n) #y
    trampa = np.mean(trampa)
    
    q = acertar * trampa + (1 - acertar)*(1 - trampa)
    
    if y == 0:
        Estimador_p = 0
    else:
        Estimador_p = (y - 1 + q) / (2 * y - 1)
    
    return Estimador_p


def verificarEmpiricamente():
    #Se realizan 50 simulaciones
    p = random.random()
    y = random.random()
    contador = 0
    total_dif = 0
    
    for i in range(0,50):
        Estimador_p = aux(p,y)
        dif = p - Estimador_p
        total_dif += dif
        contador +=1
        print(f"{contador} : {dif}\n")

    
    print(f"Promedio: {total_dif/50}")

if __name__ == "__main__":
    verificarEmpiricamente()