import random 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def bd_aleatoria(n):
    bd = pd.DataFrame()
    bd["Nombre"] = np.random.randint(0, n, n) #chatgpt
    bd["Edad"] = np.random.randint(0, 126, n)
    bd["SB1"] = np.random.binomial(1, 0.5, n) 
    bd["SB2"] = np.random.binomial(1, 0.5, n) 
    
    return bd

if __name__ == "__main__":
    n = 10
    bd_aleatoria(n)
            