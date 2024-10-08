import random 
import numpy as np
import matplotlib.pyplot as plt

def respuestaAleatorizada (n,p,gamma):
    X = np.random.binomial(1, p, n)

    Y = np.zeros(n)
    
    for i in range(n):
        if np.random.rand() < gamma:
            Y[i] = X[i]  # Responde con la verdad
        else:
            Y[i] = 1 if np.random.rand() < 0.5 else 0

    q = np.mean(Y)
    return q

def varianzaEmpirica(n,p, gamma):
    estimaciones = []

    for i in range (5000):
        q = respuestaAleatorizada(n,p,gamma)

        estimador_p = (q - (1 - gamma)) / (2 * gamma - 1)
        estimaciones.append(estimador_p)

    return np.var(estimaciones)

p = int(0.5)
gamma = int(0.75)
n_values = [50,100,375,700,1000,5000,10000,20000,50000]

var_empiricas =  []

for n in n_values:
    var = varianzaEmpirica(n,p,gamma)
    var_empiricas.append(var)

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

            