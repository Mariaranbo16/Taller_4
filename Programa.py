# Importar la biblioteca 
import numpy as np

# Usando funciones de "relleno" de arreglos 
miArreglo = np.arange(-10,10)
print (miArreglo.ndim)

miArreglo = miArreglo.reshape((2,10))
print (miArreglo.ndim)
print (miArreglo)

