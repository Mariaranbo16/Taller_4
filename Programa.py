# Importar la biblioteca 
import numpy as np

a =  np.array ([7.83445,5.63423,3.443242])

print (a.round())  # Me redondea todos los datos 
print (a.round(decimals=2))   #Redondea segun la cantidad de elementos que hay indicados

print (np.ceil(a))   # Redondea al siguiente entero
print (np.floor(a))  # Redodndea al numero anterior




