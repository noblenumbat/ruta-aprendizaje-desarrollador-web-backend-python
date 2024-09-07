import random

def f():
    return random.randint(0,5)

f_iter = iter(f, 3)

while True:
    print(next(f_iter)) # esto imprime un número aleatorio entre 0 y 5, si el número random es un 3 se genera una excepción


# Sin sentinela  u objeto callable

# a = [2, 4, 6, 8]
# a_iter = iter(a)
# print(a_iter)

# print(next(a_iter)) # 2
# print(next(a_iter)) # 4
# print(next(a_iter)) # 6
# print(next(a_iter)) # 8
# print(next(a_iter)) # Traceback (most recent call last)