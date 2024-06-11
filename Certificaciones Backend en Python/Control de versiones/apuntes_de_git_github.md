# Temario
* [Conexión a GitHub a través de SSH](#conexión-a-github-a-través-de-ssh)
* [Comandos](#comandos)
* [Ramas](#ramas)
    + [Solicitud de extracción : Compare & pull request](#solicitud-de-extracción-compare--pull-request)
* [Remoto vs local](#remoto-vs-local)
* [Resolver conflictos](#resolver-conflictos)
* [HEAD](#head)
* [Diff](#diff)
* [Blame](#blame)


# Conexión a GitHub a través de SSH

Si planea usar Github desde su dispositivo local, la forma recomendada de autenticarse es usando Secure Shell, o SSH para abreviar. Esto requiere la creación de dos claves: una clave pública y otra privada. La ventaja de usar SSH es que no necesita introducir sus credenciales cuando interactúa con el repositorio remoto. Las claves se generan y almacenan en su máquina local y luego la clave pública se copia en el servidor de Github. Una vez terminada la configuración, todas las operaciones se autentificarán utilizando las claves.

Pasos:

**Generar claves SSH**

1. Abrir la terminal
1. `ssh-keygen -t ed25519 -C "your@email.com"`
1. Presionar ENTER para omitir contraseña y confirmación de contraseña
1. Ambas claves (_privada y pública_) se guardarán en la carpeta .ssh
1. Para añadir nuestra clave a Github, necesitamos obtener una copia de la clave pública que siempre se identifica como .pub en su directorio local
1. Encontrar el nombre del archivo de claves utilizando `ls ~/.ssh/`
1. Para copiar el contenido del archivo .pub en el buffer si esta en Windows o Mac `pbcopy < ~/.ssh/<YOUR KEY>.pub` si esta en Ubuntu usar este comando `xclip -sel clip < ~/.ssh/<SU CLAVE>.pub` si xclip no esta instalado entonces `sudo apt-get install xclip` 

**Añadir sus claves a Github**

1. Inciar sesión en Github
1. Ir a settings
1. En el panel izquierdo en Access, seleccionar SSH and GPG keys
1. Clic en el botón New SSH key
1. Introducir un titulo 
1. Pegar la clave pública
1. Clic en el botón Add SSH key

**Acceso a los repositorios**

Cuando acceda a un repositorio y utilice la autenticación SSH, asegúrese de utilizar siempre la dirección SSH del repositorio.

![cLone ssh](/clone_ssh.png)

[☝️](#temario) 


# Comandos

|Comando                                |Función                                                                                |
|---------------------------------------|---------------------------------------------------------------------------------------|
|`git status`                           |Comprueba si hay cambios en el repositorio, también muestra la rama en la que estoy    |
|`git add <archivo>`                    |Rastrea archivos y permite añadir un commit                                            |
|`git restore --staged <archivo>`       |Retirar un archivo del área de seguimiento                                             |
|`git checkout -B <rama>`               |Crea una nueva rama y cambia a ella, y si la rama ya existe, la sobrescribe con la nueva rama.                                           |
|`git checkout -b <rama>`               |crea una nueva rama y cambia a ella, pero solo si la rama no existe previamente. 
|`git branch <rama>`                    |Crear una rama de forma local                                                          |
|`git branch`                           |Muestra la rama actual en la que estoy parado                                          |
|`git push -u origin <rama_donde_estoy>`|Extrae información de la rama main y publica la rama actual con los commits pendientes |
|`git checkout <rama>`                  |Cambiar de rama                                                                        |
|`git pull`                             |Permite obtener cambios del repositorio remoto                                         |
|`git init`                             |Crear un nuevo repositorio local                                                       |
|`git remote -v`                        |Muestra la URI del repositorio en la nube                                              |
|`git remote add origin <URL DEL REPO REMOTO>`| Vincular un repositorio local con uno remoto                                    |
|`git push origin <rama>`               |Muestra la URI del repositorio en la nube                                              |
|`git diff <archivo>` o `git diff <commit_current> <commit_initial>` o `git diff <rama1> <rama2>`               |Permite ver diferencias de archivos, commits, ramas                                              |
|`git log --pretty=oneline>`            |Muestra el historial de commits                                                        |
|`git blame <archivo>`                  |Permite hacer siguimiento a los archivos (quien, que, cuando)                                                        |
|`git blame -L m,n <archivo>`           |Limitar la salida, es decir específicar el rango de líneas que quiero revisar en un archivo                                                        |
|`git blame -l <archivo>`               |Ver el id completo de los commits                                                      |
|`git log -p <id_commit>`               |Ver el cambio real en el archivo                                                       |


> ![NOTE]
>
> Para configurar la identidad:
```
git config --global user.email "you@example.com"
  git config --global user.name "Tu Nombre"

para configurar la identidad por defecto de tu cuenta.
Omite --global para configurar tu identidad solo en este repositorio.
```

> ![NOTE]
>
> Tener en cuenta que al hacer un push, cuando git solicite usuario y clave, en clave poner el token.

[☝️](#temario) 


# Ramas
## Solicitud de extracción: Compare & pull request

Luego de `git push -u origin <rama_donde_estoy>` Github mostrará la nueva rama a través un aviso

![compare & pull request](/Captura%20desde%202024-06-09%2017-00-54.png)

Permite que el equipo tenga conocimiento de que realice nuevos cambios que quiero que revisen y que yo también quiero aprobar o solicitar cambios en la solicitud de sondeo propiamente dicha.

* Clic en el botón comparar (compara la rama nueva con la rama principal) y solicitud de extracción.
* Clic en el botón Create pull request.
* Como solo voy a fusionar la rama (no hay nadie más), clic en el botón Merge pull request.
* Confirmar la fusión.
* Una vez confirmada la fusión se presenta la opción de eliminar la rama. En mis propios proyectos depende de mi mantener las ramas o eliminarlas.
* Voy a la terminal y compruebo los estados de la rama <other_rama> y la rama main. En la <other_rama> todo esta actualizado. Para cambiar de rama uso `git checkout <branch>`.
* Me dirijo a la rama `main` para extraer los cambios de <other_rama> con `git pull`

> ![NOTE]
>
> Luego el equipo revisará los cambios y los aprobará o los rechazará. Un vez aprobados puede fusionar sus cambios a la rama principal. Esto es mucho más ordenado que las situaciones en las que todo el mundo trabaja en la rama principal. Es particularmente útil si tiene características que estan estrechamente vinculadas entre sí, por ejemplo podrían estar trabajando en alguna otra característica que se cruza con algún código o que requiere cambios y que, muy probablemente, sea alterada por otra persona.

EL enfoque de mantener todo a nivel de rama es mucho más sencillo que si todos trabajan desde la linea principal. De hecho, cuando todos trabajan en la misma rama, es más probable que haya problemas. Tener ramas independiente da lugar a que el proyecto sea más fácil de gestionar. Además, no hay un límite en la cantidad de ramas que pueda tener, el equipo decide sobre las convenciones de asignaciones de nombres que utilizan. En muchos casos al añadir una nueva función, puede agregar la función de palabras clave seguida del nombre de la rama como una ruta de URL, ejemplo: `feature/lesson`.

[☝️](#temario) 


# Remoto vs Local
## Enviar cambios desde el proyecto local a un repositorio remoto

### Crear un repositorio de forma local

* En la terminal dentro de la ruta del proyecto `git init`
* Se inicializa el repositorio pero no esta vinculado en Github `git remote` (la salida no muestra nada)

### Vincular un repo local a un repo remoto

* Agregar la URL del repo remoto `git remote add origin <URL DEL REPO REMOTO>`
* Obtener actualizaciones del repo remoto `git pull`

[☝️](#temario) 


# Push and pull

## Pull

Antes de enviar cambios al repositorio remoto es una buena práctia obtener los cambios del repositorio remoto y reducir la probabilidad de encontrar un conflicto.

Pull: `git pull`


## Push
Push: `git push origin <branch>`

Impulsar los cambios a la rama main del repositorio remoto `git push origin main`

[☝️](#temario) 


# Resolver conflictos

Los conflictos se producen normalmente cuando se intenta fusionar una rama que puede tener cambios que compiten entre sí. Git normalmente intentará fusionar automáticamente (auto-fusión), pero en el caso de un conflicto necesitará alguna confirmación; los cambios que compiten deben ser resueltos por el usuario final. Este proceso se denomina fusión o rebasamiento. 

El desarrollador debe mirar los cambios en el servidor y los cambios en su local y validar qué cambios deben ser resueltos.

Un ejemplo de conflicto de fusión es cuando dos desarrolladores están trabajando en sus propias ramas dependientes. Ambos desarrolladores están trabajando en el mismo archivo llamado Feature.js. Cada una de sus tareas consiste en añadir una nueva característica a un método existente. El desarrollador 1 tiene una rama llamada feature1 y el desarrollador 2 tiene una rama llamada feature2. 

El desarrollador 1 envía el código con los cambios al repositorio remoto. El desarrollador 2 envía sus cambios.

![Pull Push](/Push_Pull_img.png)

Demostración del método de envío y extracción

Vamos a ver cómo se hace esto en Git. Los desarrolladores 1 y 2 revisan el repositorio principal el lunes por la mañana. Ambos tienen exactamente la misma copia. Ambos desarrolladores comprueban una nueva rama: feature 1 y 2.

Desarrollador 1

    git pull
    git checkout -b feature1

Desarrollador 2

    git pull
    git checkout -b feature2

El desarrollador 1 realiza sus cambios en un archivo llamado Feature.js y luego envía los cambios al repositorio para su aprobación a través de una PR (pull request o solicitud de extracción)

    git add Feature.js
    git commit -m 'chore: added feature 1!!'
    git pull origin main
    git push -u origin feature1

El PR se revisa y luego se fusiona con la rama principal. Mientras tanto, el Desarrollador 2 está empezando a codificar su función. De nuevo, pasan por el mismo proceso que el Desarrollador 1:
```
    git add Feature.js
    git commit -m 'chore: added feature 2!!!'
    git pull origin main

From github.com:demo/demo-repo
 * branch            main       -> FETCH_HEAD
   9012934..d3b3cc0  main       -> origin/main
Auto-merging Feature.js
CONFLICT (content): Merge conflict in Feature.js
Automatic merge failed; fix conflicts and then commit the result.
```
Git nos avisa de que se produjo un conflicto de fusión y que hay que arreglarlo antes de que se pueda enviar al repositorio remoto. Ejecutar git status también nos dará el mismo nivel de detalle:

```
    git status
    On branch feature2
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   Feature.js

no changes added to commit (use "git add" and/or "git commit -a")
```
Para poder fusionar, el Desarrollador 2 necesita ver y comparar los cambios del Desarrollador 1. Es una buena práctica ver primero qué rama está causando el problema de fusión. El Desarrollador 1 ejecuta el siguiente comando:

```
 git log --merge

commit 79bca730b68e5045b38b96bec35ad374f44fe4e3 (HEAD -> feature2)
Author: Developer 2 
<developer2@demo.com>
Date:   Sat Jan 29 16:55:40 2022 +0000

    chore: add feature 2

commit 678b0648107b7c53e90682f2eb8103c59f3cb0c0
Author: Developer 1 
<developer1@demo.com>
Date:   Sat Jan 29 16:53:40 2022 +0000

    chore: add feature 1
```

Podemos ver en lo anterior que los cambios conflictivos del equipo ocurrieron en las ramas de feature 1 y 2. El Desarrollador 1 quiere ahora ver el cambio que está causando el conflicto.

```
git diff

diff --cc Feature.js
index 1b1136f,c3be92f..0000000
--- a/Feature.js
+++ b/Feature.js
@@@ -1,4 -1,4 +1,8 @@@
  let add = (a, b) => {
++<<<<<<< HEAD
 +  if(a + b > 10) { return 'way too much'}
++=======
+   if(a + b > 10){ return 'too much' }
++>>>>>>> d3b3cc0d9b6b084eef3e0afe111adf9fe612898e
    return a + b;
  }
```

La única diferencia es la redacción de la declaración de retorno. El desarrollador 1 añadió "too much", pero el desarrollador 2 añadió "way too much". Todo lo demás es idéntico así que en términos de fusión y es un arreglo bastante fácil. Git mostrará flechas <<< >>> para indicar los cambios. El Desarrollador 1 elimina los marcadores para que el código esté listo para ser presentado:

```
let add = (a, b) => {
  if(a + b > 10) { return 'way too much'}
  return a + b;
}
```
El Desarrollador 2 solucionó un conflicto de fusión y puede crear su PR para que el código se fusione con la línea principal.
```
 git add Feature.js
 git commit -m 'fix merge conflicts'
 git push -u origin feature2
```

[☝️](#temario) 


# HEAD

Es un archivo que se encuentra en .git/ 

Dentro de esta carpeta ejecutando `cat HEAD` podemos ver la rama actual, ejemplo:

`ref: refs/heads/main`

Después de introducir este comando `cat refs/heads/main`, aparece un único ID con hash es una referencia al commit actual. `23b412148973d9118e7106b5cc472ea1e55b6522` 

[☝️](#temario) 


# Diff

Permite comparar los cambios en sus archivos, ramas y commits. El comando **Git status** indica cuales de los archivos han sido modificados.  El comando **Git diff** va un paso más allá y dice cuales son exactamente esos cambios.

Cuando se utilizan juntos, puede pensar en ellos como un sistema de archivos, pero para el archivo y ver el contenido, se tendrá que usar gif diff.

Ejemplo:

## Diff en archivos

* Modifico un archivo de mi repositorio de nombre <README.md>
* Utilizo la herramienta ``git diff HEAD` para comparar el archivo actualizado con el head (todavía no hemos completado un commit, no esta disponible para una comparación con otro commit.) 

  ![git diff](/Captura%20desde%202024-06-10%2017-35-46.png)

  el signo - representa lo que el archivo era \
  el signo + representa lo que el archivo es ahora

  ## Diff en commits

* Mostrar el historial de commits `git log --pretty=oneline` utilizo el flag pretty para ver los commit uno por linea 
  ![git log](/Captura%20desde%202024-06-10%2018-00-47.png)

* Puedo utilizar el comando `git diff <id_commit_current> <id_commit_old>` para ver diferencias entre ambos commits
  ![git diff commit](/Captura%20desde%202024-06-10%2018-00-03.png)

  ## Diff en ramas

* Utilizo git branch para ver todas las ramas

  ![git branch](/Captura%20desde%202024-06-10%2018-17-28.png)

  La rama feature/lesson tiene los cambios más recientes

  ![git branch output](/Captura%20desde%202024-06-10%2018-26-15.png)

[☝️](#temario) 


# Blame

Es un comando que permite hacer siguimiento a los archivos (quien, que, cuando). Se usa para observar los cambios de un determinado archivo y mostrar las fechas y los horarios de las modificaciones, y qué usuarios realizaron los cambios. 

Sintaxis: `git blame <archivo>`

![git blame](/Captura%20desde%202024-06-11%2007-30-16.png)

Explicación:

![formato del mensaje](/Captura%20desde%202024-06-11%2007-34-03.png)

> ![NOTE]
> 
> En archivos muy grandes se puede limitar la salida, es decir específicar el rango de líneas que quiero revisar en un archivo.
>
> Sintaxis `git blame -L m,n <archivo>` donde _m_ es la line inicial y _n_ la linea final.

Ejemplo:

![ejemplo git blame -L m,n <archivo>](/Captura%20desde%202024-06-11%2008-12-23.png)

También es posible cambiar el formato en el que se muestra la lista para ver el id completo de los commits

Sintaxis: `git blame -l <archivo>`

Ejemplo:

![git blame -l <archivo>](/Captura%20desde%202024-06-11%2008-26-25.png)

También puedo usar `git log -p <id_commit>` para ver el cambio real en el archivo:

![git log -p <id_commit>](/Captura%20desde%202024-06-11%2008-50-14.png)

[☝️](#temario) 


