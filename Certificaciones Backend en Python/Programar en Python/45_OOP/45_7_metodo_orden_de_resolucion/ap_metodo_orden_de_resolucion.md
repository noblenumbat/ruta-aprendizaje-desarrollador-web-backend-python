# Método Orden de resolución MRO

¿Qué pasa cuando las relaciones entre clases se vuelven complejas? 

¿Cómo se sabe que clases heredan de cuáles?

El orden de resolución proporciona reglas que pueden ayudar a dar sentido a eso.

- *Reglas básicas de orden de método, resolución y cómo se aplican a las clases de herencia.*

- *Linealización de código.*

- *Herencia múltiple y orden de método de implementación, funciones de resolución en python.*

![relaciones complejas entre clases](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2015-53-37.png)

Python tiene muchos tipos de herencia. Los tipos de categorización se basan en el número de clases padre e hija, así como el orden jerárquico, incluida la herencia simple. A grandes rasgos existen cinco tipos de herencia.

1. Herencia simple.

    ![herencia simple](/45_OOP/45_7_metodo_orden_de_resolucion/Imagen%20pegada.png)

1. Herencia múltiple, que involucra una clase hija.

    ![herencia múltiple](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-07-41.png)

1. Herencia de varios niveles.

    ![herencia multinivel](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-10-59.png)

1. Herencia jerárquica: varias subclases heredan a un padre en común.

    ![herencia jerárquica](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-13-04.png)

1. Herencia híbrida: mezcla las características de las demás.

    ![herencia jerárquica](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-16-37.png)


## Linealización de una clase

El Method resolution order, determina el orden de un método dado, o los atributos se pasan a través de una búsqueda de la jerarquía de clases para su resolución; o en otras palabras, de donde pertenece, el orden de la resolución se denomina linealización de una clase y MRO define las reglas que sigue.

## Orden predeterminado en Python

El orden predeterminado en Python es de abajo a arriba, de izquierda a derecha, cuando imagine la herencia de estas clases de Python en una estructura de árbol.

![herencia jerárquica](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-25-19.png)

### Función mro()

![mro()](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-31-00.png)

### Función help()

Pŕoporciona una salida mucho más detallada con información de MRO en la parte superior.

![help()](/45_OOP/45_7_metodo_orden_de_resolucion/Captura%20desde%202024-05-29%2016-37-17.png)

