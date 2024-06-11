# ¿Como leer el contenido de un archivo?
# Funciones integradas métodos:

#read()
#devuelve todo el contenido de un archivo como una cadena que contendra todos los carácteres.

# with open('37_archivos_de_lectura/nuevo_archivo1.txt', 'r') as file:
#     print(file.read(20))
#también se puede pasar como argumento un número .read(20) que será la cantidad de carácteres a leer. 

#--------------------------------------------------------------------------------------

#readline() 
#devuelve una sola linea como una cadena 
# with open('37_archivos_de_lectura/nuevo_archivo1.txt', 'r') as file:
#      print(file.readline(4))
#también se puede pasar como argumento un número .readline(4) que será la cantidad de carácteres a leer en esa primera linea.
#--------------------------------------------------------------------------------------

#readlines()
#lee todo el contenido del archivo y luego lo devuelve en una lista ordenada. Esto me permite
#iterar sobre la lista o elegir lineas especificas basadas en una condición.

# with open('37_archivos_de_lectura/nuevo_archivo1.txt', 'r') as file:
#     print(file.readlines())
    #['Primera linea\n', 'Segunda linea\n', 'Tercera linea\n', 'Cuarta linea\n']

#iterando sobre las lineas del archivo

# with open('37_archivos_de_lectura/nuevo_archivo1.txt', 'r') as file:
#     lines = file.readlines()
#     print(len(lines))

#     for line in lines:
#         print(line)

# 4
# Primera linea

# Segunda linea

# Tercera linea

# Cuarta linea

#--------------------------------------------------------------------------------------

#Paths
#Leyendo archivos desde rutas.

#Absolute
#contienen la etiqueta de unidad
#ejemplo: 
#/usr/local/etc/somefile.txt
# o
#C:\users\system\somefile.txt

#Relative
#normalmente no contiene ninguna referencia al al directorio raíz y, en general, son relativas al
#archivo de llamada. Solo incluye la información que necesita para localizar un archivo en su actual
#directorio de trabajo.
#ejemplo:
#'somefile.txt'
# o
#'./somefile.txt'

#--------------------------------------------------------------------------------------
#COMO LEER ARCHIVOS EN PYTHON
#primera opción

# with open('37_archivos_de_lectura/sample.txt', 'r') as file:
#     print(file.read())

#segunda opción (solo una determinada sección del archivo)
# with open('37_archivos_de_lectura/sample.txt', 'r') as file:
#     print(file.read(44))

#tercera opción (leer la primera linea)
# with open('37_archivos_de_lectura/sample.txt', 'r') as file:
#      print(file.readline())

#cuarta opción 
# with open('37_archivos_de_lectura/sample.txt', 'r') as file:
#     lines = file.readlines()
#     print(len(lines)) 
#     for line in lines:
#         print(line)

# cuando se utiliza with open() y se firma como una variable, ejemplo file
# lo convierte automaticamente en una lista. El código anterior quedaría así:
# with open('37_archivos_de_lectura/sample.txt', 'r') as file:
#     for line in file:
#         print(line)

#--------------------------------------------------------------------------------------
#practicas
#elegir un nombre al azar

import random

f = open('37_archivos_de_lectura/sample1.txt', 'r')
f_content = f.read()
f_content_list = f_content.split('\n',3)
print(f_content_list)

print(random.choice(f_content_list))


