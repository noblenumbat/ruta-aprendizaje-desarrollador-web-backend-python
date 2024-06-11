""" Comprensión del generador

Las comprensiones de generadores también son muy similares a las listas, solo que utilizan corchetes curvos en lugar de cuadrados. 
También son más eficientes en memoria que las comprensiones de listas. Por ejemplo: """

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)

print(gen_obj)
# <generator object <genexpr> at 0x78f31a934a00>

print(type(gen_obj))
# <class 'generator'>

for items in gen_obj:
    print(items, end = " ")

# output:
# 2 3 5 7 11 13 17 19 23 29 31

""" En el código anterior, creé un objeto generador del generador de clases en lugar de una lista. No se puede acceder directamente a 
los elementos en este objeto iterador y se necesita la ayuda de un bucle "for ". Itero sobre estos elementos y los imprimo. """

"""  Si deseo acceder a un elemento específico en Python utilizando el bucle "for", puedo hacerlo utilizando
la función enumerate() """

data1 = [2,3,5,7,11,13,17,19,23,29,31]

for index, item in enumerate(data1):
    if index == 4:
        print(item)


