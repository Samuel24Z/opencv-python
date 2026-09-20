# Imagenes digitales
Una imagen digital I es es una representación bidimensional con datos numéricos.

Además, el tamaño de una imagen se determina a partir del ancho M (número de columnas) y la altura N (número de filas) de la matriz de imagen I. 

En procesamiento de imágenes, el sistema de coordenadas es como sigue, la coordenada y se ejecuta de arriba a abajo, la coordenada x de izquierda a derecha y el origen se encuentra en la esquina superior izquierda.

## Imágenes en color
La mayoría de las imágenes en color se basan en los colores primarios rojo, verde y azul (Red, Green, Blue, RGB), generalmente utilizando 8 bits para cada componente de color. En estas imágenes de color, cada píxel requiere 3 × 8 = 24 bits para codificar cada componente y el rango de cada componente de color individual está entre los valores 0, … ,255. En la siguiente imagen se muestra el detalle de las matrices que integran a una imagen digital, cada matriz se llama canal y es una matriz que contiene todos los datos para representar un color de una imagen.

![Imagen digital en RGB](/operaciones_principales/imagenes/Canales_imagen_digital.png)

## Imágenes en escala de grises
Así mismo, existe un tipo de imágenes en escala de grises, en este tipo de imagen los datos consisten en un solo canal que representa la intensidad o el brillo de la imagen. Así mismo, una imagen típica en escala de grises usa 8 bits por píxel y sus valores de intensidad están en el rango 0, … 255, donde el valor 0 representa el brillo mínimo (negro) y 255 el brillo máximo (blanco).

