# Importar la biblioteca 
import numpy as np

a =  np.array ([[5,10,15,20,25],[3,6,4,8,12]])

print (a)
print(a.sum())
print(a.sum(axis=1))  # Suma los elementos de cada eje
print(a.min(axis=0))  # Muestra los minimos de los ejes verticales
print(np.sqrt(a))     # Muestra la raiz de los números

print (a.size)
print (a.shape)