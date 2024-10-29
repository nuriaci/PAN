import random 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_error(m, alpha,q):
    desviacion = alpha * q
    muestras = np.random.normal(0, desviacion, m) #chatgpt
    muestrasRedondeadas= np.round(muestras) 
    resultado = muestrasRedondeadas % q 
    muestras_final = np.where(resultado >= q / 2, resultado - q, resultado)#chatgpt
    return muestras_final


if __name__ == "__main__":
    m = 1000
    q= 100 
    ConjuntoAlpha = [0.01,0.1,1]
    for i in ConjuntoAlpha:
        generate_error(m, i,q)
    
    # Graficamos el histograma para cada valor de alpha
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for i, alpha in enumerate(ConjuntoAlpha):
        errores = generate_error(m, alpha, q)
        axes[i].hist(errores, bins=range(-q // 2, q // 2), edgecolor='black', align='mid')
        axes[i].set_title(f"Histograma de errores con α = {alpha}")
        axes[i].set_xlabel("Valor de error mod q")
        axes[i].set_ylabel("Frecuencia")
    
    plt.tight_layout()
    plt.show()
            