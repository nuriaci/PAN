import numpy as np
import matplotlib.pyplot as plt
import ejercicio2
import pandas as pd

delta = 2**10
n = 256
q = 2**16

def ejercicio3(alpha):
    # Messages to be encrypted
    m1 = 10
    m2 = 8

    # Generate secret vector s and random vectors a1 and a2 within the modular range
    s = np.random.choice([-1, 0, 1], size=n)
    a1 = np.random.randint(-q // 2, (q // 2) -1, size=n)
    a2 = np.random.randint(-q // 2, (q // 2) - 1, size=n)

    # Encrypt messages with Gaussian error
    b1 = (np.dot(s, a1) + delta * m1 + ejercicio2.generate_error(1, alpha, q)) % q
    b2 = (np.dot(s, a2) + delta * m2 + ejercicio2.generate_error(1, alpha, q)) % q

    # Homomorphic addition of ciphertexts
    aCombinado = (a1 + a2) % q
    bCombinado = (b1 + b2) % q

    # Decrypt the combined ciphertext, with rounding and modular adjustment
    m_hat = np.round(((bCombinado - np.dot(s, aCombinado)) % q) / delta)
    
    # Return True if there's a decryption error
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

    # Display results in a table
    for alpha, errores in zip(Conjuntoalpha, error_counts):
        print(f"Alpha: {alpha:.4f}, Errores: {errores}")
