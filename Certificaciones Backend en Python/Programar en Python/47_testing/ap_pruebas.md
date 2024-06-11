# Testing

## Razones para realizar pruebas de software

* Detectar diseños deficientes
* Cambiar flujo o funcionalidad eficientes
* Abordar problemas de escalabilidad
* Encontrar vulnerabilidades de seguridad
 
Las pruebas ayudan a proporcionar pruebas AB para encontrar las mejores opciones adecuadas, abordar compatibilidad con plataformas y dispositivos, ofrecer garantías a las partes interesadas, y brindar una mejor experiencia a los usuarios finales.

## Buenas prácticas que de deben seguir en pruebas para lograr resultados óptimos

* Permite la reutilización de las pruebas
* Las pruebas deben ser rasteables a los requisitos establecidos 
* Las pruebas escritas beben basarse en un propósito
* Ser eficientes y permitir repetibilidad

## Ciclo de vida de las pruebas

* Planeación
* Preparación
* Ejecución
* Presentación de informes

## Pasos

* Scripts
* Casos de prueba
* Compilar los resultados de las pruebas
* Corregir los defectos basados en ellos
* Generar informes a partir de los resultados de las pruebas

## Propósito

* Mejorar la funcionalidad
* Mejorar el flujo
* Encontrar defectos

Un caso de prueba bien escrito eventualmente proporciona buena cobertura, reutilización, mejor experiencia del usuario, reducción de costos y aumento de la satisfacción general.

## Tipos de pruebas

Garantía de calidad es un componente importante para los ciclos de vida de desarrollo de software. Esto se debe al desarrollo de herramientas y técnicas de prueba. La pregunta es, ¿qué tipo de pruebas se deben usar?

- *Pruebas de caja blanca*

    El evaluador conoce el diseño del código y funcionalidades.


- *Pruebas de caja negra*

    Funciona sin información previa de diseño del código y funcionalidades.

- *Pruebas funcionales*

    Se basan en los requisitos del negocio establecidos. Determinan si las características y las funcionalidades están alineadas con las expectativas.

- *Pruebas No funcionales*

    Son más complejas de definir e implican métricas como rendimiento general y la calidad del producto.

- *Pruebas de mantenimento*

    Se producen pruebas de mantenimiento cuando el sistema y su entorno operativo se corrige, cambia o extiende.

    Existen también métodos de prueba automatizados que dependen de la escala de software. La categorización más ampliamente aceptada es en términos de los niveles de pruebas a medida que se avanza en el ciclo de vida del software.

## Niveles principales de prueba
Se basan entre sí y tienen un flujo secuencial.

1. *Pruebas unitarias o de componentes*: 

    El programa prueba componentes de individuos específico aislándolos. Los componentes son de nivel bajo, lo que significa que están más cerca del código escrito real. A veces implican el uso de automatización para integración continua debido a su tamaño pequeño. Por lo general, se escriben estan pruebas mientas se escrible el código. En Python Las pruebas unitarias se pueden escribir con paquetes tales como prueba pi, pruebas de integración.

1. *Pruebas de integración*: 
    
    Combinan las pruebas unitarias y prueban el flujo de los datos de un componente a otro. La palabra clave es **"interface"**. Esto significa que prueba si los datos se obtienen correctamente de una base de datos dentro del código Python, y si lo ha enviado a la página web. Existen diferentes enfoques, como arriba abajo, abajo arriba y sandwich. Su enfoque depende de las interfaces de nivel de código que intente primero. Se basa en las pruebas unitarias y un evaluador se ocupa de ello.

1. *Pruebas del sistema*: 

    A continuación, se realizan pruebas del sistema que evalúan todo el software que probó con los requisitos del conjunto y expectativas para asegurar la integridad. Esto incluye mediciones de la ubicación de componentes desplegados, como:

    + Confiabilidad
    + Rendimiento
    + Seguridad y
    + Equilibrio de carga

    También mide la operabilidad en el ambiente de trabajo, como la plataforma y el sistema operativo.

    Esta es la etapa más importante manejada por el equipo de evaluadores. También es la etapa más crítica, ya que el envío de software a las partes interesadas y el usuario final ocurre después de esta fase.
    
1. Pruebas de aceptación: el tipo final de prueba es la prueba de aceptación. Cuando el producto llega a esta etapa, generalmente se considera que está listo para el despliegue, se espera que este libre de errores y que cumpla con los estándares establecidos. Los grupos de interés y los pocos usuarios finales selectos están involucrados en las pruebas de aceptación. Normalmente involucra pruebas alfa, beta y regresión. Una forma de acercarse a esto es dar situaciones escritas a los usuarios con antelación. Utilice los resultados para realizar mejoras y tratar de encontrar errores que se perdieron antes.

Todos los diferentes niveles de prueba están diseñados para optimizar el software en fases diferentes.

> ![NOTE]
>
> 👀
> La clave para realizar pruebas es realizar pruebas tempranas y con frecuencia. Aunque cada una de las fases de prueba es importante, la detección temprana ahorra tiempo, esfuerzo y dinero. 

A medida que el código se vuelve cada vez más complejo, los errores se vuelven más díficiles de corregir. No necesariamente significa que las pruebas de la unidad solo se realizarán en el comienzo y aceptación en una etapa posterior. Existen muchos ciclos de prueba donde estos niveles son abordados iterativamente. Un ejemplo típico es el modelo de desarrollo ágil, aquí lanzamos diferentes versiones del producto de forma iterativa y realizamos pruebas de aceptación cada cierto número de semanas.