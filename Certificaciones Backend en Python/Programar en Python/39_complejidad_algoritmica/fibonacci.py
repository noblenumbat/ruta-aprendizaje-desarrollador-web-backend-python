# Manera iterativa
def fibonacci(n):
    a = 0
    b = 1

    for k in range(n):
        c = a + b
        a = b 
        b = c 

    return b

for x in range(3):
    print(fibonacci(x))

# n = 5 
# a = 0     
# b = 1 ************
# c = 1
# a = 1
# b = 1 

# n = 4 
# a = 1     
# b = 1 ************
# c = 2
# a = 1
# b = 2 

# n = 3 
# a = 1     
# b = 2 ************
# c = 3
# a = 2
# b = 3 

# Salida:
# 1
# 1
# 2

# -------------------------------

# Manera recursiva
# def fibonacci_r(n):
#     if n <= 1: #punto de corte
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
 
# for k in range(20):
#     print(fibonacci_r(k))