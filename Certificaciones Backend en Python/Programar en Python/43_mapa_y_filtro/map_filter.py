menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    

# map toma todos los objetos en una lista y les aplica una función.
# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)


# filter hace lo mismo, pero toma los resultados y crea un nuevo listado solo con los valores verdaderos.
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

# Nota: map() devuelve todos los elementos de un iterable y filter() devuelve los valores si son Verdaderos.