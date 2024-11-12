import numpy as np
import matplotlib.pyplot as plt
import ejercicio1 
import pandas as pd

# Parámetros
q = 2**16
delta = 2**10
n = 256
c = 10
m = 3
alpha_values = np.arange(5e-04,5e-03,5e-04) # Valores de alpha

def ejercicio4(alpha):
    # Genera el vector secreto s y el vector aleatorio a
    s = np.random.choice([-1, 0, 1], size = n)
    a = np.random.randint(-q // 2, (q // 2) - 1, size=n)
    
    # Calcula b
    b = (np.dot(s, a) + delta * m + ejercicio1.generate_error(1, alpha, q)[0]) % q

    #Generar cifrado
    a_prima =  (c * a) % q
    b_prima = (c * b) % q
    
    #Descifrar el resultado
    m_hat = np.round((b_prima - np.dot(s,a_prima)) % q / delta)
         
    return m_hat != m * c

if __name__ == "__main__":
    Conjuntoalpha =  np.arange(5e-04,5e-03,5e-04)

    error_counts = []
    for alpha in Conjuntoalpha:
        resultado = 0
        for i in range(1000):
            if ejercicio4(alpha):
                resultado += 1
        error_counts.append(resultado)

    # Crear la tabla de resultados
    for alpha, errores in zip(Conjuntoalpha, error_counts):
        print(f"Alpha: {alpha:.4f}, Errores: {errores:.4f}")