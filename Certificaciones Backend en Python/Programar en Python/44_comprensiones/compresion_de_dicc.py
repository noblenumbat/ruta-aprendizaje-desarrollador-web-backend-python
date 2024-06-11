""" La sintaxis para la comprensión del diccionario es:

dict = { key:value for key, value in <sequence> if <condition> }  """

""" La comprensión del diccionario toma una o dos listas como entrada y crea un diccionario fuera de él. 
Ahora demostraré cómo se puede hacer esto usando solo una lista y usando dos listas.  """

# using range() function and no input list

usingrange = {x:x*2 for x in range(12)}
print("Using range(): ", usingrange)

# output:
# Using range(): {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}

# -------------------------------------------------------------------------------------------------------

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "JUne", "July", "Sept", "Oct", "NOv", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict )

# output:
# Using one input list to create dict:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144} 

#--------------------------------------------------------------------------------------------------------
# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two list: ", months_dict)  
# output:
# Using two list:  {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'JUne', 7: 'July', 8: 'Sept', 9: 'Oct', 10: 'NOv', 11: 'Dec'}

""" Nótese como en el caso de utilizar dos listas, el formato que sigue es: 

    new_dict ={key:value for (key, value) in zip(list1, list2)}

Aquí he utilizado la función zip que combina las dos listas. Cuando las dos listas son de longitud diferente, la longitud de la lista más corta es la longitud del diccionario. """

