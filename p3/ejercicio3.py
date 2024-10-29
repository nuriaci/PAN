import numpy as np
import matplotlib.pyplot as plt
import random
import ejercicio1 

delta = 2**10
n = 256
q = pow(2, 16)

def ejercicio3():
    # Mensajes cifrados
    m1= 10
    m2 = 8
    # Genera el vector secreto s y el vector aleatorio a1 y a2
    s = np.random.choice([-1, 0, 1], size = n)
    a1 = np.random.randint(-q/2,(q/2) -1, size=n)
    a2 = np.random.randint(-q/2,(q/2) -1, size=n)
    # Calcula b usando s^T * a y el error escalar
    b1 = np.dot(s, a1) + delta * m1 + ejercicio1.generate_error(1, alpha, q)
    b2 = np.dot(s, a2) + delta * m2 + ejercicio1.generate_error(1, alpha, q)
    
    #Generar cifrado
    
    #Descifrar el resultado
    
 
    
if __name__ == "__main__":
    alpha =  np.arange(5e-04,5e-03,5e-04)
    for i in range(1000):
        ejercicio3()