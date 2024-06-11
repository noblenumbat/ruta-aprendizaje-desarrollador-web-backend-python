# secuencia
print(1,'a',22.4)

# aritmético 
print(1 + 4)

# concatenating
name = 'Lucy'
print('Hello ' + name)

# print() tiene reservadas palabras clave que se pueden analizar como argumentos adicionales.
# Incluye objetos que son valores impresos en pantalla,
# sep define como se imprimen los objetos o se separan

print('Hola','tu','todo','bien',sep=', ')

# end define lo que se imprime al final. Esto también hace que no haya un salto de linea en el
# próximo print. 

print('hola','tu','todo','bien',end='!')

# Direct formatting. Phyton permite el formato directo dentro de la sentencia print

a = 10
b = 5
ans = a + b 
print ('\nAdding the value of {} and {} = {}'.format(a,b,ans)) # se controla el orden 

# Direct formatting. Ejemplo controlando el orden mendiante el número dentro de las llaves
print("I'd like to be a {0} than the {1}".format('doctor','teacher'))
print("I'd like to be a {1} than the {0}".format('doctor','teacher'))

# input()
num1 = input('Type your first number: ')
num2 = input('Type your second number: ')
result = print(int(num1) + int(num2)) # primero hace la conversión
result = print(int(num1 + num2)) # suponiendo que num1 = 3 y num2 = 3 
                                 # primero resuelve num1 + num2 como string '33'
                                 # luego imprime el '33' como 33 

str1 = input('Please enter your first name:')
str2 = input('Please enter your last name:')
salutation = print('Hello ' + str1 + ' ' + str2 + ' 👋')
salutation = print('Hello {} {}'.format(str1, str2) + ' 👋')
