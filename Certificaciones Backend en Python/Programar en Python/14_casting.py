# Type casting.  Es el proceso de conversión de un tipo de datos a otro.
# Tipos de conversiones: Implícitas y Explícitas.

# Implícita: la realiza automaticamente el compilador de Python para evitar la perdida de datos.
# Ejemplo: el resultado es un dato float que proviene de dos valores int

num1 = 4
num2 = 3

print(type(num1))
result = num1 / num2 

print(type(result))

# Explícita: exiten diferentes funciones proporcionadas por Python para realizar conversiones.
# str()

print(type(str(num2)))

# int()
print(int(result))

# float()
print(float(num1))

# ord() 
# convierte la cadena que representa un carácter Unicode en un entero que representa el carácter 
# Unicode del carácter
print(ord('3'))
print(ord('d'))
print(ord('D'))

# hex()
print(hex(num1))

# oct()
print(oct(num2))

# oct()
print(tuple('jon')) # Excelente

# set()
print(set('jon')) # Excelente

# list()
print(list('jon')) # Excelente


# ---

# Practica casting de datos

print(10 ==10)
# Output: True

print(10 == 10.0)
# Output: True. Es True porque Python convierte el int a float de forma implícita

print(10 + 10.0)
# Output: 20.0. Esta salida me permite concluir que cuando Python ejecuta 
# operaciones con enteros y flotantes, convierte implícitamente el tipo de enteros 
# en un flotante y luego completa la operación.

print(type(10 + 10.0)) 
# Output: <class 'float'>

# Entrada de datos
num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = num1 + num2 

print(ans)

# Output: 99
# Esto pasa porque todo lo que se envia al input() se convierte implícitamente a 
# cadena 
# Para poder sumar ambos números hacemos la conversión explicita así:

num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = float(num1) + float(num2) # de esta manera me aseguro de que el programa 
# acepte int e incluso flotantes sin que genere error

print('el resultado de sumar ' , num1 , ' y ' , num2 , 'es igual a : '  , ans)
# Output: el resultado de sumar  9  y  9 es igual a :  18.0

# Otra manera de mostrar el resultado utilizando +  para concatenar y realizando 
# la conversión explícita sería:

num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = float(num1) + float(num2) # de esta manera me aseguro de que el programa acepte int # e incluso flotantes sin que genere error

print('el resultado de sumar ' + str(num1) + ' y ' + str(num2) + ' es igual a : '  + str(ans))
# Output: el resultado de sumar  9  y  9 es igual a :  18.0

 