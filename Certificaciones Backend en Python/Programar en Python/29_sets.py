#set es una colección de elementos sin duplicados, pero también es una colección de elementos si alterar
#set_a = {1, 2, 3, 4 ,5, 5}

# ----------------------------------------

#métodos

#.add() añade un nuevo elemento

#set_a.add(6)

# .remove() elimina un elemento

#set_a.remove(5)

# .discard(2) hace lo mismo que remove

#set_a.discard(2)

#print(set_a)

# -----------------------------------------
#OPERACIONES ENTRE CONJUNTOS

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

#.union() permite fusionar dos conjuntos o sets

#print(set_a.union(set_b))

#| lo mismo que union.()
#print(set_a | set_b) 

#{1, 2, 3, 4, 5, 6, 7, 8} se omiten valores duplicados

# ---

#.intersection()  retorna los elementos duplicados 

#print(set_a.intersection(set_b)) 
#{4, 5}

#& lo mismo que intersection.()
#print(set_a & set_b)

# ---

#.difference() da como resultado elementos del primer set que no estan en el segundo

#print(set_a.difference(set_b))

#{1, 2, 3}

#- lo mismo que difference()

#print(set_a - set_b)

#{1, 2, 3}

# ---
#symmetric_difference retorna elementos no repetidos del primer conjunto respecto al segundo conjunto

#print(set_a.symmetric_difference(set_b))

#{1, 2, 3, 6, 7, 8}

# ^ mismo que symmetric_difference

print(set_a ^ set_b)

#{1, 2, 3, 6, 7, 8}