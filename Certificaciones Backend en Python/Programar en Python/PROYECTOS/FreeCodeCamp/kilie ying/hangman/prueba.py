palabra = 'jonathan'

letras_usadas = {'j', 'n'} # conjunto de letras

# comprensión de lista
palabra_lista = [letra if letra in letras_usadas else '-' for letra in palabra] # Es un bucle que recorre cada letra de la cadena palabra, tomando una letra a la vez.

print(palabra_lista) # la variable palabra pasa a ser una lista

# Salida:
['j', '-', 'n', '-', '-', '-', '-', 'n']


for letra in palabra:
    print(letra)