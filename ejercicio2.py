import random 
import numpy as np
import matplotlib.pyplot as plt

#implementa la estrategia de RA de 'dos monedas' descrita anteriormente produciendo un vector con las salidas
def respuestaAleatorizada (n,x):

    y = np.zeros(n)
    
    opciones = ["cara", "cruz"]
    
    for i in range(0,n):
        primera_opcion = random.choice(opciones)
        
        if primera_opcion == "cara":
           y[i] = x[i] #dice la verdad
        else: #cruz -> no dice la verdad 
            segunda_opcion = random.choice(opciones)
            if segunda_opcion == "cara":
                y[i] = 1

    return y

#verificar empiricamente

def verificarEmpiricamente():
    totalprob = 0
    #Se realizan 1000 simulaciones
    for i in range(0,1000):
        n = random.randint(1, 30)
        p = random.random()
        contador = 0
    
        # genera un vector largo con 1's y 0's de manera que la probabilidad de un 1 esté dada por un parámetro p (verdaderos)
        x = np.random.binomial(1, p, n) #IA - chatgpt
        #vector de respuestas aleatorizada RA
        y =respuestaAleatorizada(n,x)
    
        for i in range(0,n):#Comparamos vectores y sumamos las veces que ha acertado 
            if x[i] == y[i]:
                contador +=1
    
        prob = contador/n #calculamos la probabilidad
    
        totalprob += prob
    print(f"La probabilidad promedia tras 1000 simulaciones es de {totalprob/1000 :.2f}")
    
    
        
if __name__ == "__main__":
    verificarEmpiricamente()
            
        