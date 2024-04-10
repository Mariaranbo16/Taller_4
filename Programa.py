# Importar la biblioteca 
import numpy as np

a =  np.array ([5,10,15,20,25])
print (a)

b = np.array ([3,4,7,9,56])
print (b)

c = a-b
print (c)

c = a + b
print (c)

c = a * b
print (c)

c = a**b  # Es el elevado
print (c)

c = np.sin (b)
print (c)

c = (b>6)
print (c)

c = a @ b  # Es el producto punto 
print (c)