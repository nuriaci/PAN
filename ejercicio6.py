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


def varianzaEmpirica(n,p):
    estimaciones = []

    for i in range (5000):
        q, coincidir = respuestaAleatorizada(n,p)
        
        if (coincidir==0 or coincidir==0.5):
            estimador_p=0
        else:
            estimador_p = (q - (1 - coincidir)) / (2 * coincidir - 1)
   
        estimaciones.append(estimador_p)

    return np.var(estimaciones)

p = 0.5
n_values = [50,100,200,500,600,1000]
var_empiricas =  []

for n in n_values:
    var = varianzaEmpirica(n,p)
    var_empiricas.append(var)

# Graficar las diferencias - chatGPT
plt.figure(figsize=(10, 6))
plt.plot(n_values, var_empiricas, marker='o', linestyle='-', color='b')
plt.xscale('log')
plt.yscale('log')
plt.title('Varianza Empírica de $\\hat{p}$ frente a Diferentes Valores de n')
plt.xlabel('Número de Estudiantes (n)')
plt.ylabel('Varianza Empírica')
plt.grid()
plt.show()

for n, var_empirical in zip(n_values, var_empiricas):
    print(f"n = {n}, Varianza Empírica = {var_empirical:.6f}")

            