#args
#Tiene la ventaja de poder pasar cualquier cantidad de argumentos

#ejemplo:

# def sum_of(a,b):
#     return a + b

# print(sum_of(4,9))
#13

#-------------------------------------------------------------------------------------------
#¿Qué pasa si agrego un tercer parámetro?
# def sum_of(a,b):
#      return a + b

# print(sum_of(4,9,5))
#TypeError: sum_of() takes 2 positional arguments but 3 were given

#--- para solucionar esto, entonces utilizo args para aceptar n cantidad de parámetros:

# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print(sum_of(4,9,5,30,2))

#50

#-------------------------------------------------------------------------------------------

#kwargs
#se pueden pasar cualquier cantidad de argumentos de palabra clave 

def sum_of(**kwargs):
    sum = 0
    for k, v, in kwargs.items():
        sum += v
    return round((sum),2)

print(sum_of(cafe=2.5,almohabana=1.8,pan=5))
#9.3