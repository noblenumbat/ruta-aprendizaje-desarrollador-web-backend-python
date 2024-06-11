# PyTest

Es uno de los módulos más populares para realizar pruebas unitarias en Python, esto se debe a que permite realizar pruebas simples con esfuerzo mínimo y también tiene un código sencillo y limpio con buena documentación.

Ver archivos de ejemplo en la misma carpeta donde se cuentra este documento.

Los archivos son:

[addition.py](/47_testing/addition.py)

[test_addition.py](/47_testing/test_addition.py)


Pasos para escribir una prueba unitaria con Pytest:

1. Instalar el paquete Pytest, en debian es `sudo apt installa python3-pytest`

1. En el archivo de test por ejemplo (test_addition.py) importar el archivo que contiene el código a probar, ejemplo: `import addition` e `import pytest`

1. Definir las funciones para probar el código de esta manera `test_nombre Archivo.nombreFuncion` ejemplo: `test_addition.add` y `test_addition.sub`. En el cuerpo de la función debe esta la palabra clave "**assert**" a la cual se le pasa el codigo a evaluar y devuelve un booleano "True" o "False", si es "True" la prueba es superada.

1. Abrir una terminal y correr el archivo de test (en Windows `python -m pytest archivo_de_test`) en debian `pytest archivo_de_test` ejemplo: `pytest test_addition.py` . Cuando ejecute pytest para una función específica, agregue :: para ejecutar una función específica en un archivo determinado, ejemplo: `py.test test_addition.py::test_add`

El resultado es algo como esto:
![test execution](/47_testing/Captura%20desde%202024-06-02%2011-41-51.png)

## Banderas utilizadas

Por ejemplo, -v es el marcador:

`python3 -m pytest abc.py -v` ó `pytest abc.py -v` para debian

Verbose muestra información detallada, ejemplo:
![verbose](/47_testing/Captura%20desde%202024-06-02%2014-11-33.png)



Otras opciones de indicadores son:

-v para verbose

-q quiet mode

-s permite que la sentencia print dentro de las funciones se ejecute

-x marca las pruebas para detener la ejecución después de la primera falla

-m se utiliza para marcar una función específica

-k es un indicador de búsqueda y ejecución de pruebas con una palabra clave específica

--tb es para desactivar el código de rastreo de errores

--maxfail n especifica el número máximo de fallas de prueba permitidas

