import numpy as np
import matplotlib.pyplot as plt
import ejercicio1 
import pandas as pd

delta = 2**10
n = 256
q = 2**16


def ejercicio3(alpha):
    # Mensajes cifrados
    m1= 10
    m2 = 8
    # Genera el vector secreto s y el vector aleatorio a1 y a2
    s = np.random.choice([-1, 0, 1], size = n)
    a1 = np.random.randint(-q // 2, (q // 2) - 1, size=n)
    a2 = np.random.randint(-q // 2, (q // 2) - 1, size=n)
    # Calcula b usando s^T * a y el error escalar
    b1 = (np.dot(s, a1) + delta * m1 + ejercicio1.generate_error(1, alpha, q)[0]) % q
    b2 = (np.dot(s, a2) + delta * m2 + ejercicio1.generate_error(1, alpha, q)[0]) % q
    
    #Generar cifrado
    aCombinado = (a1 + a2) % q
    bCombinado = (b1 + b2) % q

    #Generar cifrado & Descifrar el resultado
    m_hat = np.round((bCombinado - np.dot(s, aCombinado)) / delta)
    
    # Incrementa el contador si hay un error en el descifrado 
    #if m_hat != (m1 + m2): 
      #  resultado += 1
        
    return m_hat != (m1 + m2)

if __name__ == "__main__":
    Conjuntoalpha =  np.arange(5e-04,5e-03,5e-04)

    error_counts = []
    for alpha in Conjuntoalpha:
        resultado = 0
        for i in range(1000):
            if ejercicio3(alpha):
                resultado += 1
        error_counts.append(resultado)

    # Crear la tabla de resultados
    for alpha, errores in zip(Conjuntoalpha, error_counts):
        print(f"Alpha: {alpha:.4f}, Errores: {errores:.4f}")