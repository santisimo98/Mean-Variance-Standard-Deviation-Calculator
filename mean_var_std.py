import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(list).reshape(3, 3)
    
    # Aplanar la matriz para realizar cálculos en una sola dimensión
    flattened = matriz.flatten()

    # Crear un diccionario para almacenar los cálculos
    calculations = {
        'mean': [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), flattened.mean().tolist()],  # Media por columnas, filas y matriz aplanada
        'variance': [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), flattened.var().tolist()],  # Varianza por columnas, filas y matriz aplanada
        'standard deviation': [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), flattened.std().tolist()],  # Desviación estándar por columnas, filas y matriz aplanada
        'max': [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), flattened.max().tolist()],  # Máximo por columnas, filas y matriz aplanada
        'min': [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), flattened.min().tolist()],  # Mínimo por columnas, filas y matriz aplanada
        'sum': [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), flattened.sum().tolist()]  # Suma por columnas, filas y matriz aplanada
    }

    return calculations