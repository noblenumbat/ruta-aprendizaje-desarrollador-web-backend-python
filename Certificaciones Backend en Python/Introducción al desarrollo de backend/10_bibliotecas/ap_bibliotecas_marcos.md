# Introducción a los marcos y bibliotecas de IU
## Adminitrador de paquetes (Package manager)
Un administrador de paquetes es una herramienta que descarga e instala dependencias automáticamente. Nos referimos a las dependencias como "paquetes".
Tambien proporciona la capacidad de publicar sus propios paquetes.
Para cada dependencia, se puede especificar una versión y el administrador de paquetes la descargará.

![](/10_bibliotecas/package-manager.png)

Si hay un arbol de dependencias, el administrador de paquetes se encargara de eso también.

Para usar API sin problema de dependencias.

### Node Package Manager (NPM)

El administrador de paquetes más común para el desarrollo de front-end.

---
Luego que se descargan las dependencias, necesito incluirlas en en un archivo HTML.

Como desarrollador, desarrollando una aplicación para un web server, usare una herramienta de creación de lotes (bundling)  para combinar todas la dependencias dentro de un archivo.

![](/10_bibliotecas/bundle.png)

Si el lote es muy grande hay muchos programas que pueden dividir las dependencias en varios lotes.
Herramientas como: *Gulp, Webpack*
![](/10_bibliotecas/many-packages.png)

