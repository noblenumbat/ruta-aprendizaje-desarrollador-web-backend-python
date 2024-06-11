# Funciones Puras

Por ejemplo, si tengo una lista en el ámbito global, una función pura no puede agregar algo a esa lista o alterarla de cualquier manera.

Es imporntante mantener limpio el código para facilitar la depuración, y asegurar que sea extensible.
Las funciones puras me pueden ayudar.

Las funciones puras se pueden usar en la programación funcional.

Es una función que no cambia o tiene algun efecto en una variable, datos, lista o conjuntos más allá de su propio alcance. 

## Beneficios

1. Con funciones puras siempre sabe cuál será el resultado.
1. Las funciones puras son fragmentos consistentes de codigo que hacen exactamente lo que están destinado a hacer.
1. Incluyen la capacidad de cache ya que sabe que el rendimiento siempre va a ser el mismo.
1. Se adaptan bien a un programa de varios hilos.

## Programa de varios hilos

Más de un proceso se puede ejecutar simultáneamente, lo que crea muchos hilos de datos.

Las funciones puras ayudan a evitar cambios en el ambito global asegurando que los datos se mantengan confiables.
