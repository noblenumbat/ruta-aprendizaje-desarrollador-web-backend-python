# Estamos viendo como añadir un módulo que se encuentra fuera de la carpeta de un proyecto

import sys 

# 1. se inserta la ruta en el indice 1 y se pasa al r que es el argumento
sys.path.insert(1, r'/home/jonathan/Documentos/Cursos/Certificaciones Backend en Python/Programar en Python/46_modulos/ruta_ejemplo')

# 2. ahora importo el archivo de prueba
import mod_prueba

print(mod_prueba.names)