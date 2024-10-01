import random 
import numpy as np
import matplotlib.pyplot as plt



def aux(p,y):
    n = 1000
    trampa = np.zeros(n)
    acertar = np.random.binomial(1, p, n) #p
    
    for i in range(0,n):
        if acertar[i] == 0:
            trampa[i] = 1
        else:
            trampa[i] = 0
    
    acertar = np.mean(acertar)
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
    diferencias = [] 
    
    for i in range(0,50):
        Estimador_p = aux(p,y)
        dif = p - Estimador_p
        diferencias.append(dif) 
        total_dif += dif
        contador +=1
        print(f"{contador} : {dif}\n")

    
    print(f"Promedio: {total_dif/50}")
    
    # Graficar las diferencias - chatGPT
    plt.figure(figsize=(10, 5))
    plt.plot(diferencias, marker='o', linestyle='-', color='b', label='Diferencias entre p y Estimador_p')
    plt.axhline(0, color='r', linestyle='--', label='Cero')
    plt.title('Diferencias entre p y Estimador_p en 50 Simulaciones')
    plt.xlabel('Simulación')
    plt.ylabel('Diferencia (p - Estimador_p)')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    verificarEmpiricamente()