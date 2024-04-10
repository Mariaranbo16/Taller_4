# Importar la biblioteca 
import numpy as np

a =  np.array ([[5,10,15,20,25],[3,6,4,8,12]])
b =  np.array ([[1,2,3,4,5],[6,7,8,9,10]])

print (a)
print (b)

# Se puede usar de las dos maneras, sin embargo luego de un tiempo genera algunas incosistencias
c = np.add (a,b)
c = a + b
print (c)

