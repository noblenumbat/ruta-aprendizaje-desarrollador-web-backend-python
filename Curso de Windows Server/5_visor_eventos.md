# Visor de Eventos
Importante tener una copia de seguridad de todos nuestros registros.
Existen scripts para crear una copia automatica de estos registros, cuando el servidor tiene una carga considerable de eventos, con el objetivo de guardarlos en una ruta especifica.

También se pueden guardar manualmente por Acciones > Vaciar  registro (Guardar y borrar registros)

En la categoria de Registros de Windows, en Sistema se pueden obtener información de los errores en el sistema operativo.

## id del Evento
Tener en cuenta el id. del evento porque con ese número se puede obtener información exacta del evento en Internet.

### Recomendación:
Al igual que los servicios, se recomienda revisar diariamente el visor de eventos.

## Eventos reeviados
Son eventos reeenviados desde otros servidores.

## Cambiar ubicación de los archivos de registros de eventos

Se hace a través de las Directivas de Grupo Locales de nuestro servidor.

Pasos:

1. Ir a Directivas de Grupo Locales:
    
    * En **Ejecutar** escribir el comando: gpedit.msc 

2. Ir a Plantillas Administrativas > Componentes de Windows.

3. Buscar la carpeta de Servicios de Registro de eventos.

4. Seleccionar la categoria de registro por ejemplo, Aplicación

5. Crear una carpeta preferiblemente en el Disco Local C.

6. Seleccionar 'Controlar la ubicación del archivo de registro' > Habilitar 

7. En 'Ruta de acceso del archivo de registro' pegar la ruta de la carpea creada en el paso 5. Ejemplo: C:\Eventos
![](/assets/Captura%20desde%202024-05-21%2020-59-56.png)

8. Validar el nombre del archivo de registro desde el Visor de eventos para colocarlo en la nueva ruta. En este ejemplo para 'Aplicación'
![](/assets/Captura%20desde%202024-05-21%2021-03-03.png)

9. Quedaria así:
C:\Eventos\Application.evtx

10. Aplicar > Aceptar
![](/assets/Captura%20desde%202024-05-21%2021-15-26.png)
*En la imagen se puede observar que se han generado cambios de ruta para cada una de las categorías de registros de eventos.*
### Aceder al visor de eventos desde un sistema Window 10

* Panel de Control

* Herramientas Administrativas

* Visor de Eventos