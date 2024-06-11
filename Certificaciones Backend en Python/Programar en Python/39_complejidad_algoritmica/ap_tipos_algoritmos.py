# Escribir código para satisfacer las necesidades la empresa.

# REFACTORIZACIÓN 
# ----------------
# El código tendrá que ir a través de lo que se denomina refactorización.
# Esto significa que reescribe o vuelve a trabajar el código, para que sea más fácil de administrar
# o para que se ejecute de manera más eficiente.

# La refactorización es una pieza estándar del ciclo de desarrollo de software.
# Facilitar la administración del código puede ser sencillo, pero surgen dos cuestiones:
# 1. Hacerlos más rápido ó
# 2. Mejorar su rendimiento

# Para lo anterior el código debe poder ser medido. El código se mide por tiempo y espacio.
# Tiempo: el tiempo se mide por cuanto tarda.
# Espacio: por cuanta memoria utiliza.

# Big O notation
# ---------------
# Tiene diferentes complejidades o categorías que van desde orrible a excelente. Se utiliza para medir
# la eficiencia del algoritmo, en términos de espacio y tiempo.

# Tipos de complejidades del tiempo
# ----------------------------------
# Tiempo constante: este es un algoritmo que siempre se ejecutará bajo el mismo tiempo y espacio, 
# independientemente del tamaño.
# Example:
# Dictionary
# drinks = {1:'coffee', 2:'Tea', 3:'Juice'}
# print(drinks[2])
# Para obtner el valor de un elemento, necesita tener la clave. La clave es un puntero directo al valor
# y no requiere ninguna iteración para encontrarlo. Se considera constante.

# El segundo es un algoritmo de tiempo lineal.
# Esto crecerá según el tamaño de la entrada.
# Example:
# for x in range(1000000):
#     print(x)
# Si tengo una matriz de número de un rango de 100, se ejecutará muy rápido. Pero si se aumenta a 1000000 
# tardará mucho más en completarse. El tamaño de ese código afecta el tiempo de ejecución del código.

# Un algoritmo de tiempo se refiere al tiempo de ejecución de las entradas, frente al número de operaciones.
# Example:
# Algoritmo lineal
# def find_num(num):
#     count = 0
#     for x in range(100):
#         if x == num:
#             print("Total Iterations: " + str(count))
#             return x 
#         count += 1

# find_num(97)
# El código anterior bajo Algoritmo de tiempo (continuar en 2:00)
def find_number_log(target):
    iterations = 0
    x = range(100)
    left = 0
    right = len(x) - 1

    while left <= right:
        iterations += 1
        middle = (left + right) // 2
        isNumber= x[middle]

        if target == isNumber:
            print('Iteractions', iterations)
            return middle
        elif target < isNumber:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(find_number_log(50))
    
# El algoritmo que has proporcionado es una implementación de búsqueda binaria, 
# que es un algoritmo eficiente para encontrar un elemento en una lista ordenada.

#--------------------------------------------------------------------------------
# Quadractic Time
# Se refiere a una operación lineal de cada valor de los datos de entrada al cuadrado.
# Esto suele ser una lista anidada como en este bucle "for" se considera tiempo cuadratico

# for x in range (10):
#     for y in range(10):
#         print(x,y)


