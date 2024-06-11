# Programación Funcional
Permite procesar grandes cantidades de datos a gran velocidad.

## Tipos de funciones:
*Tradicional*: 

*Pura*: siempre haran lo mismo y devolveran los mismos resultados sin importar cuantas veces se llamen.

## Funcion Tradicional vs Función Pura

||Tradicional|Pura|
|---|---|---|
|Acceso variables de estado global|🗸|❌|
|Modificar variables globales|🗸|❌|
|Acceso variables de estado local|🗸|🗸|
|Cambio de Args|🗸|❌|
|Las salidas de las funciones dependen de las entradas|❌|🗸|

Es un paradigma de programación que utiliza funciones para código limpio, consistente y mantenible.

En comparación con la programación orientada a objetos, la programación funcional se diferencia por su diseño.

**Tener en cuenta**: la programación funcional no cambia los datos fuera del ámbito de la función.

![](/40_pro_funcional/Captura%20desde%202024-05-18%2017-18-22.png)

La función debe eviar modificar los datos de entrada o argumentos que se pasan, **en su lugar solo debe devolver el resultado completo de la función prevista que se llama.**

Las funciones se consideran autonomas o independientes y esto ayuda a la naturaleza limpia y elegante del código.

El propio lenguaje tiene que permitir pasar la función como argumento y también devolver una función a su llamador.

Las funciones son ciudados de primera clase.
![](/40_pro_funcional/Captura%20desde%202024-05-18%2017-24-51.png)

Tienen el mismo nivel de cadenas y números.

Funciones

|Se pueden:||
|---|---|
|Asignar una variable|🗸|
|Pasar como argumento|🗸|
|Retornar su caller|🗸|

## Ventaja
La lógica que hay detras de ciertas tareas ya se encuentra integrada, las funciones son reutilizables y de ese modo se ahorra mucho tiempo de desarrollo.