import cv2 as cv
import numpy as np
import os

os.chdir("..")
rutaEjemplos = os.getcwd() + "\\img\\"
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
print("El valor del pixel (200, 100) en grises (calculado) es: " + str(0.299 * rojo + 0.587 * verde + 0.114*azul))

pixel = escalaGrises[100, 200]
print("El valor del pixel (200, 100) dado por opencv es: " + str(pixel))
