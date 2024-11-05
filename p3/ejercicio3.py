import numpy as np
import matplotlib.pyplot as plt
import ejercicio1
import pandas as pd

# Parámetros 
delta = 2**10
n = 256
q = 2**16

def ejercicio3(alpha):
    # Mensajes - cifrar
    m1 = 10
    m2 = 8

    # Genera el vector secreto s y los vectores aleatorios a1 y a2 
    s = np.random.choice([-1, 0, 1], size=n)
    a1 = np.random.randint(-q // 2, (q // 2) -1, size=n)
    a2 = np.random.randint(-q // 2, (q // 2) - 1, size=n)

    # Cifra los mensajes con error Gaussiano - chatgpt
    b1 = (np.dot(s, a1) + delta * m1 + ejercicio1.generate_error(1, alpha, q)) % q
    b2 = (np.dot(s, a2) + delta * m2 + ejercicio1.generate_error(1, alpha, q)) % q

    # Suma homomórfica de los cifrados
    aCombinado = (a1 + a2) % q
    bCombinado = (b1 + b2) % q

    # Descifra el cifrado combinado
    m_hat = np.round(((bCombinado - np.dot(s, aCombinado)) % q) / delta)
    
    # Devuelve True si hay un error de descifrado
    return m_hat != (m1 + m2)

if __name__ == "__main__":
    Conjuntoalpha = np.arange(5e-04, 5e-03, 5e-04)

    error_counts = []
    for alpha in Conjuntoalpha:
        resultado = 0
        for _ in range(1000):
            if ejercicio3(alpha):
                resultado += 1
        error_counts.append(resultado)

     # Muestra los resultados en forma de tabla
    for alpha, errores in zip(Conjuntoalpha, error_counts):
      print(f"Alpha: {alpha:.4f}, Errores: {errores}")
