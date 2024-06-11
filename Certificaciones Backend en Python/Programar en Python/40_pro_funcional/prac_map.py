numbers = [1, 2, 3, 4, 5, 6]

def cubo(x):
    return x ** 3

ans_cubos = map(cubo, numbers)

list() # función que permite convertir el objeto map() en una lista.
print(list(ans_cubos))
# Output
# [1, 8, 27, 64, 125, 216]