
# Activar Windows

*Recomendación:* Activar Windows inmediatamente se instale. Puede suceder que luego de la activación, si existen configuraciones previas, se presenten novedades o fallas.

Pasos:

1. Ingresar a configuración>Update & Security>Activación.
1. Cambiar clave del producto.
1. El equipo se conecta a una organización para validar la clave de producto.

## Activar Windows a través del CMD

1. Desde CMD como Admin 
1. Proporcionar la clave del producto | Cambiar la clave del producto ➡️ slmgr -ipk XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX	
1. Activar Windows ➡️ slmgr -auto
			 	

## Covertir la versión de evaluación en versión COMPLETA
1. Requisitos: tener la Key
1. Consultar la versión instalada ➡️    DISM /online /Get-CurrentEdition
1. Proporcionar la clave ➡️ DISM /online /Set-Edition:ServerStandard /ProductKey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX /AcceptEula

*Recomendación:* Realizar esto antes de hacer configuraciones en el sistema.



