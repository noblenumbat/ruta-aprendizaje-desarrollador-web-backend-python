# ------------------------------- COMPRESION LIST ---------------------------------
""" 
familia = ['Jonathan', 'Climaco', 'Romero']

fullname = [nombre + ' ' + 'Castillo' for nombre in familia]

print(f"Estos son los nombres con apellidos: {fullname}")

contiene_a = [nombre for nombre in familia if 'm' in nombre]

print(contiene_a)


# Otra forma de imprimir
for nombre in contiene_a:
    print(nombre) 

"""

# ---------------------------------COMPRESION GENERATOR -----------------------------
 
data = [2,3,5,7,11,13,17,19,23,29,31]

gen_obj = (x for x in data)

print(gen_obj)

print(type(gen_obj))

for item in gen_obj:
    print(item, end = " ") 



print("\n")


for index, item in enumerate(data):
    if index == 5:
        print(item)

# ---------------------------------COMPRESION SET -----------------------------

cualquier_cosa = {cosa for cosa in range(30,41) if cosa not in [31,33]}

print(cualquier_cosa)

# ---------------------------------COMPRESION DICCIONARIO ---------------------

usando_rango = {x:'a' for x in range(10)}

print (usando_rango)


# Ejemplo con una lista:
months = ["Jan", "Feb", "Mar", "Apr", "May", "JUne", "July", "Sept", "Oct", "NOv", "Dec"]

number = [1,2,3,4,5,6,7,8,9,10,11,12]

divididos_en_dos = {x:x/2 for x in number}

print(f"Todos los elementos de la lista number divididos por 2: {divididos_en_dos}")


# Ejemplo con dos listas:
numeros_de_meses = {key:value for (key,value) in zip(number,months)}

print(numeros_de_meses)