import numpy as np
import pandas as pd

# Parámetros
q = 2**16
delta = 2**10
n = 256
alpha_values =  np.arange(5e-04,5e-03,5e-04)  # Valores de alpha

# Función para generar el error escalar
def generate_error(m ,alpha, q):
    desviacion = alpha * q
    # Genera un solo valor de error con desviación estándar alpha * q
    muestra = np.random.normal(0, desviacion, m)
    muestra_redondeada = np.round(muestra) % q  # Redondea y aplica módulo q
    # Ajuste para centrar en el rango [-q/2, q/2 - 1]
    return (muestra_redondeada + q // 2) % q - q // 2

# Lista para almacenar los resultados de cada alpha
error_counts = []

for alpha in alpha_values:
    error_count = 0
    for i in range(1000):
        # Genera el vector secreto s y el vector aleatorio a
        s = np.random.choice([-1, 0, 1], size=n)
        a = np.random.randint(-q // 2, q // 2, size=n)
        
        # Mensaje y cifrado
        m = 10
        # Calcula b usando s^T * a y el error escalar
        b = np.dot(s, a) + delta * m + generate_error(1, alpha, q)
        
        # Descifrado
        m_hat = np.round((b - np.dot(s, a)) / delta)
        
        # Incrementa el contador si hay un error en el descifrado
        if m_hat != m:
            error_count += 1

    # Guarda el contador de errores para el valor actual de alpha
    error_counts.append({"Alpha": alpha, "Contador de errores": error_count})

# Crear la tabla de resultados
df = pd.DataFrame(error_counts)
print(df)
