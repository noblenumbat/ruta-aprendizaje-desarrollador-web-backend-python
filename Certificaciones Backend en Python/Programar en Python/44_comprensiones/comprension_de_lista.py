# Comprensión de la lista: 
# Ex1: Modificando la misma lista: Es una manera de afectar cada elemento, de modificar la lista.

data = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]

data = [x+3 for x in data]

print("Actualizando la lista: ", data)

# ------------------------------------------------------------------------------------------

# Ex2: Creando una diferente lista con valores actualizados
new_data = [x*2 for x in data]
print("Creando una nueva lista: ", new_data)

# ------------------------------------------------------------------------------------------

# Ex3: Con una condición if: Múltiples de cuatro
fourx = [x for x in new_data if x%4 == 0]
print("Divisible por 4: ", fourx)

# ------------------------------------------------------------------------------------------

# Ex4: Alternativamente podemos actualizar la lista con el if condicional tambien

fourxsub = [x-1 for x in new_data if x%4 == 0]
print("Divisible por cuatro menos uno: ", fourxsub)

# Exp5: Using range function:

nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

#----------------------------------
# # List comprehension:
# data = [x+3 for x in data]
# print(data)

#---

# Regular for loop:
# for x in range(len(data)):
#  data[x] = data[x] + 3
#----------------------------------