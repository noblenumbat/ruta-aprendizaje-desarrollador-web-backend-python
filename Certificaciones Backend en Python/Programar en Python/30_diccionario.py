#diccionarios  Es similar a un diccionario real. En un diccionario normal, para buscar una palabra se busca
#por la primera letra y luego se usa el sistema de orden alfabético para encontrar su ubicación.
#del mismo modo los diccionarios en Python se optimizan para recuperar valores.
#los diccionarios acceden a los valores basandonse en claves y no en la posición del índice.
#son más rápidos y flexibles en su funcionamiento.

#se asigna una clave a un valor especifico, se denomina par clave valor.
#Key : Value

#Beneficios: mucho más rápido de usar que las listas tradicionales.
#para buscar un elemento en una lista, necesita continuar revisando la lista hasta que localice el elemento.
#pero en un diccionario Python, puede ir directamente al elemento que necesita mediante su clave.

#Key:
#---

#En un diccionario las claves y los valores se pueden modificar o actualizar despues de su creación.

#Value
#-----

#por ejemplo puede declarar un número 1 como clave,

#1:Coffee

#y Coffee es el elemento, y a continuación cambiarlo  por cualquier otro número o elemento bebida.

# ----------------------------------------------------------------------------------------------------
#ACCEDER 
#¿Cómo funciona? ¿Cómo acceder o localizar el elemento que necesita dentro de un diccionario Python con el uso de las claves?

#Ejemplo: acceder al elemento Coffee dentro del diccionario Python.

#declaro el diccionario
#sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}

#print(sample_dict[1]) #el [1] es la clave NO un indice
#Coffe

# ----------------------------------------------------------------------------------------------------
#ACTUALIZAR ELEMENTO
#actualizar un diccionario reemplazando un elemento por otro. Solo necesito usar la clave para referenciarla
#mientras uso el operador de asignación "es igual a" para asignar el valor.

#Ejemplo: 
#sample_dict = {1: 'Coffe', 2: 'Tea', 3: 'Juice'}

#sample_dict[2] = 'Avena'

#print(sample_dict)
#{1: 'Coffe', 2: 'Avena', 3: 'Juice'}
 
# ----------------------------------------------------------------------------------------------------
#ELIMINAR ELEMENTO
#sample_dict = {1: 'Coffe', 2: 'Tea', 3: 'Juice'}

#del sample_dict[2]

#print(sample_dict)
#{1: 'Coffe', 3: 'Juice'}

# ----------------------------------------------------------------------------------------------------
#METODOS PARA ITERAR SOBRE UN DICCIONARIO

#Standard método estandar de iteración

#Items() la función de elementos

#Values() función de valores

my_d = {1: 'Test', 'Name': 'Jon'}
#print(type(my_d))
#<class 'dict'>

#print(my_d)
#print(my_d[1])
#print(my_d['Name'])

# ---
#AGREGAR UN VALOR
my_d[2] = 'Test 2' 
#print(my_d)
#{1: 'Test', 'Name': 'Jon', 2: 'Test 2'}

#ACTUALIZAR UN VALOR
my_d['Name'] = 'Clara'
#print(my_d)
#{1: 'Test', 'Name': 'Clara', 2: 'Test 2'}

#UN DICCIONARIO NO PERMITE CLAVES DUPLICADAS, DE EXISTIR TOMA EL VALOR DE LA ULTIMA CLAVE

my_another_d = {'first_name': 'Jhensy', 'last_name': 'Urrego', 'phone_number': '32080*****', 'last_name': 'Asprilla'}
#print(my_another_d)
#{'first_name': 'Jhensy', 'last_name': 'Asprilla', 'phone_number': '32080*****'}

# ----------------------------------------------------------------------------------------------------
print(my_d)
#{1: 'Test', 'Name': 'Clara', 2: 'Test 2'}

#IMPRIMIR CLAVES
#puedo usar for x para imprimir la clave
for x in my_d:
    print(x)

#IMPRIMIR CLAVE VALOR. Se utiliza el metodo items()
for key, value in my_d.items():
    print(str(key) + " : " + value)
