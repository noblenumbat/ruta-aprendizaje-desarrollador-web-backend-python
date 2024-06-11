# Clases y métodos abstractos

*Ventajas*: Funcionalidad de cada clase que se deriva de ella. Ejemplo un vehículo, se puede derivar un carro, una mula, un barco.

Los métodos en los que ponemos la clase abstracta están garantizados para que se presenten en la clase derivada, porque deben implementarse. Si un vehículo tiene un método de encendido del motor, entonces aseguramos que cualquier método que llama a una clase derivada, es decir, buscando "encender motor" lo encontrará.

Esto podría ser por razones de:
- *interoperatividad*, 
- *consistencia*, y 
- *evitar duplicación de código en general*.

En la programación orientada a objetos, **la clase abstracta es un tipo de clase para la que no se puede crear un instancia**. Python tampoco admite abstracción directamente.

Necesita imponer un módulo solo para defirnir una clase abstracta, además los métodos en una clase abstracta necesitan ser definidos antes de que se puedan implementar.

## Por qué utilizar clases abstractas

### Ventajas

* Capacidad de ocultar los detalles de la implementación sin sacrificar la funcionalidad.
* La implementación en clases abstractas se puede hacer de dos formas: 1. Como base las clases abstractas carecen de implementación propia, los métodos se deben implementar por la clase derivada. 2. Se puede utilizar la función "super()". 

## Módulo
Para definir una clase abstracta. El módulo se conoce como la clase abstracta o ABC, y necesita importarse con algún código.
![modulo](/45_OOP/45_6_clases_y_metodos_abstractos/Captura%20desde%202024-05-28%2020-17-28.png "Haciendo un import")

Después de eso, se puede crear una clase denominada "SomeAbstractClass" y pasar el módulo ABC para que herede la clase.

![modulo](/45_OOP/45_6_clases_y_metodos_abstractos/Captura%20desde%202024-05-28%2020-21-04.png "Heredando la clase abstracta")

El siguiente paso es importar el decorador de método abstracto dentro del mismo módulo.
![modulo](/45_OOP/45_6_clases_y_metodos_abstractos/Captura%20desde%202024-05-28%2020-23-55.png "Importar el decorador de método abstracto")

>![NOTE]
>
> El decorador es una función que requiere otra función como sus argumentos y da una nueva función como su salida. Se denota con el signo "add". *Los decoradores son como funciones ayudantes que agregan funcionalidad a una función ya existente*.

Por último, se define un método abstracto que no se puede llamar en un objeto de esta clase.

![metodo abstracto](/45_OOP/45_6_clases_y_metodos_abstractos/Captura%20desde%202024-05-28%2020-31-04.png "Se define el método abstracto")

Se podrá llamar a este método sobre sobre objetos de clase que heredan de esta clase.
|class B(A)|b = A()|
|---|---|
|🗸|❌|

Del mismo modo, podemos definir métodos abstractos con la ayuda de lo que denominamos un decorador de método abstracto presente dentro del mismo módulo.

Cualquier clase abstracta puede consistir en uno o más métodos abstractos. Sin embargo, una clase que tiene una clase abstracta como su padre no se puede instanciar a menos que anule todos los métodos abstractos presentes al principio.

![metodo abstracto](/45_OOP/45_6_clases_y_metodos_abstractos/Captura%20desde%202024-05-28%2020-54-51.png "Eliminar método abstracto para crear un objeto a partir de una clase derivada de una clase abstracta")

En la class Donation se elimina el método abstracto, para dar la posibilidad de crear un objeto a partir de una clase derivada de una clase.

Luego se crean las instancias, y se llama la función sobre cada una de ellas, tambien se crea una lista de montos, al que se anexaran los valores devueltos. Por último una sentencia "print" para los importes que daran el valor total de las donaciones de ambos empleados.
