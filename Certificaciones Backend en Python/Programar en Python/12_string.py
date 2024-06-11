a = 'This is a sigle line. '

b = 'This is a first line, and ' \
    'this is a second line. ' \
    'With this third line we a multi line.'

print(len(a))

print(b)

# Now I'm concatenating the variables a and b, lets watch!

print('Watch the follow contatenate: ' + a + b)

# How can I access to certains characters of this string, for example:

print(b[3] + a[4] + a[5])

print('The spaces also count!')

bill = 4.99
print(type(bill))

# Question

age = input('Ingrese su edad por favor: ') # This is the input

print('Thank you, your age ' +  age + ' is registred.')

# Make a sum please

print('Please sum two numbers')

num1 = int(input('Type the first number: ')) # Es importante especificar el tipo de dato
                                             # en el input para que el interprete tome
                                             # el dato como un número y no con un string

num2 = int(input('Type the second number: '))
result = num1 + num2

# En esta linea estoy convirtiendo un int a float
print('Well done, the result is:', float(result)) # El operador + no es permitido para mostrar 
                                           # una salida str con un int, en su lugar 
                                           # utilizamos una coma ','

