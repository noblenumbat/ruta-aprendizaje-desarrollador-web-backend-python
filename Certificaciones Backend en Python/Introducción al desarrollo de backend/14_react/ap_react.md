# Que es React
Es una biblioteca de Java Script de código abierto. Para crear aplicaciones de una sola página (SPA) y también para desarrollar aplicaciones móviles con React Native.

## Componentes

Permite definier componentes que se pueden combinar para crear una aplicación web. Un componente es básicamente un pequeño fragmento de interfaz de usuario, como un reproductor de música o una galería de fotos.

El modelo de componentes permite hacer varias cosas:

1. Desarrollar y probar partes de la aplicación en aislamiento.
1. Reutilizar componentes en múltiples secciones de la aplicación.

## ¿Cómo funciona?

React permite crear interfaces de usuario, pero ¿Cómo se convierten los componentes de React en los elementos de la página web que usted usa?

Cuando el navegador recibe una página HTML, construye un DOM para representarla. Pero actualizar el DOM es una tarea costosa, porque el navegador tarda mucho en hacerlo. Cada vez que se actualiza el DOM del navegador, el navegador vuelver a calcular la página. Sin embargo, muchos sitios web grandes y populares aún se cargan al instante.

*¿Como resuelve React este problema?*

Calculando su propio DOM virtual. ¿Cómo se relacionan los componentes de React con el sitio web que se muestra en el navegador.

Un componente de React tiene relación directa con un elemento HTML que se muestra en la página web. ¿Cómo hace React para saber que elementos deben actualizarse?  Aquí entra en juego el DOM virtual de React. Cuando React construye su arbol de componentes,  construye su propia cúpula en la memoria, que se llama "DOM virtual".

## DOM virtual

Es una representación del DOM del navegador que se mantiene en la memoria. React utiliza el DOM virtual para actualizar el navegador DOM solo cuado es necesario. Esto garantiza que su aplicación sea rápida y receptiva a la entrada del usuario. 

*Conciliación*

React comprueba si los componentes HTML  del DOM virtual coinciden con el DOM del navegador. Si se requiere un cambio se actualiza el DOM del navegador. Si no ha cambiado nada, no se realiza ninguna actualización. Este proceso se denomina "conciliación".

1. Se actualiza el DOM virtual con la version anterior del DOM virtual.
1. Luego React compara el DOM virtual con la version anterior del DOM virtual y determina que elementos han cambiado en el navegador.
1. Solo los elementos modificados se actualizan en el DOM del navegador.
1. Los cambios en el DOM del navegador hacen que la página web mostrada cambie.

## Jerarquía de componentes

Cada aplicación de React contiene almenos un componente, el componente raíz o componente de aplicación. Los componentes se agregan al conjunto de la aplicación para construir una estructura de árbol de componentes que componen la aplicación. 

Ejemplo :  (*Aplicación lista de compras*)

En la raíz tenemos el componente de la aplicación, este componente tiene dos componentes secundarios: NewItemBar y Shopping List

El componente secundario de cada árticulo de la lista de compras. Aunque el artículo en sí podría ser diferente, como pollo o fideos, se muestra de la misma manera que otros artículos.

![ejemplo jerarquía de componentes](/assets/Captura%20desde%202024-05-26%2009-31-27.png)

Por lo tanto se puede reutilizar el componente para cada artículo de compra para mostrar varios artículos.

Cuando un usuario quita los artículo la lista se actualiza y elimina el componente secundario del artículo de compra correspondiente.

![actualización de la lista de compra](/assets/Captura%20desde%202024-05-26%2009-32-35.png)










