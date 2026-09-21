import cv2 as cv
import os

os.chdir("..")
os.chdir("..")
rutaEjemplos = os.getcwd() + "\\img\\"
img = cv.imread(rutaEjemplos + "messi5.jpg")
img2 = img
img3 = img.copy()

cv.circle(img, (200, 200), 30, (0, 255, 0), 5)

"""
Debido a que img2 solo es una referencia en memoria de img, entonces
cada vez que modifiquemos algo en img, también se va modificar en
img2, para evitar todo esto tenemos que usar la función copy() de 
opencv y con esto podremos crear una verdadera copia de la imagen
original
"""

cv.imshow("Referencia afectada", img2)
cv.imshow("Copia sin afectar", img3)

cv.waitKey(0)
cv.destroyAllWindows()
