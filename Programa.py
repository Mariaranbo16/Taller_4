# Importar la biblioteca 
# Hacer un ALIAS para no escribir completo. (np)  ES OPCIONAL

import numpy as np

# Una forma de crear arreglos ndarray es usando una lista 

miLista = [3,5,7,9]
miArreglo = np.array (miLista)

# Atributos de los arreglos 
print (miArreglo.ndim)
print (miArreglo.shape)
print (miArreglo.size)
print (miArreglo.dtype)

# No se puede olvidar poner las llaves en la lista de numpy
miArreglo2 = np.array ([2,6,7,90])
