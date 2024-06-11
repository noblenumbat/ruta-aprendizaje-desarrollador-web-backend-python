# Temario
* [Comandos básicos](#comandos-básicos)
    + [Directorios y archivos](#directorios-y-archivos)
* [Edicion](#edición)
* [Scripts](#scripts)
* [Uso de bash en la terminal Mac](#uso-de-bash-en-la-terminal-mac)
* [Redireccionamiento](#redireccionamiento)
* [Grep (Impresión Global de Expresiones Regulares)](#grep-impresión-global-de-expresiones-regulares)


# Comandos básicos

## Directorios y archivos

| Description                                                                       | Command                               |     
| --------------------------------------------------------------------------------- | ------------------------------------- |
| Acceder directamente a una carpeta de usuario                                     |  `cd ~/Escritorio`                    |
| Ir a una ruta absoluta                                                            |  `cd /`                               |
| Crear un nuevo archivo                                                            |  `touch  example.md`                  |
| Abrir un archivo en codigo VSCode                                                 |  `code example.md`                    |
| Permite leer o concatenar un archivo                                              |  `cat`                                |
| Muestra el contenido de un archivo página por página                              |  `less`                               |
| Expresión regular global que permite buscar el contenido de archivos o carpetas	|  `grep`                               |
| Comando para recontar palabras (Pipes)                                            |  `wc file1.txt -w`                    |
| Comando para recontar palabras (Pipes)                                            |  `cat file1.txt \| wc -w`             |
| Comando para recontar palabras en más de un archivo (Pipes)                       |  `wc file1.txt file2.txt -w`          |
| Comando para recontar palabras en más de un archivo (Pipes)                       |  `cat file1.txt file2.txt \| wc -w`   |
| Contar la cantidad de archivos (Pipes)                                            |  `ls \| wc -w`                        |

> [!NOTE]
>
> Pipes permite usar la salida de un comando como entrada de otro.

[👆](#temario)


# Edición

Existen unas cuantas opciones para editar archivos en bash. Sin embargo, el más común suele ser VI o Vim. VI significa editor visual y permite realizar ediciones y cambios en un archivo y guardarlos. Es muy similar a lo que puede haber utilizado en aplicaciones como Word. VIM es una versión mejorada de VI con algunas mejoras; de ahí su nombre, editor visual mejorado. Aprender los diferentes comandos en Vim se sentirá un poco diferente en comparación con las aplicaciones GUI, pero una vez que practique se convertirá en un hábito. Vim utiliza los modos para determinar los comandos con los que se puede trabajar:

    Modo normal: Modo por defecto

    Modo de inserción: Permite editar el contenido de los archivos.

    Modo de línea de comandos: Los comandos normales comienzan con :

	
| Description               | Command               |
| ------------------------- | --------------------- |
| Abrir archivo con Vim     |  `vim example.md`     |
| Guardar archivo con Vim   |  `:w`                 |
| Salir de Vim              |  `:q`                 |                       
| Guardar y salir de Vim    |  `:wq!`               |

[👆](#temario)


# Scripts

1. El archivo deberá tener la extension `.sh`
1. La primera linea del archivo debe contener `#!/bin/bash`
1. Para ejecutar el archivo `./example.sh`

[👆](#temario)


# Uso de bash en la terminal Mac

La terminal de Mac puede abrirse de tres maneras: Finder, Launch Pad y Spotlight.

* Finder
    1. Clic en el icono de ***Finder***
    1. Clic en ***Aplicaciones*** en el lado izquierdo
    1. Localizar la carpeta ***Utilities*** y expandirla
    1. Clic en la aplicación ***Terminal***

* Launch Pad
    1. Command + F4
    1. Aparece la ventana vista Launch Pad
    1. En la barra de búsqueda escribir la palabra term
    1. Clic sobre el icono de la Terminal

* Spotlight
    1. Command + Barra Espaceadora
    1. Aparece el modal de Spotlight
    1. Escribir term
    1. Clic sobre el icono de la Terminal

[👆](#temario)
	

# Redireccionamiento

El flujo de trabajo básico de cualquier comando de Linux requiere una entraa y una salida. El dispositivo de entrada estándar es el teclado y el dispositivo de salida estándar es la pantalla. Utilizando el redireccionamiento se puede cambiar la entrada o la salida estándar.

Tipos de redireccionamiento de entrada/salida:

* Standard Input
* Standard Outpunt
* Standard Error

El shell mantiene una referencia de entrada, salida y error estándar mendiante un sistema de numeración.

## Entrada Estándar **0** -> stdin

Pasos: para almacenar entradas en un archivo txt.

1. Definir el archivo que va a contener la entrada `cat > input.txt`  
1. Realizar la entrada `This is me adding some text from keyboard!`
1. `ENTER`
1. `Ctrl + D `
1. Observar el texto añadido `cat < input.txt`

## Salida Estándar **1** -> stout

Todos los comandos utilizados hasta ahora envian las salidas a un archivo especial (stdout) llamado "salida estándar". 

¿Cómo enviar una salida a un archivo de texto?

`ls -l > output.txt`

Ver el contenido del archivo: `less output.txt`

```
total 16
-rw-rw-r-- 1 jonathan jonathan 89 jun  7 17:42 file1.txt
-rw-rw-r-- 1 jonathan jonathan 88 jun  7 17:45 file2.txt
-rw-rw-r-- 1 jonathan jonathan 26 jun  7 19:29 inputnuevo1.txt
-rw-rw-r-- 1 jonathan jonathan 26 jun  7 19:28 input.txt
-rw-rw-r-- 1 jonathan jonathan  0 jun  7 21:58 output.txt

```

## Error Estándar **2** -> stderr

Cuando se genera un error también hay que especificar que quede registrado en un archivo.

Sintaxis: `Command <input.txt>output.txt2>error.txt`

Ejemplo:

![error.txt](/Captura%20desde%202024-06-07%2022-12-31.png)

Ahora el error se puede ver en el archivo de texto

![contenido del error.txt](/Captura%20desde%202024-06-07%2022-14-25.png)

Para crear el archivo de error y/o generar el archivo de salida

![error y salida archivo](/Imagen%20pegada.png)
 
Ahora el error y/o salida se puede ver en el archivo de texto

![vista de la salida](/Captura%20desde%202024-06-07%2022-24-34.png)

[👆](#temario)


# Grep (Impresión Global de Expresiones Regulares)

Se utiliza para buscar en archivos y carpetas, así como en el contenido de los archivos.

Usar Grep para buscar patrones de nombres con coincidencias en el inicio (Búsqueda estándar).

Lo siguiente son ejemplos:

```
grep Sam names.txt

--- 

grep sam names.txt # coincidencias parciales

---

grep -i Sam names.txt # usando una marca para ignorar sensibilidad entre mayúsculas y minúsculas

--- 

grep -w Sam names.txt # coincidencia exacta usando una marca diferente

--- 

ls  /bin | grep zip # puedo usar el comando pipe para combinar diferentes búsquedas para grep. Comprobando archivos ejecutables dentro del directorio bin

```

[👆](#temario)
