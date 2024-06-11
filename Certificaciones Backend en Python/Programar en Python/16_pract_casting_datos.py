# Practica casting de datos

print(10 ==10)
# Output: True

print(10 == 10.0)
# Output: True. Es True porque Python convierte el int a float de forma implícita

print(10 + 10.0)
# Output: 20.0. Esta salida me permite concluir que cuando Python ejecuta operaciones con enteros y flotantes, convierte implícitamente el tipo de enteros en un flotante y luego completa la operación.

print(type(10 + 10.0)) 
# Output: <class 'float'>

# Entrada de datos
num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = num1 + num2 

print(ans)

# Output: 99
# Esto pasa porque todo lo que se envia al input() se convierte implícitamente a cadena
# Para poder sumar ambos números hacemos la conversión explicita así:

num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = float(num1) + float(num2) # de esta manera me aseguro de que el programa acepte int e incluso flotantes sin que genere error

print('el resultado de sumar ' , num1 , ' y ' , num2 , 'es igual a : '  , ans)
# Output: el resultado de sumar  9  y  9 es igual a :  18.0

# Otra manera de mostrar el resultado utilizando +  para concatenar y realizando la conversión explícita sería:

num1 = input('Enter the first number: ') # 9
num2 = input('Enter the second number: ') # 9
ans = float(num1) + float(num2) # de esta manera me aseguro de que el programa acepte int e incluso flotantes sin que genere error

print('el resultado de sumar ' + str(num1) + ' y ' + str(num2) + ' es igual a : '  + str(ans))
# Output: el resultado de sumar  9  y  9 es igual a :  18.0