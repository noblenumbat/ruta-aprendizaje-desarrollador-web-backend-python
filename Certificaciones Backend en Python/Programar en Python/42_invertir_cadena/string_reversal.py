# Primera manera de invertir una cadena
# ----------------------------------------------------

# Sintaxis de corte ampliada
# str[start:stop:step]



#Ver 40_pro_funcional/pract.py
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    return palabra

print(invertir_palabra('pajaro'))

trial = 'reversal'
trial = trial[::-1] #se modifica la cadena en la variable
print(trial)

# Segunda manera de invertir una cadena
# ----------------------------------------------------
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0] # str[1] recorre cadena desde el comienzo 
     

str = 'reversal'
print(string_reverse(str))