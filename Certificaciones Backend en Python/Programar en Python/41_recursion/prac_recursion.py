# Encontrar el factorial de un número:
# El factorial de un entero positivo n, el factorial de n o n factorial se define en 
# principio como el producto de todos los números enteros positivos desde 1 hasta n.

# Solución iterativa

# def find_factorial_by_looping(n):
#     if n<0:
#         return 0
#     else:
#         factorial = 1
#         for i in range(1,n+1): # el primer argumento (1) es el inicio, el segundo argumento n+1 el valor final, pero no incluye el valor final en si mismo.
#             factorial = factorial * i
#         return factorial

# print(find_factorial_by_looping(5))
# Output:
# 120

# Solución recursiva
def find_factorial_by_r(n):
    if n == 1:
        return 1
    else: 
        return n * find_factorial_by_r(n-1)

print(find_factorial_by_r(5))
        
# Aquí está el proceso paso a paso de cómo se calcula el factorial utilizando este código:

#     Llamada inicial: find_factorial_by_r(5)
#     La condición n == 1 no se cumple, por lo que se ejecuta el bloque else.
#     Se devuelve n * find_factorial_by_r(n-1), que es 5 * find_factorial_by_r(4).
#     Llamada recursiva: find_factorial_by_r(4)
#     La condición n == 1 no se cumple, por lo que se ejecuta el bloque else.
#     Se devuelve n * find_factorial_by_r(n-1), que es 4 * find_factorial_by_r(3).
#     Llamada recursiva: find_factorial_by_r(3)
#     La condición n == 1 no se cumple, por lo que se ejecuta el bloque else.
#     Se devuelve n * find_factorial_by_r(n-1), que es 3 * find_factorial_by_r(2).
#     Llamada recursiva: find_factorial_by_r(2)
#     La condición n == 1 no se cumple, por lo que se ejecuta el bloque else.
#     Se devuelve n * find_factorial_by_r(n-1), que es 2 * find_factorial_by_r(1).
#     Llamada recursiva: find_factorial_by_r(1)
#     La condición n == 1 se cumple, por lo que se devuelve 1.
#     El resultado final es 5 * 4 * 3 * 2 * 1, que es igual a 120.

# Entonces, el código está correctamente implementado y devuelve 1 cuando n tiene un valor de 1.

# cuando se realiza una llamada recursiva, los valores de n se guardan en una pila de llamadas. Cada vez que se realiza una llamada recursiva, se agrega un nuevo marco de pila a la parte superior de la pila. Este marco de pila contiene los valores de las variables locales de la función en ese momento.

# En el caso del cálculo del factorial utilizando recursión, cada llamada recursiva crea un nuevo marco de pila con su propio valor de n. A medida que las llamadas recursivas se van resolviendo, los marcos de pila se van eliminando de la pila en orden inverso, lo que se conoce como "desapilamiento" o "desenrollado de la pila".

# En el ejemplo que proporcionaste, cuando se llama a find_factorial_by_r(5), se crean los siguientes marcos de pila:

#     find_factorial_by_r(5)
#     find_factorial_by_r(4)
#     find_factorial_by_r(3)
#     find_factorial_by_r(2)
#     find_factorial_by_r(1)

# Luego, a medida que las llamadas recursivas se resuelven, los marcos de pila se eliminan en orden inverso:

#     find_factorial_by_r(1) devuelve 1.
#     find_factorial_by_r(2) multiplica 2 por el resultado de la llamada anterior y devuelve 2.
#     find_factorial_by_r(3) multiplica 3 por el resultado de la llamada anterior y devuelve 6.
#     find_factorial_by_r(4) multiplica 4 por el resultado de la llamada anterior y devuelve 24.
#     find_factorial_by_r(5) multiplica 5 por el resultado de la llamada anterior y devuelve 120.

# En resumen, los valores de n se guardan en una pila de llamadas durante la recursión y se desapilan en orden inverso a medida que las llamadas recursivas se resuelven.

