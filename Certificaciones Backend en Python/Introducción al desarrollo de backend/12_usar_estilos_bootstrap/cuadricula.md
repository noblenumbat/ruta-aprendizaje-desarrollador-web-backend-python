# Cuadricula
Crear un sitio web utilizando un diseño receptivo requiere una cuadrícula y breakpoints receptivos.

Bootstrap proporciona ambos como parte de su biblioteca. 

El sistema de cuadricula de bootstrap nos ayuda a crear diseños de páginas web a través de una serie de filas y columnas que albergan nuestro contenido.

!["Cuadricula de bootstrap"](/assets/Captura%20desde%202024-05-25%2008-56-23.png)

Para la cuadrícula, Bootstrap utiliza un sistema de cuadrícula de 12 columnas que puede ser fluido o fijo.

!["Cuadricula de bootstrap"](/assets/Captura%20desde%202024-05-25%2008-58-30.png)

El sistema de cuadrícula de Bootstrap siempre tiene filas, columnas y contenedores.

El contenedor es el elemento raíz. El contenedor contiene y alinea el contenido.

Su ancho se determina en función del punto de interrupción receptivo actual.

!["Sistema de cuadrícula"](/assets/Captura%20desde%202024-05-25%2009-02-33.png)

Se pueden agregar filas y, dentro de ellas, se pueden agregar columnas.

!["Rows and columns"](/assets/Captura%20desde%202024-05-25%2009-14-55.png)

>[!NOTE]
>
>Si quiero controlar controlar cuántos espacios utiliza una columna, puedo poner un sufijo de número.

Ejemplo:

`<div class="col-8">`
`<div class="col-4">`

col-12 para dispositivos móviles ya que al ocupar todas las columnas de la cuadrícula se apilan una debajo de otra.

Y col-lg-6 para escritorio para que las columnas de la cuadrícula se distribuyan una al lado de la otra.
`<div class="col-12 col-lg-6">`
