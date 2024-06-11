# Ejemplo de recursión: Torre de Hanoi

## Objetivo y reglas del rompecabezas

El objetivo es mover n número de discos de una torre a otra siguiendo un conjunto de reglas. Estas reglas son las siguientes: 

* Solo se puede mover un disco por vez 

* Sólo se puede mover el disco superior de cualquiera de las torres 

* Los discos más grandes no se pueden colocar sobre los discos más pequeños

![](/41_recursion/hanoi.png)

Arriba se ofrece una imagen de las fases inicial y final del rompecabezas. 

En el escenario óptimo de resolución del rompecabezas, el total de movimientos será de 2^n - 1, donde n es el número de discos que hay que mover.

Ahora examinemos cómo puede escribir el código en Python mediante los principios de recursión que ha aprendido.

## Explicación [*Ver algoritmo*](/41_recursion/rec_torre_hanoi.py "ejemplo hanoi")

Si puede imaginar los discos en cuestión como se muestran en la imagen, puede comprender cómo el código distribuye correctamente los tres discos de la torre A a la C, siguiendo las reglas esperadas. 

Observe cómo el disco variable toma inicialmente el número de discos como la entrada y luego se lee o se entiende como el número de discos en cuestión dentro del código.

En el bloque de código, la primera sección es la condición base que se aplica al utilizar el disco 1. Una vez que se ejecutó, vuelve al resto del flujo de ejecución fuera de la condición "if".

Los discos restantes se mueven pasando los valores de origen a ayudante con el destino como ayudante. El disco restante se mueve de origen a destino. Los discos n-1 restantes del ayudante se mueven del ayudante al destino con origen como ayudante.

En la última sección, el código del controlador toma la entrada del número de discos que quiero mover. De acuerdo con eso, paso los valores de A, B y C como los nombres de las torres y doy la llamada a la función.

Notará que llevó 2^3 - 1 = 7 pasos para completar la transferencia, lo que cumple mis expectativas.

La Torre de Hanoi y la recursión, en general, pueden ser confusas, incluso para un ávido programador de Python. Por eso, la mejor manera de entender la recursión es mediante la inserción de los valores y la ejecución de un código seco utilizando un lápiz y papel para ver cómo cambian los valores y qué función se llama en el código en qué momento.
