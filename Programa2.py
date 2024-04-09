# Importar la biblioteca 
# Hacer un ALIAS para no escribir completo. (np)  ES OPCIONAL

import numpy as np

# Crear arreglos de dos  dimensiones a partir de listas

miLista = [[1,2,3,4],[5,6,7,8],[9,10,11,20]]

miArreglo = np.array(miLista, dtype = int)
print(miArreglo.ndim)
print(miArreglo)
print(miLista)