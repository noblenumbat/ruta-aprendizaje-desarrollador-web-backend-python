# Administrador de servicios de Windows

*Recomendación*: Cuando se instala una aplicación independiente o una solución, se recomienda se cree una cuenta local o de Active Directory para que arranque ese servicio, por temas de seguridad.

*Tipos de inicio*:

- Inicio retrasado (Delayed Start), para permitir un inicio rápido del sistema operativo.

- Automatic

- Manual

- Disable

*Recuperación*: Permite establecer las acciones que se llevaran a cabo, en caso que se presenten fallas en el servicio.

*Dependencias*: Si las dependencias el servicio no arranca, ejemplo: para Windows Remote Management las dependencias son:  HTTP Service, Remote Procedure Call (RPC).

## Recomendación

Al llegar al trabajo, revisar los servicios de Windows.
