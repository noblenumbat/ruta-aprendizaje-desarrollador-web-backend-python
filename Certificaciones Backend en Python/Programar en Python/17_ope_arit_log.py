# Casting o conversión de datos
si_no = 'No'
print(bool(si_no))

name = "Prueba"

print(len(name))

# Operadores aritméticos

# + Addition
add = 6 + 2
print(add)

# - Subtraction
subs = 6 - 2
print(subs)

# / Division
div = 6 / 2
print(type(div))

# * Multiplication
mul = 6 * 2
print(type(mul))

# Operadores lógicos

# and valida que ambas condiciones sean verdaderas. 
#Ejemplo: 

print(add==8 and subs==4)

# or valida que al menos una condición sea verdadera. 
#Ejemplo: 

print(div>2 or div<3)

# not retorna falso si el resultado es verdadero. 
#Ejemplo: 

print(not(mul<13))

a = False
b = False

if not(a) or not(b) :
    print('All true')

# la doble diagonal "//" se conoce como operador de división entera. 
# Esto significa que el resultado de la división se redondea hacia abajo 
# al número entero más cercano. En el caso específico de la línea de código 
# que proporcionaste, la expresión "(left + right) // 2" calcula el promedio 
# entero de los valores de "left" y "right"

# Ejemplo

dividendo = 7
divisor =3
ans1 = dividendo / divisor
ans2 = dividendo // divisor
print(round(ans1,2)) #2.33
print(round(ans2,2)) #2