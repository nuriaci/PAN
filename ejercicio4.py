import random 
import numpy as np
import matplotlib.pyplot as plt

def respuestaAleatorizada (n,p):
    x = np.random.binomial(1, p, n) #IA - chatgpt  
    y = np.zeros(n) #respuesta
    acertar=0
    trampa=0
    opciones = ["cara", "cruz"]
    
    for i in range(0,n): #Implementar mecanismo R.A.
        primera_opcion = random.choice(opciones) 
        if primera_opcion == "cara":
           y[i] = x[i] #dice la verdad
        else: #cruz -> no dice la verdad 
            segunda_opcion = random.choice(opciones)
            if segunda_opcion == "cara":
                y[i] = 1

    for i in range(0,n): #comparar resultados
        if(y[i]==x[i]):
            acertar +=1
        else:
            trampa +=1
            
    acertar = acertar/n
    trampa = trampa/n
    
    return acertar,trampa

def aux(p,y):
    n = 1000
    acertar,trampa =respuestaAleatorizada(n,p)
    
    q = acertar * trampa + (1 - acertar)*(1 - trampa)
    
    if y == 0:
        Estimador_p = 0
    else:
        Estimador_p = (y - 1 + q) / (2 * y - 1)
    
    return Estimador_p


def verificarEmpiricamente():
    #Se realizan 50 simulaciones
    contador = 0
    total_dif = 0
    p = random.random()
    y = random.random()
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