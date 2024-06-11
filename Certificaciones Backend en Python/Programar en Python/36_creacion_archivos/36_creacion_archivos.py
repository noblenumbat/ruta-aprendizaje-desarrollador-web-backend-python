# with open('36_creacion_archivos/nuevo_archivo.txt', 'w') as file:
#     #file.write("Este es la segunda linea del archivo creado")
#     file.writelines(["Tercera linea", "\nCuarta linea", "\nQuinta linea"]) #lineas separadas por comas dentro de una lista

# Nota: el modo 'w' sobreescribe el contenido del archivo

# ---------------------------------------------------------------------------------------------------

# with open('36_creacion_archivos/nuevo_archivo.txt', 'a') as file:
#     file.writelines(["\nPrimera linea", "\nSegunda linea", "\nTercera linea", "\nCuarta linea", "\nQuinta linea"])

# Nota: el modo 'a' permite anexar contenido al archivo

# ---------------------------------------------------------------------------------------------------

# 👀 tener en cuenta la necesidad de tratar con excepciones 

# try:
#     with open('36_creacio_archivos/nuevo_archivo.txt', 'a') as file:
#         file.writelines(["\nPrimera linea", "\nSegunda linea", "\nTercera linea", "\nCuarta linea", "\nQuinta linea"])
# except FileNotFoundError as e:
#         print('ERROR',e)