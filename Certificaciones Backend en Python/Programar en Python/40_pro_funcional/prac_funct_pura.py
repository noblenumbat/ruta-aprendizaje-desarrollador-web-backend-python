# Pure function or not?

# ------------------------------------------------------------
# global scope
# global_list = [1, 2, 3]

# def add_to(item):
#     return global_list.append(item)
   

# add_to(4)

# print(global_list)

# [1, 2, 3, 4] 
# No es una función pura  (ver ap_funciones_puras.md)
# ------------------------------------------------------------


# Para cambiarla a una función pura hay que pensar como: 
# 1. extender la función para aceptar una lista como argumento
# 2. agregar el elemento a la lista,sin modificar la lista original
# 3. como devolver una nueva lista con el elemento recién agregado.

# Solución:
# Crear una nueva lista, copiar o clonar los datos de lista original.

# CAMBIANDO EL CODIGO ANTERIOR A FUNCION PURA: agrega un valor a lista pero 
# no modifica la lista original.

# Facilidad de leer
# Depuraración
# Consistencia

# def add_to_list(lst, item):

#     nl = lst.copy() # realizando la copia de la lista original

#     nl.append(item) # el nuevo elemento se agrega a la lista nueva

#     return nl # la nueva lista se devuelve al caller

# print(add_to_list(global_list, 7))





