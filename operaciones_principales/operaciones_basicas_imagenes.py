import cv2 as cv
import numpy as np
import os

""" 
Si abrimos la terminal y presionamos "code ." en la raíz del proyecto 
y usamos chdir(), entonces el programa de python se va comenzar a
mover a partir de esa raíz que se eligió, sin embargo si se usa 
"code ." desde un nivel arriba o uno abajo entonces ese directorio
se va usar como el inicio para que el programa python se pueda 
mover hacia otras rutas.
En este caso nos movemos un nivel arriba con chdir('..')
"""
os.chdir("..") 
rutaEjemplos = os.getcwd() + "\\img\\" # Devolvemos la ruta actual (un nivel átras)
img = cv.imread(rutaEjemplos + "messi5.jpg")
escalaGrises = cv.imread(rutaEjemplos + "messi5.jpg", cv.IMREAD_GRAYSCALE)

# Acceso a los pixeles de una imagen RGB por sus coordenadas [y, x]
pixelRGB = img[100, 200]
print("El valor del pixel (x=200, y=100) es:" + str(pixelRGB))
# print(pixelRGB[2]*0.299 + pixelRGB[1]*0.587 + pixelRGB[0]*0.114)
# pixel[2] -> R
# pixel[1] -> G
# pixel[0] -> B

# Acceso a un solo pixel de una imagen RGB
azul = img[100, 200, 0] # [y, x, canal]
verde = img[100, 200, 1]
rojo = img[100, 200, 2]
# Cálculo de un pixel en escala de grises por medio de sus componentes RGB
print("El valor del pixel (200, 100) en grises (calculado) es: " + str(0.299 * rojo + 0.587 * verde + 0.114*azul))

pixel = escalaGrises[100, 200]
print("El valor del pixel (200, 100) dado por opencv es: " + str(pixel))

# Obtenemos las dimensiones de la imagen con shape, es decir, obtenemos filas, columnas y canales
print("Las dimensiones de la imagen RGB son: ")
print("Filas:" + str(img.shape[0]))
print("Columnas:" + str(img.shape[1]))
print("Canales: " + str(img.shape[2]))
print("En resumen tenmos estas dimensiones: " + str(img.shape))

# El número total de pixeles es: No filas * No columnas * No de canales
print("El número total de pixeles es: " + str(img.size))

# Obtenemos el tipo de datos de la imagen
print("El tipo de datos de la imagen es: " + str(img.dtype))

# Accedemos a una región de interés de la imagen
pelota = img[280:340, 330:390] # [y1:y2, x1:x2]
# Colocamos una región extraída (la pelota) en otra región de interés
img[273:333, 100:160] = pelota

# cv.imshow("Región de intéres", img)
# cv.waitKey(0)

# El acceso a una región de interés se puede observar en el siguiente ejemplo
imagen2 = np.zeros((8, 8), dtype=np.uint8)
imagen2[1:4, 2:6] = 1
# print("\nAcceso a región de interés:")
# print(imagen2)

# Separamos los canales de una imagen
blue = img[:,:,0]
green = img[:,:,1]
red = img[:,:,2]
# De nuevo mezclamos los canales con la función merge()
cv.imshow("BGR", cv.merge((blue, green, red)))
cv.waitKey(0)
"""
También es posible separar los canales por medio de la función split()
pero es una operación costosa en términos de tiempo, por tanto es 
preferible usar la indexación de numpy
"""
