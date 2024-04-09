# Importar la biblioteca 
import numpy as np

# Usando funciones de "relleno" de arreglos 
miArreglo = np.arange(-10,10)
print (miArreglo.ndim)

miArreglo.reshape((2,10))

miArreglo = np.ones ((5,4))
print (miArreglo)

miArreglo = np.zeros ((4,5))
print (miArreglo)

miArreglo = np.empty ((4,5))
print (miArreglo)
