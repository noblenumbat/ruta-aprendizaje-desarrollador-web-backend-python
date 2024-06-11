# No lo suma para remediarlo añadir \ al final de la linea 2
x = 1
+ 2

# Esta manera es valida
def say_hello(): 
    print("Hello there!")
print(say_hello())

# Esta manera tambien es valida
def say_hello(): print("Hello there!")
print(say_hello())

# Error
def say_hello():
print("Hello there!")

# Error
    def say_hello():
print("Hello there!")