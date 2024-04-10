import numpy as np                            # Importar la biblioteca  
import matplotlib.pyplot as plt               # Hacer un ALIAS para no escribir completo.  
def mandelbrot(h, w, maxit=20, r=2):          # Definir la función de matplotlib con tres variables que se van a trabajar
    
    x = np.linspace(-2.5, 1.5, 4*h+1)         # Crea un rango de números entre -2.5 a 1.5 y genera una lista entre ese rango con un espaciado definido por 4*h+1
    y = np.linspace(-1.5, 1.5, 3*w+1)         # Crea un rango de números entre -1.5 a 1.5 y genera una lista entre ese rango con un espaciado definido por 3*w+1
    A, B = np.meshgrid(x, y)                  # Es una asiganción multiple. A y B se asignan a x y 
    C = A + B*1j                              # Se realiza la operación, C es la nueva variable que va a almacenar el resultado de la operación con un numero complejo, en este caso B
    z = np.zeros_like(C)                      # Crea una matriz de ceros almacenada en el tamaño de C
    divtime = maxit + np.zeros(z.shape, dtype=int)      # 

    for i in range(maxit):                      # Se utiliza el ciclo for para recorrer la variable maxit en el rango 20
        z = z**2 + C                            # Ahora z va a ser igual a la matriz elevada al cuadrado y se le suma las coordenadas de la tupla que hicimos en un principio C = A + B*1j
        diverge = abs(z) > r                    # Se declara 
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))