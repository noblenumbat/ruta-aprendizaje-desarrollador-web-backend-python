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


