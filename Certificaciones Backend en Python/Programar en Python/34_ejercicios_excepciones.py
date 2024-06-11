#IndexError
# Starter code

# try:
#     items = [1,2,3,4,5]
#     item = items[6]
#     print(item)

# except:
#     print('El elemento no existe en la lista')


#----------------------------------------------------------------------------------------------
#ZeroDivisionError

# En matemáticas existen reglas sobre dividir por cero. El siguiente código intenta hacerlo y 
# mostrará un ZeroDivisionError. Agregue la gestión de excepciones para devolver 0 en lugar de 
# permitir que se produzca el error.

# Starter code
# def divide_by(a, b):
#     return a / b

# try:
#     ans = divide_by(40, 0)
#     print(ans)
# except ZeroDivisionError as e: # division by zero
#     print(0)
# except Exception as e: # division by zero
#     print(e, 'sigue habiendo algo mal')

#----------------------------------------------------------------------------------------------
#FileNotFoundError

# El código siguiente busca un archivo que no existe. Agregue la gestión de excepciones para detectar 
# este error y devolver el siguiente mensaje "No se pudo encontrar el archivo".

# Starter code
# try:
#     with open('file_does_not_exist.txt', 'r') as file:
#         print(file.read())
# except:
#     print('No se puedo encontrar el archivo')
