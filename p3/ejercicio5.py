import numpy as np
import pandas as pd
import ejercicio1  # Asegúrate de que esta función esté bien implementada

# Parámetros
q = 2**16
delta = 2**10
n = 256
m = 3
p = 3  
alpha_values = np.arange(5e-04, 5e-03, 5e-04)  # Valores de alpha

def descomposition_gadget(c, p):
    base = 2**p
    coeficientes = []

    while c != 0:
        coef = c % base
        # Ajuste de coeficiente a rango [-base/2, base/2 - 1]
        if coef >= (base // 2):
            coef -= base  # Asegurar que esté en [-base/2, base/2 - 1]
        
        coeficientes.append(coef)
        c = (c - coef) // base  # Actualiza c
    return coeficientes

def ejercicio5(alpha, c):
    # Genera el vector secreto s y el vector aleatorio a
    s = np.random.choice([-1, 0, 1], size=n)
    a_p = [np.random.randint(-q // 2, q // 2, size=n) for _ in range(p)]
    

    # Calcula b
    error = ejercicio1.generate_error(1, alpha, q) 
    b = [(np.dot(s, a_p[i]) + delta * m * 2**(p*i) + error) % q for i in range(p)]

    # Generar los coeficientes de la descomposición gadget
    gadgetCoefs = descomposition_gadget(c, p)

    # Generar cifrado
    a_gadget = sum((coef * a_p[i]) for i, coef in enumerate(gadgetCoefs)) % q
    b_gadget = sum((coef * b[i]) for i, coef in enumerate(gadgetCoefs)) % q

    # Descifrar el resultado
    m_hat = np.round((b_gadget - np.dot(s, a_gadget)) % q / delta)

    return m_hat != m * c

if __name__ == "__main__":
    error_counts = []
    for alpha in alpha_values:
        resultado = 0
        for i in range(1000):
            if ejercicio5(alpha, c=10):
                resultado += 1
        error_counts.append(resultado)

    # Crear la tabla de resultados
    for alpha, errores in zip(alpha_values, error_counts):
        print(f"Alpha: {alpha:.4f}, Errores: {errores:.4f}")
