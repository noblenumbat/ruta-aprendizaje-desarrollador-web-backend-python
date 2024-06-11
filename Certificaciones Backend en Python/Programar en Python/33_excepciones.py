#excepciones
#hay 2 clases de error: humanos (error de sintaxis, de tipo de datos, ortográfico), excepciones 
#son errores conocidos que se debe manejar.

#manejo de excepciones: 1) cambiar mensajes de error, 2) envolver el codigo dentro de las 
#sentencias "try" y "except"

#ejemplo
def divide(a,b):
    return a / b

#print(divide(10,2))
#5

#print(divide(10,0))
#ZeroDivisionError: division by zero

#--------------------------------------------------------------------------------------
# F O R M A   S I M P L E

# try:
#     ans = divide(10,0)    
# except:
#     print('Algo esta mal')

#--------------------------------------------------------------------------------------
# E S P E C I F I C A N D O   L A   C L A S E   D E L   E R R O R
# try:
#     ans = divide(10,0)
# except Exception as e: # la clase Exception especifica el error
#     print('Algo esta mal:', e)
#     print(e.__class__) # tipo o clase de error que se ha producido OPCIONAL

#Algo esta mal: division by zero 
#<class 'ZeroDivisionError'>

#--------------------------------------------------------------------------------------
# P E R S O N A L I Z A N D O   E L   M E N S A J E
# try:
#     ans = divide(10,0)
# except ZeroDivisionError as e: #si sabemos la clase de error, este se puede especificar
#     print(e,': No se puede dividir por cero') #y en la salida tambien

#division by zero : No se puede dividir por cero

#---------------------------------------------------------------------------------------
# COMO SE PUEDE MANEJAR MAS DE UNA EXCEPCIÓN 
#Al igual que con cualquier excepción de lenguaje de programación ocurre en Python. Puede 
#manejar más de una excepción encadenando la sentencia "except" al agregar otra sentencia "except".

try:
    ans = divide(10,0)
except ZeroDivisionError as e: #si sabemos la clase de error, este se puede especificar
    print(e,': No se puede dividir por cero') #y en la salida tambien
except Exception as e:
    print(e, 'sigue habiendo un error!')
