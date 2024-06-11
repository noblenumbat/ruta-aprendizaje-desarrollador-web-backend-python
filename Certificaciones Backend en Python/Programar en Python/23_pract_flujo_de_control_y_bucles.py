favorites = ['Creme Brulee','Apple Pie','Churros','Tiramisú','Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite dessert is', dessert)

# FUNCTION break : interrumpe la ejecución del código
# ---------------------------------------------------

# for dessert in favorites:
#     if dessert == 'Churros': # PRIMERO SE EJECUTA ESTE PRIMER BLOQUE DE CODIGO
#         print('Yes! One of my favorite dessert is', dessert)
#         break

# else: # OJO CON LA INDENTACION
#     print('No sorry, that dessert is not on my list')

# FUNCTION continue : se puede utilizar para controlar la iteración del bucle. 
# La diferencia clave es que puede permitirle saltar una sección del bucle, 
# pero luego continuar con el resto.
# ---------------------------------------------------------------------------

# for dessert in favorites:
#     if dessert == 'Churros':
#         continue # HAY QUE SABERLO UTILIZAR
#     print('Other dessert I like are', dessert)

# FUNCTION pass : le permite pasar por el bucle en su totalidad e ignorar eficazmente 
# que se ha cumplido la condicion if.

# for dessert in favorites:
#     if dessert == 'Churros':
#         pass
#     print('Other dessert I like are', dessert)
