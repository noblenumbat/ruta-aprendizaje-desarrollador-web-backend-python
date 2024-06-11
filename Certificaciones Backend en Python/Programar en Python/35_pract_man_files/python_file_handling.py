# file = open('35_pract_man_files/test.txt', mode = 'r')

#para leer el archivo se debe agregar una función "readline" o "readlines"

#METODOS
#readline lee 1 linea
#readlines lee todas las lineas



# data = file.readlines()

# print(data)

# file.close()



# --------------------------------------------------------------------------

#with open es mejor en el manejo de excepciones y cerrara el archivo por mi
with open('35_pract_man_files/test.txt', mode = 'r') as file:
    data = file.readline()

    print(data)
