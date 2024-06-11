# Practica formato director (organizando mi número de telefono: 317 353 8964)
          
a = '3' # 0
b = '3' # 3
c = '3' # 5
d = '4' # 9
e = '9' # 7 
f = '8' # 6
g = '6' # 8
h = '1' # 1
i = '7' # 2
j = '5' # 4

# asignan el orden directamente desde el print

print('Mi número de teléfono es: {}{}{} {}{}{} {}{}{}{}'.format(a,h,i,b,j,c,f,e,g,d))

# asignando el orden directamente desde las llaves con los indices 
print('Mi número de teléfono es: {0}{7}{8} {1}{9}{2} {5}{4}{6}{3}'.format(a,b,c,d,e,f,g,h,i,j))

tel = a,h,i,b,j,c,f,e,g,d

# prueba función len()
print(len(tel))