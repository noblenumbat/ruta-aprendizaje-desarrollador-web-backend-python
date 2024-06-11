# Espacios de nombres y ámbitos
La documentación oficial de Python define espacio de nombres como la asignación de los nombres a los objetos, y el alcance es la región textual de un programa de Python donde se puede acceder directamente al espacio de nombres. 

Python scope

```
# Built In scope (def)
def outer():

    #Enclosed Scope
    b = 2
    def inner():

        #Local Scope
        c = 3
```

En este punto, el diccionario con sus pares de valores clave sirve como la estructura de datos ideal para el mapeo de nombres y objetos.

Python dictionary

`beverage_dict = {1: 'Coffee', 2: 'Tea', 3: 'Water'}`

Módulos

Son un tipo de espacio de nombres. 

Los espacios de nombres y los ámbitos pueden llegar a ser muy confusos muy rápidamente y así es importante para conseguir tanta práctica de alcances como para garantizar un estándar de calidad.

Existen cuatro tipos principales de ámbitos que se pueden definir en Python: 

+ local: Esto es donde la primera búsqueda de una variable está en el ámbito local.
Una variable declarada en el interior de una función es local.
+ cerrado: Esto se define dentro de una función cerrada o anidada.
+ global: Se define en el nivel superior o simplemente las funciones externas.
Las variables que estan fuera del ámbito de cualquier función generalmente es global.
+ integrado: Son las funciones, las palabras clave presentes en el módulo integrado.

![scope](/46_modulos/46_3_domains_space_names/Captura%20desde%202024-05-30%2018-53-45.png)

La práctica de intentar determinar en que ámbito una cierta variable pertenece se conoce como resolución de ámbito.

La resolución del ámbito sigue lo que se conoce conmumente como la regla LEGB.

Ejemplo:

Existen tres declaraciones posibles de la variable. A nivel global, dentro de la función "b" o dentro de la función anidada "c" que se llama desde "b".

La función "id()" se utiliza en "c()" y "b()" en las sentencias print, que devuelve la identidad de los objetos. 

```
greek = "alpha"
        Print(:Global declaration: "+Greek, id(Greek))
    def b():
        Greek = "beta"
        print("Inside local: : + greek,id(greek))
        def c():
            greek = "gamma"
            print("Enclosed: " + greek, id(greek))
    c()
        print("Inside local: End of local scope: " + greek, id(greek))
    
    b()
        print("Global after local execution: " + greek, id(greek))
```

*Observaciones de salida del ejemplo anterior:*

### Global level
La "id" para la variable global alfa de la variable permanece igual, como se define después de que el código se ejecuta completamente.

Global declaration: alpha 4380175536

## Local variable
La "id" para la variable local beta en el interior de la función b permanece sin cambios antes y después de la ejecución anidada "c".

Inside local: beta 4380137072

## Nested function
La "id" para Gamma solo está asignada dentro del ámbito de la función anidada. 

Enclosed: gamma 4380478000

Inside local: End of local scope: beta 4380137072

Global after local execution: alpha 4380175536

La "id" para las tres variables es diferente, aunque todas tengan el mismo nombre de variable.

## Las variables
Las variables en Python son declaradas implícitamente cuando las define. Eso significa, a diferencia de otros lenguajes de programación, que no existe una declaración especial hecha, en Python para la variable que especifica su tipo de datos.

Lo que también implica es que una variable dada es local y no global cuando se declara, a menos que se indique lo contrario.

Esto contrasta con la mayoria de otros lenguajes de programación donde las variables son globales por defecto.

Cuando se declara una variable en un espacio global, también es local para este espacio. 

Ejemplo: [ver código y salida del código](/46_modulos/46_3_domains_space_names/domains_spaces_names.py)

Si nos fijamos en el contenido de estos dos diccionarios,

Local and global scope

```
country = "USA"
print("Country name: " + country)
print(globals())
print("-------------")

def b():
    country = "Germany"
    print("Country name: " + country)
    print(locals())

b()
print("Country name: " + country)
```

Aúnque las variables locales son aceptables, se desaconsejan por una serie de razones.

Cuando trabaja con código de producción, la estructura del proyecto puede ser compleja, y trabajar con variables globales puede ser difícil de diagnosticar, lo que lleva a lo que se denomina código "spaghetti".

Otros paradigmas, como los modificadores de acceso, la concurrencia, y la asignación de memoria se manejan mejor con variables locales. 

Al principio del recorreido con Python, siempre es una buena idea integrar buenas prácticas en su código. 

Existen dos palabras clave que se pueden usar para cambiar el ámbito de las variables: **"blobal"** y **"nonlocal"**.

La palabra clave "global" nos ayuda a acceder a variables globales desde dentro de la función.

**nonlocal** es un tipo especial de ámbito definido en Python que se utiliza dentro de las funciones anidadas solo en la condición que se ha definido antes en las funciones cerradas.

Ejemplo: para entender la idea de ámbito para un atributo. *[ver el ejemplo en el código](/46_modulos/46_3_domains_space_names/domains_spaces_names.py)*









