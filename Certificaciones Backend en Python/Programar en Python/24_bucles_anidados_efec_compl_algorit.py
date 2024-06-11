# Bucles anidados: se pueden utilizar para resolver problemas más complejos
# Por ejemplo, el bucle "for" anidado se escribe con sangría dentro del bucle exterior.

#outer loop
# for x in range(10):
#     print('x',x)
#     #inner loop
#     for y in range(5): # por cada vuelta de x se ejecutan todas las vueltas de y
#         print('y',y)

# BUCLES ANIDADOS PARA ITERAR MAS DE DOS LISTAS
# ---------------------------------------------------------------------------------------
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8,9]

# count = 0
# #outer loop
# for x in list1:         # 9 TIMES
#     count +=1
#     #inner loop
#     for y in list2:     # 81 TIMES
#         count += 1

# print(count)

# Other example:

#outer loop
# for i in range(10):
#     #inner loop
#     for j in range(10):
#         print(0, end=" ")
#     print() # OJO CON LA INDENTACION

#output:
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 0 

# PONIENDO UNA MARCA DE TIEMPO
# -----------------------------------------

import time
start_time = time.time()
count = 0
#outer loop
for i in range(100):
    #inner loop
    for j in range(100):
        print(0, end = " ")
        count +=1
    print()
    print('linea: ',count) # OJO CON LA INDENTACION

print(round((time.time() - start_time), 2))