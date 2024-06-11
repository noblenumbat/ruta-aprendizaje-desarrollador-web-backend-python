# Instalador de Paquetes para Python (pip)

Comprobar que este instalado: 
`pip --version`

Instalar pip: 
`sudo apt install python3-pip`

Instalar un paquete de terceros en Python en todo el sistema:
`sudo apt install python3-xyz` donde xyz es el nombre del paquete, ejemplo, `sudo apt install python3-requests`

Verificar si el paquete esta instalado correctamente:
`pip show requests`

Ejemplo de salida:
```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /usr/lib/python3/dist-packages
Requires: 
Required-by:
```

error: entorno gestionado externamente

× Este entorno se gestiona externamente
╰─> Para instalar paquetes de Python en todo el sistema, intente instalar apt
 python3-xyz, donde xyz es el paquete que estás intentando
 instalar.

 Si desea instalar un paquete Python que no está empaquetado en Debian,
 cree un entorno virtual usando python3 -m venv ruta/a/venv.
 Luego use ruta/a/venv/bin/python y ruta/a/venv/bin/pip. Hacer
 Asegúrate de tener python3-full instalado.

 Si desea instalar una aplicación Python empaquetada que no sea Debian,
 Puede ser más fácil usar pipx install xyz, que administrará un
 entorno virtual para usted. Asegúrate de tener pipx instalado.

 Consulte /usr/share/doc/python3.12/README.venv para obtener más información.

nota: Si cree que se trata de un error, comuníquese con su proveedor de instalación de Python o de distribución del sistema operativo. Puede anular esto, a riesgo de dañar su instalación o sistema operativo de Python, pasando --break-system-packages.
Sugerencia: consulte PEP 668 para obtener especificaciones detalladas.








