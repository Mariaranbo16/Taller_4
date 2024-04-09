# Importar la biblioteca 
import numpy as np

# Usando funciones de "relleno" de arreglos 
miArreglo = np.linspace (0,100,100)
miArreglo = miArreglo.reshape(10,10)
print (miArreglo)
print (miArreglo.ndim)
print (miArreglo.size)
print (miArreglo.shape)
