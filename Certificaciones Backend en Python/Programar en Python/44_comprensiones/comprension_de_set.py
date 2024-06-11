""" Comprensión de set

La comprensión del conjunto se ocupa del tipo de datos del conjunto y es muy similar a la comprensión de la lista. 
La única diferencia clave es el uso de llaves para los conjuntos en lugar de corchetes como en las listas. 
Por ejemplo: """

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)
# output
# {10, 11, 13, 15, 17, 18, 19}