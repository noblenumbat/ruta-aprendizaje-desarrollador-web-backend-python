# Herencia simple

""" class A:
    pass
class B(A):
    pass
 """
# Herencia multiple

""" class A:
    a = 1

class B:
    b = 2

class C(A,B):
    pass

c = C()
print(c.a, c.b)

# output 
# 1 2 """

# Herencia de varios niveles

""" class A:
    a = 1

class B(A):
    a = 2

class C(B):
    pass 

c = C()
print(c.a)
# output: La salida es 2 porque C deriva de la superclase inmediata de C, y esa es B. """

# Funciones integradas

"""
Existen dos funciones integradas que pueden ser útiles cuando se trata de encontrar la relación 
entre diferentes clases y objetos: issuclass() y isinstance()

A continuación se muestra la primera issubclass()
"""

# Función issubclass()

""" class A:
    a = 1

class B(A):
    pass
 """

"""
Se pasan dos clases como argumentos a esta función y se devuelve un resultado booleano. El ejemplo
anterior se puede amplicar como sigue.
"""

""" 
print(issubclass(B,A)) # True porque B es subclase de A
print(issubclass(A,B)) # False porque A no es subclase de B. A es la superclase. 
"""

# Función isinstance()

"""
La otra función integrada similar a esta es isinstance(), que determina si algún objeto es una instancia de alguna clase.
"""

""" class A:
    pass 
class B(A):
    pass

b = B()
print(isinstance(b,B)) # True  porque b es una instancia de B """

# Función super()

"""
La función super() es una función integrada que se puede llamar dentro de la clase derivada y da acceso
a los métodos variables de las clase padres o hermanas. Las clases hermanas son las clases que comparten 
la misma clase padre. Cuando llama a la función super(), obtiene un objeto que representa la clase padre 
en devolución.

La función super() juega un papel importante en la herencia múltiple y ayuda a impulsar el flujo de ejecución
del código. Ayuda a gestionar o determinar el control de donde puedo sacar los valores de mis funciones y 
variables deseadas.

Si cambia algo dentro de la clase padre, hay una recuperación directa de los cambios de la clase derivada.
Esto se utiliza principalmente en lugares donde se necesita inicializar las funcionalidades presentes dentro de la
clase padre en la clase hija también. Luego, puede agregar código adicional en la clase hija.

Ejemplo:
"""

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit) 

class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

""" 
output: 
Fruit type:  Apple
Apple is sweet """

"""
En el código anterior, si hubiera comentado la línea para la función super(), la salida sería: 
Apple is sweet

Esto ocurrió porque cuando se inicializa la clase hija, no se inicializa la clase base con ella. 
La función super() lo ayuda a lograr esto y a agregar la inicialización de la clase base con la clase derivada.
"""
