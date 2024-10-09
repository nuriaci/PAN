import random 
import numpy as np
import matplotlib.pyplot as plt

def respuestaAleatorizada (n,p):
    x = np.random.binomial(1, p, n) #IA - chatgpt  
    y = np.zeros(n)
    coincidir=0
    opciones = ["cara", "cruz"]
    
    for i in range(0,n): #Implementar mecanismo R.A.
        primera_opcion = random.choice(opciones) 
        if primera_opcion == "cara":
           y[i] = x[i] 
        else: 
            segunda_opcion = random.choice(opciones)
            if segunda_opcion == "cara":
                y[i] = 1
    
    for i in range(0,n): 
        if(y[i]==x[i]):
            coincidir +=1
            
    coincidir = coincidir/n
    
    q = np.mean(y) 
    
    return q,coincidir

def aux(p):
    n = 1000
    q, coincidir =respuestaAleatorizada(n,p)
    
    if (coincidir==0 or coincidir==0.5):
        estimador_p=0
    else:
        estimador_p = (q - (1 - coincidir)) / (2 * coincidir - 1)
   
    
    return estimador_p


def verificarEmpiricamente():
    #Se realizan 50 simulaciones
    contador = 0
    total_dif = 0
    p = random.random()
    diferencias = []
    
    for i in range(0,50):
        estimador_p = aux(p)
        dif = p - estimador_p
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