#Listas
list1 = ['1','2','3','4','5']

print(*list1)
# 1 2 3 4 5

#insert permite agregar un elemento a la lista

list1.insert(len(list1),6)

list1.insert(0,0) #dando la posición del elemento a insertar

#append inserta un elemento al final de la lista
list1.append(10)

#extend inserta varios elementos en una lista
list1.extend([11, 12, 13, 14, 15])

#pop elimina el último elemento de la lista
list1.pop()
#también se especifica el indice del elemento a eliminar
#[0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14]

#despues
# list1.pop(2)
#[0, 1, 3, 4, 5, 6, 10, 11, 12, 13, 14]

#otra manera
del list1[2]

#print(list1)

#for permite acceder a todos los elementos de una lista.

for x in list1:
    print('Value: ', x)




# #print(list1[2])

# list2 = ['A','B','C']


# list3 = ['Hello',1,True,40.22] 

# #listas anidadas

# list4 = [list2, list3]
# #[['A', 'B', 'C'], ['Hello', 1, True, 40.22]]

# list5 = [1, [2,3,4], 5, 6]

# print(list5[0],list5[1])
# #1 [2, 3, 4]