# Temario
1. [Comandos SQL comunes](#comandos-sql-comunes)
    + [Lenguaje de definición de datos (DDL)](#lenguaje-de-definición-de-datos-ddl)
    + [Lenguaje de manipulación de datos (DML)](#lenguaje-de-manipulación-de-datos-dml)
    + [Lenguaje de control de datos (DCL)](#lenguaje-de-control-de-datos-dcl)
    + [Leguaje de control de transacciones (TCL)](#leguaje-de-control-de-transacciones-tcl)
    + [Other Querys](#others-query)
1. [Database constraints](#database-contrainsts)
1. [Crear y Eliminar una Bases de Datos](#crear-y-eliminar-una-base-de-datos)
1. [Insertar multiples registros a una tabla](#insertar-multiples-registros-a-una-tabla)
1. [Extraer datos del campo de una tabla en una columna de otra tabla](#extraer-datos-del-campo-de-una-tabla-en-una-columna-de-otra-tabla)
1. [Actualizar datos de una tabla](#actualizar-datos-de-una-tabla)
1. [Eliminar registros de una tabla](#eliminar-registros-de-una-tabla)
1. [Ejercicios con operadores aritméticos](#ejercicios-con-operadores-aritméticos)
1. [ORDER BY](#order-by)
1. [WHERE](#where)
1. [SELECT  DISTINCT](#select-distinct)

# Comandos SQL comunes

## Lenguaje de definición de datos (DDL)
|Comando|Sintaxis|
|---|---|
|CREATE|CREATE TABLE table_name (column_name1 datatype(size), column_name1 datatype(size), column_name1 datatype(size));|
|DROP|DROP TABLE table_name;|
|ALTER|ALTER TABLE table_name ADD (column_name datatype(size));|
|ALTER|ALTER TABLE table_name ADD primary key(column_name);|
|ALTER|ALTER TABLE table_name MODIFY name_field datatype();| 
|ALTER|ALTER TABLE productos CHANGE producto_id id INT;|
|ALTER|ALTER TABLE table_name DROP name_field;|
|TRUNCATE|TRUNCATE TABLE table_name;|
|COMMENT|--Retrieve all data from a table <br> SELECT * FROM table_name;|

[☝️](#temario) 


## Lenguaje de manipulación de datos (DML)

|Comando|Sintaxis|
|---|---|
|SELECT|SELECT * FROM table_name;|
|INSERT|INSERT INTO table_name(column1,column2,column3) VALUES(value1,value2,value3);|
|UPDATE|UPDATE table_name SET column1=value1, column2=value2 WHERE condition;|
|DELETE|DELETE FROM table_name WHERE condition;|

[☝️](#temario) 


## Lenguaje de control de datos (DCL)

|Comando|Sintaxis|
|---|---|
|GRANT|proporciona al usuario de la base de datos los privilegios necesarios que permiten que los usuarios accedan y manipulen la base de datos|
|REVOKE|quita permisos a cualquier usuario|

[☝️](#temario) 


## Leguaje de control de transacciones (TCL)

|Comando|Sintaxis|
|---|---|
|COMMIT|guarda todo el trabajo realizado en la base de datos|
|ROLLBACK|restaura una base de datos al último estado confirmado|

[☝️](#temario) 


## Others query

|Comando|Proposito|
|---|---|
|SHOW columns FROM table_name;|Describe los campos y tipos de datos de una tabla|
|mysql --version|Muestra la versión instalada de Mysql|

[☝️](#temario) 


# Database contrainsts
Permite garantizar la fiabilidad y precisión de los datos en la base de datos, debe delimitar el tipo de datos que se puede ingresar en la tabla de base datos. Si la base de datos determina una infracción entre restricción y las operaciones de datos, interrumpe estas operaciones.  Un ejemplo puede ser insertar o cargar datos no validos.

Dos restricciones en base de datos pueden ser NOT NULL y DEFAULT.

## Restricción NOT NULL

Se usa para garantizar que los campos siempre esten completo y nunca en blanco. 

Ejemplo:

```
CREATE TABLE Customer (
    customer_id int NOT NULL,
    customer_name varchar(255) NOT NULL
);
```

## Restricción DEFAULT

Significa que si no se insertan un dato en un campo, la base de datos asigna un valor por defecto a ese campo.

```
CREATE TABLE Player (
    name varchar(50) NOT NULL,
    city varchar(30) DEFAULT "Colombia"
);
```

[☝️](#temario) 


# CREAR Y ELIMINAR UNA BASE DE DATOS

A continuación se presentan las sitaxis para crear y eliminar una base de datos.

## Crear una base de datos

`CREATE DATABASE name_database;`

## Eliminar una base de datos

`DROP DATABASE name_database;`

# INSERTAR MULTIPLES REGISTROS A UNA TABLA

```
INSERT INTO name_table (field1, field2, field3) 
    VALUES 
    (value1, value2, value3),
    (value1, value2, value3),
    (value1, value2, value3);
```

Ejemplo:

```
INSERT INTO students (id, nombre, email, edad, pais, nacionalidad) 
VALUES
(1, 'Tom', 'tom@mail.com', 13, 'Argentina', 'argentino'),
(2, 'Lisa', 'lisa@mail.com', 15, 'Mexico', 'Mexicana'),
(3, 'Peter', 'peter@mail.com', 12, 'Venezuela', 'Venezolano');
```

[☝️](#temario) 


# Extraer datos del campo de una tabla en una columna de otra tabla

Sintaxis
```
INSERT INTO target_tbl (column_name)
SELECT column_name
FROM source_tbl;
```

[☝️](#temario) 


# Actualizar datos de una tabla

Sintaxis
```
UPDATE tabla set campo1 = 'algún dato', campo2 = 'otro dato' WHERE 'campo_clave' = 'el_parametro'; 
```

Ejemplo:
```
UPDATE studen_tbl set home_address = 'Dg 4b # 7A-45 Sorvasquez Street', contact_number = '573051234567' WHERE ID = 3; 
```

Actualizar con dos condiciones:
```
UPDATE studen_tbl set home_address = 'Buenavista', college_address = 'Torre III' WHERE ID = 1 OR ID = 3; 
```
En el ejemplo el OR permite afectar dos registros de la misma tabla. También vemos que es posible actualizar dos campos al mismo tiempo.

[☝️](#temario)


# Eliminar registros de una tabla

Sintaxis
```
DELETE FROM table WHERE field = 'value' -- The field and his value  is the condiction
```
También es posible eliminar varios registros si varios registros tienen en común un mismo dato en un campo.

La siguiente clausula es peligrosa porque elimina todos los registros en una tabla

🙀
Sintaxis
```
DELETE FROM table
```

[☝️](#temario)


# Ejercicios con operadores aritméticos

## Suma

```
mysql> select * from students;
+----+--------+----------------+------+-----------+--------------+---------+---------+
| id | nombre | email          | edad | pais      | nacionalidad | saldo   | interes |
+----+--------+----------------+------+-----------+--------------+---------+---------+
|  1 | Tom    | tom@mail.com   |   13 | Argentina | argentino    | 1000000 |       4 |
|  2 | Lisa   | lisa@mail.com  |   15 | Mexico    | Mexicana     | 1000000 |       4 |
|  3 | Peter  | peter@mail.com |   12 | Venezuela | Venezolano   | 1000000 |       4 |
+----+--------+----------------+------+-----------+--------------+---------+---------+
3 rows in set (0,00 sec)

mysql> select (saldo + 300000) from students;
+------------------+
| (saldo + 300000) |
+------------------+
|          1300000 |
|          1300000 |
|          1300000 |
+------------------+
3 rows in set (0,01 sec)
```

```
mysql> UPDATE students SET saldo = 1050000 where nacionalidad = 'Venezolano';
Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from students;
+----+--------+----------------+------+-----------+--------------+---------+---------+
| id | nombre | email          | edad | pais      | nacionalidad | saldo   | interes |
+----+--------+----------------+------+-----------+--------------+---------+---------+
|  1 | Tom    | tom@mail.com   |   13 | Argentina | argentino    | 1000000 |       4 |
|  2 | Lisa   | lisa@mail.com  |   15 | Mexico    | Mexicana     | 1000000 |       4 |
|  3 | Peter  | peter@mail.com |   12 | Venezuela | Venezolano   | 1050000 |       4 |
+----+--------+----------------+------+-----------+--------------+---------+---------+
3 rows in set (0,00 sec)

mysql> select * from students where saldo + 50000 = 1100000;
+----+--------+----------------+------+-----------+--------------+---------+---------+
| id | nombre | email          | edad | pais      | nacionalidad | saldo   | interes |
+----+--------+----------------+------+-----------+--------------+---------+---------+
|  3 | Peter  | peter@mail.com |   12 | Venezuela | Venezolano   | 1050000 |       4 |
+----+--------+----------------+------+-----------+--------------+---------+---------+
1 row in set (0,00 sec)
```

## Resta

```
mysql> ALTER TABLE students ADD prestamos float(9,2);
Query OK, 0 rows affected, 1 warning (0,03 sec)
Records: 0  Duplicates: 0  Warnings: 1

mysql> UPDATE students SET prestamos = 200000 WHERE id = 1 or id = 2 or id = 3;
Query OK, 3 rows affected (0,01 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> SELECT nombre, saldo - prestamos FROM students;
+--------+-------------------+
| nombre | saldo - prestamos |
+--------+-------------------+
| Tom    |         800000.00 |
| Lisa   |         800000.00 |
| Peter  |         850000.00 |
+--------+-------------------+
3 rows in set (0,00 sec)
```

Otro ejemplo de restas esta vez en la clausula WHERE

```
mysql> SELECT nombre, nacionalidad FROM students WHERE saldo - prestamos = 800000;
+--------+--------------+
| nombre | nacionalidad |
+--------+--------------+
| Tom    | argentino    |
| Lisa   | Mexicana     |
+--------+--------------+
2 rows in set (0,00 sec)
```

## Multiplicación y División

En este ejemplo estoy agregando dos campos numéricos a la tabla students. Luego a través de un select estoy generando el 4% del saldo de cada estudiante que figura en la tabla.

```
mysql> UPDATE students SET saldo = 1000000, interes = 3.5 WHERE id = 1 or id = 2 or id = 3;
Query OK, 3 rows affected, 3 warnings (0,02 sec)
Rows matched: 3  Changed: 3  Warnings: 3

mysql> select * from students;
+----+--------+----------------+------+-----------+--------------+---------+---------+
| id | nombre | email          | edad | pais      | nacionalidad | saldo   | interes |
+----+--------+----------------+------+-----------+--------------+---------+---------+
|  1 | Tom    | tom@mail.com   |   13 | Argentina | argentino    | 1000000 |       4 |
|  2 | Lisa   | lisa@mail.com  |   15 | Mexico    | Mexicana     | 1000000 |       4 |
|  3 | Peter  | peter@mail.com |   12 | Venezuela | Venezolano   | 1000000 |       4 |
+----+--------+----------------+------+-----------+--------------+---------+---------+
3 rows in set (0,00 sec)

mysql> SELECT (saldo * interes)/100 FROM students;
+-----------------------+
| (saldo * interes)/100 |
+-----------------------+
|            40000.0000 |
|            40000.0000 |
|            40000.0000 |
+-----------------------+
3 rows in set (0,00 sec)
```

## Modulo %

```
mysql> ALTER TABLE students ADD días INT AFTER saldo;
Query OK, 0 rows affected (0,02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe students;
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| id           | int           | NO   |     | NULL    |       |
| nombre       | varchar(30)   | YES  |     | NULL    |       |
| email        | varchar(50)   | YES  |     | NULL    |       |
| edad         | int           | YES  |     | NULL    |       |
| pais         | varchar(50)   | YES  |     | NULL    |       |
| nacionalidad | varchar(100)  | YES  |     | NULL    |       |
| saldo        | decimal(10,0) | YES  |     | NULL    |       |
| días         | int           | YES  |     | NULL    |       |
| interes      | decimal(10,0) | YES  |     | NULL    |       |
| prestamos    | float(9,2)    | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
10 rows in set (0,01 sec)

mysql> UPDATE students SET días = 2 WHERE nombre = 'Tom' or nombre = 'Lisa';
Query OK, 2 rows affected (0,01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> UPDATE students SET días = 3 WHERE nombre = 'Peter';
Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT nombre, saldo,días FROM  students;
+--------+---------+-------+
| nombre | saldo   | días  |
+--------+---------+-------+
| Tom    | 1000000 |     2 |
| Lisa   | 1000000 |     2 |
| Peter  | 1050000 |     3 |
+--------+---------+-------+
3 rows in set (0,00 sec)

mysql> SELECT nombre, saldo % días AS 'sin resto' FROM students WHERE saldo % días = 0;
+--------+-----------+
| nombre | sin resto |
+--------+-----------+
| Tom    |         0 |
| Lisa   |         0 |
| Peter  |         0 |
+--------+-----------+
3 rows in set (0,00 sec)
```
[☝️](#temario)


# ORDER BY

Sintaxis:

```
SELECT column_1, column_2, column_3...
FROM table_name
ORDER BY column_name ASC; 
```

```
SELECT column_1, column_2, column_3...
FROM table_name
ORDER BY column_name DESC; 
```

```
SELECT column_1, column_2
FROM table_name
ORDER BY column1_name ASC, column2_name DESC; 
```

```
SELECT *
FROM table_name
ORDER BY column1_name ASC, column2_name ASC|DESC; 
```
El  ASC|DESC en el último select significa que se puede usar ASC o DESC.

## Practicas

Ejecuntando una clausula ORDER BY sencilla

```
mysql> SELECT * FROM accounts
    -> ;
+------+----------------+
| id   | email          |
+------+----------------+
|    1 | NULL           |
|    2 | NULL           |
|    3 | NULL           |
| NULL | tom@mail.com   |
| NULL | lisa@mail.com  |
| NULL | peter@mail.com |
|    4 | NULL           |
|    5 | NULL           |
|    6 | NULL           |
| NULL | tom@mail.com   |
| NULL | lisa@mail.com  |
| NULL | peter@mail.com |
+------+----------------+
12 rows in set (0,01 sec)

mysql> SELECT email FROM accounts ORDER BY email;
+----------------+
| email          |
+----------------+
| NULL           |
| NULL           |
| NULL           |
| NULL           |
| NULL           |
| NULL           |
| lisa@mail.com  |
| lisa@mail.com  |
| peter@mail.com |
| peter@mail.com |
| tom@mail.com   |
| tom@mail.com   |
+----------------+
12 rows in set (0,00 sec)

```

Mostrando registros en orden descendente 'DESC' por el campo 'saldo'

```
mysql> SELECT * FROM students;
+----+--------+----------------+------+-----------+--------------+---------+-------+---------+-----------+
| id | nombre | email          | edad | pais      | nacionalidad | saldo   | días  | interes | prestamos |
+----+--------+----------------+------+-----------+--------------+---------+-------+---------+-----------+
|  1 | Tom    | tom@mail.com   |   13 | Argentina | argentino    | 1000000 |     2 |       4 | 200000.00 |
|  2 | Lisa   | lisa@mail.com  |   15 | Mexico    | Mexicana     | 1000000 |     2 |       4 | 200000.00 |
|  3 | Peter  | peter@mail.com |   12 | Venezuela | Venezolano   | 1050000 |     3 |       4 | 200000.00 |
+----+--------+----------------+------+-----------+--------------+---------+-------+---------+-----------+
3 rows in set (0,01 sec)

mysql> SELECT nombre, edad, nacionalidad, días, saldo FROM students ORDER BY saldo DESC;
+--------+------+--------------+-------+---------+
| nombre | edad | nacionalidad | días  | saldo   |
+--------+------+--------------+-------+---------+
| Peter  |   12 | Venezolano   |     3 | 1050000 |
| Tom    |   13 | argentino    |     2 | 1000000 |
| Lisa   |   15 | Mexicana     |     2 | 1000000 |
+--------+------+--------------+-------+---------+
3 rows in set (0,00 sec)
```

# WHERE

## BETWEEN

Filtra registros dentro de un rango numérico, tiempo o fecha.

Ejemplos:

```
SELECT id, nombre, apellido, salario FROM empleados WHERE salario BETWEEN 4000 AND 5000;
```

```
SELECT id, nombre, apellido, fecha_nacimiento FROM empleados WHERE fecha_nacimiento BETWEEN '1986-01-01' AND '1997-12-31';
```

```
SELECT id, nombre, apellido, edad FROM empleados WHERE edad BETWEEN 20 AND 30;
```


## LIKE
Especifica patrones dentro de un criterio.

```
SELECT nombre, apellido, departamento FROM empleados WHERE departamento LIKE '%li%';

+----------+----------+--------------+
| nombre   | apellido | departamento |
+----------+----------+--------------+
| Carlos   | Perez    | Contabilidad |
| Marta    | Sanchez  | Contabilidad |
| Diego    | Suarez   | Contabilidad |
| Ricardo  | Mendoza  | Contabilidad |
| Patricia | Rivera   | Contabilidad |
| Alberto  | Romero   | Contabilidad |
| Felipe   | Aguilar  | Contabilidad |
| Natalia  | Herrera  | Contabilidad |
+----------+----------+--------------+
```

```
SELECT nombre, apellido, departamento FROM empleados WHERE departamento LIKE 'Ma%';

+-----------+-----------+--------------+
| nombre    | apellido  | departamento |
+-----------+-----------+--------------+
| Ana       | Lopez     | Marketing    |
| Luis      | Castillo  | Marketing    |
| Daniel    | Torres    | Marketing    |
| Carolina  | Peña      | Marketing    |
| Isabel    | Rojas     | Marketing    |
| Rodrigo   | Velasquez | Marketing    |
| Mariana   | Diaz      | Marketing    |
| Gabriela  | Mendez    | Marketing    |
| Valentina | Serrano   | Marketing    |
+-----------+-----------+--------------+
```

```
SELECT nombre, apellido FROM empleados WHERE apellido LIKE '%ez';
+----------+-----------+
| nombre   | apellido  |
+----------+-----------+
| Carlos   | Perez     |
| Ana      | Lopez     |
| Pedro    | Martinez  |
| Laura    | Rodriguez |
| Jorge    | Ramirez   |
| Marta    | Sanchez   |
| Sofia    | Gutierrez |
| Elena    | Jimenez   |
| Diego    | Suarez    |
| Jose     | Alvarez   |
| Cesar    | Bermudez  |
| Rodrigo  | Velasquez |
| Oscar    | Perez     |
| Raul     | Ramirez   |
| Gabriela | Mendez    |
| Sara     | Gonzalez  |
| Manuel   | Lopez     |
| Lucia    | Gomez     |
+----------+-----------+
```

## IN
Especifica multiples posibles valores para una columna. (Ver min 7 del video)

```
SELECT nombre, apellido, departamento FROM empleados WHERE departamento IN ('Soporte','Desarrollo');

+----------+-----------+--------------+
| nombre   | apellido  | departamento |
+----------+-----------+--------------+
| Pedro    | Martinez  | Desarrollo   |
| Laura    | Rodriguez | Soporte      |
| Sofia    | Gutierrez | Desarrollo   |
| Elena    | Jimenez   | Soporte      |
| Andrea   | Morales   | Soporte      |
| Paola    | Cruz      | Soporte      |
| Fernando | Vargas    | Desarrollo   |
| Gabriel  | Mora      | Desarrollo   |
| Nicolás  | Rios      | Soporte      |
| Hugo     | Mejia     | Soporte      |
| Cesar    | Bermudez  | Desarrollo   |
| Luis     | Salazar   | Soporte      |
| Mauricio | Ferrer    | Desarrollo   |
| Silvia   | Carrillo  | Soporte      |
| Raul     | Ramirez   | Soporte      |
| Cristina | Reyes     | Desarrollo   |
| Sara     | Gonzalez  | Desarrollo   |
| Manuel   | Lopez     | Soporte      |
| Javier   | Ruiz      | Soporte      |
| Lucia    | Gomez     | Desarrollo   |
+----------+-----------+--------------+
```

## Practicando el WHERE con el UPDATE Y DELETE

### Con UPDATE

Para esta práctica he seleccionado registros especificos de la tabla empleados para despues ver el cambio cuando se ejecute el UPDATE o el DELETE.

```
mysql> SELECT nombre, apellido, salario FROM empleados WHERE salario BETWEEN 3050 and 3600;
+-----------+-----------+---------+
| nombre    | apellido  | salario |
+-----------+-----------+---------+
| Ana       | Lopez     | 3200.50 |
| Elena     | Jimenez   | 3500.00 |
| Daniel    | Torres    | 3200.00 |
| Adriana   | Blanco    | 3500.00 |
| Nicolás   | Rios      | 3200.00 |
| Jose      | Alvarez   | 3400.00 |
| Patricia  | Rivera    | 3100.00 |
| Cesar     | Bermudez  | 3050.00 |
| Rodrigo   | Velasquez | 3600.00 |
| Alberto   | Romero    | 3200.00 |
| Oscar     | Perez     | 3400.00 |
| Cristina  | Reyes     | 3600.00 |
| Valentina | Serrano   | 3150.00 |
| Natalia   | Herrera   | 3500.00 |
| Lucia     | Gomez     | 3300.00 |
+-----------+-----------+---------+
15 rows in set (0,00 sec)
```

Ahora voy a ejecutar un UPDATE haciendo uso del WHERE con el BETWEEN

```
UPDATE empleados SET salario = 5000  WHERE salario BETWEEN 3050 and 3600;

mysql> SELECT nombre, apellido, salario FROM empleados WHERE salario = 5000;

+-----------+-----------+---------+
| nombre    | apellido  | salario |
+-----------+-----------+---------+
| Ana       | Lopez     | 5000.00 |
| Elena     | Jimenez   | 5000.00 |
| Daniel    | Torres    | 5000.00 |
| Adriana   | Blanco    | 5000.00 |
| Nicolás   | Rios      | 5000.00 |
| Jose      | Alvarez   | 5000.00 |
| Patricia  | Rivera    | 5000.00 |
| Cesar     | Bermudez  | 5000.00 |
| Rodrigo   | Velasquez | 5000.00 |
| Alberto   | Romero    | 5000.00 |
| Oscar     | Perez     | 5000.00 |
| Cristina  | Reyes     | 5000.00 |
| Valentina | Serrano   | 5000.00 |
| Natalia   | Herrera   | 5000.00 |
| Lucia     | Gomez     | 5000.00 |
+-----------+-----------+---------+
```

### Con DELETE

```
mysql> SELECT apellido FROM empleados WHERE apellido IN ('campos','mejia','rivera');
+----------+
| apellido |
+----------+
| Rivera   |
| Mejia    |
| Campos   |
+----------+
3 rows in set (0,00 sec)

mysql> DELETE FROM empleados WHERE apellido IN ('campos','mejia','rivera');
Query OK, 3 rows affected (0,01 sec)
```

Los registros dados en la condición fueron eliminados.

```
mysql> SELECT apellido FROM empleados WHERE apellido IN ('campos','mejia','rivera');
Empty set (0,00 sec)
```

### Operador !>

Sintaxis

```
SELECT id, nombre, precio
FROM productos
WHERE precio !> 100;
```

Filtra los registros donde el precio no es mayor que 100, lo que es equivalente a precio <= 100.

### Operador ALL

El operador ALL en MySQL se utiliza para comparar un valor con todos los valores devueltos por un subconjunto (subquery). Devuelve TRUE si la comparación es verdadera para todos los valores en el conjunto de resultados.

Sintaxis

```
SELECT columna
FROM tabla
WHERE valor operador ALL (subquery);
```

# RELACIONES

1. Crear las tablas base (productos y proveedores)

```
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto VARCHAR(50),
    precio DECIMAL(10,2)
    );
Query OK, 0 rows affected (0,10 sec)
```

```
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    proveedor VARCHAR(100)
    );
Query OK, 0 rows affected (0,10 sec)
```

2. Crear la tabla intermedia con las claves foráneas

```
CREATE TABLE productos_proveedores (
    -> producto_id INT,
    -> proveedor_id INT,
    -> PRIMARY KEY (producto_id, proveedor_id),
    -> FOREIGN KEY (producto_id) REFERENCES productos(id)
    -> ON DELETE CASCADE
    -> ON UPDATE CASCADE,
    -> FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
    -> ON DELETE CASCADE
    -> ON UPDATE CASCADE
    -> );
Query OK, 0 rows affected (0,09 sec)
```


> !Note
>
>
> La tabla intermedia no se llena automáticamente. Esta tabla es una tabla de relación (muchos a muchos) que requiere que insertes los datos manualmente para indicar qué productos están relacionados con qué proveedores.

## Insertando datos en tablas base

```
INSERT INTO productos (id, producto, precio) VALUES (1, 'cuaderno', 3000), (2, 'lapiz', 700), (3, 'corrector', 2000), (4, 'regla', 2000), (5, 'curvigrafo', 3500), (6, 'compas', 5000), (7, 'carpeta', 2000);

Resultado:

mysql> SELECT * FROM productos;
+----+------------+---------+
| id | producto   | precio  |
+----+------------+---------+
|  1 | Cuaderno   | 3000.00 |
|  2 | lapiz      |  700.00 |
|  3 | corrector  | 2000.00 |
|  4 | regla      | 2000.00 |
|  5 | curvigrafo | 3500.00 |
|  6 | compas     | 5000.00 |
|  7 | carpeta    | 2000.00 |
+----+------------+---------+
7 rows in set (0,00 sec)

```

```
INSERT INTO proveedores (id, proveedor) VALUES (1, 'A'), (2, 'B'), (3, 'C');

Resultado:

mysql> SELECT * FROM proveedores;
+----+-----------+
| id | proveedor |
+----+-----------+
|  1 | A         |
|  2 | B         |
|  3 | C         |
+----+-----------+
3 rows in set (0,00 sec)
```

## Insertando datos en la tabla intermedia

```
INSERT INTO productos_proveedores (producto_id, proveedor_id) VALUES (1, 3), (3, 1), (6, 2);

Resultado:

mysql> SELECT * FROM productos_proveedores;
+-------------+--------------+
| producto_id | proveedor_id |
+-------------+--------------+
|           3 |            1 |
|           6 |            2 |
|           1 |            3 |
+-------------+--------------+
3 rows in set (0,00 sec)
```

## Consulta de los datos relacionados

```
mysql> SELECT p.producto, pr.proveedor
    -> FROM productos_proveedores pp
    -> JOIN productos p ON pp.producto_id = p.id
    -> JOIN proveedores pr ON pp.proveedor_id = pr.id;
+-----------+-----------+
| producto  | proveedor |
+-----------+-----------+
| corrector | A         |
| compas    | B         |
| Cuaderno  | C         |
+-----------+-----------+
3 rows in set (0,00 sec)
```

## Ejercicio: Alternativa al operador ALL 

Para consultar el proveedor con el producto más costoso, por ejemplo cuando existe una relación entre dos tablas

Se requiere obtener el proveedor con el producto de mayor precio.

```
mysql> SELECT pr.proveedor
    -> FROM proveedores pr
    -> JOIN productos_proveedores pp ON pr.id = pp.proveedor_id
    -> JOIN productos p ON pp.producto_id = p.id
    -> WHERE p.precio = (SELECT MAX(precio) FROM productos);
+-----------+
| proveedor |
+-----------+
| B         |
+-----------+
1 row in set (0,00 sec)
```

En este caso:

    Se busca el producto con el precio máximo (MAX(precio)), y luego se obtiene el proveedor relacionado a ese producto.

Resultado:

Ambas consultas te devolverán el nombre del proveedor que está asociado con el producto más costoso.

## Ejercicio: operador ALL en tablas sin relación

Creando tabla competidores para realizar la prueba

```
mysql> CREATE TABLE competidores (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nombre VARCHAR(50),
    -> precio DECIMAL(10,2)
    -> );
Query OK, 0 rows affected (0,03 sec)

```

Insertando datos en la tabla competidores

```
INSERT INTO competidores (nombre,precio) VALUES 
    ('Papeleria Univerisal',1000),
    ('La Favorita',2900),
    ('Papeleria Malaga',4500);
Query OK, 3 rows affected (0,01 sec)
```

Consultando los datos ingresador

```
mysql> SELECT * FROM competidores;
+----+----------------------+---------+
| id | nombre               | precio  |
+----+----------------------+---------+
|  1 | Papeleria Univerisal | 1000.00 |
|  2 | La Favorita          | 2900.00 |
|  3 | Papeleria Malaga     | 4500.00 |
+----+----------------------+---------+
3 rows in set (0,00 sec)
```

Seleccionando los productos cuyo precio es mayor que todos los precios de los competidores

```
SELECT producto, precio FROM productos WHERE precio > ALL (SELECT precio FROM competidores);
+----------+---------+
| producto | precio  |
+----------+---------+
| compas   | 5000.00 |
+----------+---------+
1 row in set (0,00 sec)
```

Explicación:

    (SELECT precio FROM competidores) devuelve todos los precios de la tabla competidores.
    > ALL se asegura de que el precio del producto sea mayor que todos los precios devueltos por la subconsulta.

En este caso, solo el Producto compas será seleccionado, porque su precio (5000) es mayor que todos los precios en la tabla competidores (1000, 2900, 4500).

Este ejemplo no requiere una relación entre las tablas productos y competidores, ya que solo estás comparando precios entre dos conjuntos de datos independientes.
Resumen:

    Con relación entre tablas: Útil cuando las tablas están vinculadas por una clave externa o alguna otra relación.
    Sin relación entre tablas: Útil cuando simplemente quieres comparar valores entre dos conjuntos de datos independientes.

### Operador AND

Permite la existencia de varias condiciones en la cláusula WHERE de una indicación SQL

```
mysql> SELECT nombre,apellido,salario,departamento FROM empleados WHERE salario BETWEEN 3000 AND 5000;
+-----------+-----------+---------+------------------+
| nombre    | apellido  | salario | departamento     |
+-----------+-----------+---------+------------------+
| Ana       | Lopez     | 5000.00 | Marketing        |
| Pedro     | Martinez  | 4500.00 | Desarrollo       |
| Jorge     | Ramirez   | 3800.00 | Ventas           |
| Sofia     | Gutierrez | 4000.00 | Desarrollo       |
| Elena     | Jimenez   | 5000.00 | Soporte          |
| Miguel    | Romero    | 3800.00 | Ventas           |
| Daniel    | Torres    | 5000.00 | Marketing        |
| Fernando  | Vargas    | 3000.00 | Desarrollo       |
| Camila    | Ortiz     | 4000.00 | Ventas           |
| Adriana   | Blanco    | 5000.00 | Recursos Humanos |
| Nicolás   | Rios      | 5000.00 | Soporte          |
| Jose      | Alvarez   | 5000.00 | Ventas           |
| Cesar     | Bermudez  | 5000.00 | Desarrollo       |
| Rodrigo   | Velasquez | 5000.00 | Marketing        |
| Alberto   | Romero    | 5000.00 | Contabilidad     |
| Oscar     | Perez     | 5000.00 | Recursos Humanos |
| Cristina  | Reyes     | 5000.00 | Desarrollo       |
| Carlos    | Pardo     | 3000.00 | Ventas           |
| Valentina | Serrano   | 5000.00 | Marketing        |
| Natalia   | Herrera   | 5000.00 | Contabilidad     |
| Lucia     | Gomez     | 5000.00 | Desarrollo       |
+-----------+-----------+---------+------------------+
21 rows in set (0,00 sec)

mysql> SELECT nombre,apellido,salario,departamento FROM empleados WHERE nombre = 'Ana' AND salario BETWEEN 3000 AND 5000;
+--------+----------+---------+--------------+
| nombre | apellido | salario | departamento |
+--------+----------+---------+--------------+
| Ana    | Lopez    | 5000.00 | Marketing    |
+--------+----------+---------+--------------+
1 row in set (0,00 sec)
```

### Operador OR

Se utiliza para combinar varias condiciones en la cláusula WHERE de una indicación SQL

Teniendo en cuenta el ejemplo anterior:

```
mysql> SELECT nombre,apellido,salario,departamento FROM empleados WHERE nombre = 'Ana' AND salario BETWEEN 3000 AND 5000;
```

Se va modificar una parte de la sentencia para ver la diferencia, es decir cambiar el primer AND por OR, veremos que los resultados incluyen otros registros. AND a diferencia de OR incluye solo los registros que cumplen todas condiciones.  En la consulta de abajo no solo retorna al empleado con el nombre ANA sino, también todos los empleados que tienen un salario entre 3000 y 5000.

```
mysql> SELECT nombre,apellido,salario,departamento FROM empleados WHERE nombre = 'Ana' OR salario BETWEEN 3000 AND 5000;
+-----------+-----------+---------+------------------+
| nombre    | apellido  | salario | departamento     |
+-----------+-----------+---------+------------------+
| Ana       | Lopez     | 5000.00 | Marketing        |
| Pedro     | Martinez  | 4500.00 | Desarrollo       |
| Jorge     | Ramirez   | 3800.00 | Ventas           |
| Sofia     | Gutierrez | 4000.00 | Desarrollo       |
| Elena     | Jimenez   | 5000.00 | Soporte          |
| Miguel    | Romero    | 3800.00 | Ventas           |
| Daniel    | Torres    | 5000.00 | Marketing        |
| Fernando  | Vargas    | 3000.00 | Desarrollo       |
| Camila    | Ortiz     | 4000.00 | Ventas           |
| Adriana   | Blanco    | 5000.00 | Recursos Humanos |
| Nicolás   | Rios      | 5000.00 | Soporte          |
| Jose      | Alvarez   | 5000.00 | Ventas           |
| Cesar     | Bermudez  | 5000.00 | Desarrollo       |
| Rodrigo   | Velasquez | 5000.00 | Marketing        |
| Alberto   | Romero    | 5000.00 | Contabilidad     |
| Oscar     | Perez     | 5000.00 | Recursos Humanos |
| Cristina  | Reyes     | 5000.00 | Desarrollo       |
| Carlos    | Pardo     | 3000.00 | Ventas           |
| Valentina | Serrano   | 5000.00 | Marketing        |
| Natalia   | Herrera   | 5000.00 | Contabilidad     |
| Lucia     | Gomez     | 5000.00 | Desarrollo       |
+-----------+-----------+---------+------------------+
21 rows in set (0,00 sec)
```

### Operador ANY

El operador ANY se utiliza para comparar un valor con cualquier valor devuelto por una subconsulta. Generalmente se usa con operadores de comparación `=`, `>`, `<`, `>=`, etc. y retorna verdadero si la condición es verdadera para al menos uno de los valores duvueltos por la subconsulta. 

Sintaxis básica:

`valor_operacion ANY (subconsulta)`

`valor_operacion`: Es el valor que se compara con los resultados de la subconsulta.
`subconsulta`: Es una consulta que devuelve un conjunto de valores con los que se comparará el `valor_operacion`.

Ejemplo con ANY:

Se necesita hacer un listado de los productos que tengan precio mayor a por lo menos uno de los precios de los competidores.

```
mysql> SELECT * FROM competidores;
+----+----------------------+---------+
| id | nombre               | precio  |
+----+----------------------+---------+
|  1 | Papeleria Univerisal | 1000.00 |
|  2 | La Favorita          | 2900.00 |
|  3 | Papeleria Malaga     | 4500.00 |
+----+----------------------+---------+
3 rows in set (0,02 sec)
```

```
mysql> SELECT * FROM productos;
+----+------------+---------+
| id | producto   | precio  |
+----+------------+---------+
|  1 | Cuaderno   | 3000.00 |
|  2 | lapiz      |  700.00 |
|  3 | corrector  | 2000.00 |
|  4 | regla      | 2000.00 |
|  5 | curvigrafo | 3500.00 |
|  6 | compas     | 5000.00 |
|  7 | carpeta    | 2000.00 |
+----+------------+---------+
7 rows in set (0,01 sec)
```

```
mysql> SELECT producto FROM productos WHERE precio > ANY (SELECT precio FROM competidores);
```

```
+------------+
| producto   |
+------------+
| Cuaderno   |
| corrector  |
| regla      |
| curvigrafo |
| compas     |
| carpeta    |
+------------+
6 rows in set (0,00 sec)
```

Explicación: 

La consulta `SELECT producto FROM productos` selecciona todos los productos, es decir, 
`WHERE precio > ANY` compara los precios de todos los productos con los precios de los competidores `(SELECT precio FROM competidores);` y si encuentra que el precio de un producto es mayor al precio de un competidor lo selecciona y lo muestra en la consulta. 

lapiz con precio de 700.00 es el único producto cuyo precio NO es mayor a ninguno de los precios de los competidores y por eso no es retornado en la consulta. 

Si queremos comprobar esto hacemos la siguiente consulta:

```
mysql> SELECT producto FROM productos WHERE precio < ALL (SELECT precio FROM competidores);
+----------+
| producto |
+----------+
| lapiz    |
+----------+
1 row in set (0,00 sec)
```

Otro ejemplo: consultar el producto o los productos que tengan el mismo o los mismos precios que el de los competidores.

```
mysql> INSERT INTO competidores (nombre,precio) VALUES ('La Favorita',3500);
Query OK, 1 row affected (0,01 sec)

mysql> SELECT * from competidores;
+----+----------------------+---------+
| id | nombre               | precio  |
+----+----------------------+---------+
|  1 | Papeleria Univerisal | 1000.00 |
|  2 | La Favorita          | 2900.00 |
|  3 | Papeleria Malaga     | 4500.00 |
|  4 | La Favorita          | 3500.00 |
+----+----------------------+---------+
4 rows in set (0,00 sec)

mysql> SELECT producto FROM productos WHERE precio = ANY (SELECT precio FROM competidores);
+------------+
| producto   |
+------------+
| curvigrafo |
+------------+
1 row in set (0,00 sec)

mysql> 
```

### Operador EXIST

El operador `EXIST` en MySQL se utiliza para verificar si una subconsulta devuelve al menos una fila. Si la subconsulta devuelve una o más filas, `EXISTS` retorna `TRUE`. Si la subconsulta no devuelve ninguna fila, entonces retorna `FALSE`.

A diferencia de operadores como `ALL` o `ANY`, `EXISTS` no devuelve valores específicos de subconsulta, solo verifica su existencia.

Sintaxis básica:

```
SELECT columnas
FROM tabla_principal
WHERE EXISTS (subconsulta);
```

### Ejemplos con EXISTS

**Ejemplo 1**: Seleccionar todos los productos que estan asociados con al menos un proveedor en la tabla `productos_proveedores`. 

Verificando el contenido de la tabla `productos_proveedores` para tener presente los `id`.

```
mysql> SELECT * FROM productos_proveedores;
+-------------+--------------+
| producto_id | proveedor_id |
+-------------+--------------+
|           3 |            1 |
|           6 |            2 |
|           1 |            3 |
+-------------+--------------+
3 rows in set (0,01 sec)
```

Verificando el contenido de la tabla `productos` para tener en cuenta el nombre de los productos.

```
mysql> SELECT * FROM productos;
+----+------------+---------+
| id | producto   | precio  |
+----+------------+---------+
|  1 | Cuaderno   | 3000.00 |
|  2 | lapiz      |  700.00 |
|  3 | corrector  | 2000.00 |
|  4 | regla      | 2000.00 |
|  5 | curvigrafo | 3500.00 |
|  6 | compas     | 5000.00 |
|  7 | carpeta    | 2000.00 |
+----+------------+---------+
7 rows in set (0,00 sec)
```

Aquí se consultan los productos existentes en la tabla `productos_proveedores`. Tenga en cuenta que la tabla `productos_proveedores` solo contiene los id de los productos y los id de los proveedores, pero con la siguiente sentencia y a través de la relación entre las tablas `productos` y `proveedores` es posible obtener el nombre de los productos.
  
```
mysql> SELECT p.producto FROM productos p WHERE EXISTS(SELECT 1  FROM productos_proveedores pp WHERE pp.producto_id = p.id );
+-----------+
| producto  |
+-----------+
| Cuaderno  |
| corrector |
| compas    |
+-----------+
3 rows in set (0,00 sec)
```

+ **subconsulta:** Es una consulta que devuelve filas (o no). Si devuelve al menos una fila, `EXIST` será `TRUE`.

---

**Ejemplo 2**: Seleccionar todos los proveedores que estan asociados con al menos un proveedor en la tabla `productos_proveedores`. 


Consultando el contenido de la tabla `proveedores` para tener en cuenta el nombre de los proveedores.

```
mysql> SELECT * FROM proveedores;
+----+-----------+
| id | proveedor |
+----+-----------+
|  1 | A         |
|  2 | B         |
|  3 | C         |
+----+-----------+
3 rows in set (0,01 sec)

```

Consultando los proveedores existentes en la tabla `productos_proveedores`. Tenga en cuenta que la tabla `productos_proveedores` solo contiene los id de los productos y los id de los proveedores, pero con la siguiente sentencia y a través de la relación entre las tablas `productos` y `proveedores` es posible obtener el nombre de los proveedores.

```
mysql> SELECT pr.proveedor FROM proveedores pr WHERE EXISTS(SELECT 1 FROM productos_proveedores pp WHERE pp.proveedor_id = pr.id);
+-----------+
| proveedor |
+-----------+
| A         |
| B         |
| C         |
+-----------+
3 rows in set (0,00 sec)
```

> Note
>
> En SQL, el 1 en la subconsulta SELECT 1 no tiene un significado especial en sí mismo; simplemente es un valor constante que se devuelve. Su propósito principal en este contexto es verificar la existencia de filas que cumplan con la condición especificada en la subconsulta.
>
> El SELECT 1 no significa que se está seleccionando "algo especial". Podría ser cualquier valor constante (por ejemplo, SELECT 0, SELECT 'X', etc.), ya que solo se necesita una expresión válida.
>
> Usar 1 es una práctica común porque es breve y no introduce complejidad. Como el valor devuelto no se usa, seleccionar una constante evita realizar un trabajo innecesario como recuperar datos adicionales.

[☝️](#temario)

# SELECT DISTINCT

Extrae valores distintos de una columna sin incluir los duplicados.

**Ejemplo 1**: Tenemos la tabla estudiantes con valores duplicados en el campo `country`

```
+------------+------------+-----------+------------+-----------+
| student_id | first_name | last_name | dob        | country   |
+------------+------------+-----------+------------+-----------+
|          1 | Levi       | Williams  | 2010-01-03 | Australia |
|          2 | John       | Smith     | 2010-05-20 | Australia |
|          3 | Alira      | Gorrie    | 2010-07-15 | Australia |
|          4 | Carlos     | Ramirez   | 2010-11-03 | USA       |
|          5 | John       | Taylor    | 2020-08-15 | USA       |
|          6 | Meiling    | Zhao      | 2010-10-10 | China     |
|          7 | James      | Wilson    | 2020-05-20 | UK        |
+------------+------------+-----------+------------+-----------+
```

Ahora voy a seleccionar los países con 'SELECT DISTINCT' y veamos el resultado:

```
mysql> SELECT DISTINCT country FROM estudiantes;
+-----------+
| country   |
+-----------+
| Australia |
| USA       |
| China     |
| UK        |
+-----------+
4 rows in set (0,01 sec)
```

> Nota
>
> La salida de la sentencia anterior permite obtener el nombre de los países en la estudiantes sin mostrar valores duplicados. 

**Ejemplo 2**: Ahora usemos la claúsula `SELECT DISTINCT`con una combinación de columnas en la tabla estudiantes. _Pero antes_ vamos a añadir una columna a la misma tabla para hacer este ejercicio.

```
mysql> ALTER TABLE estudiantes ADD COLUMN faculty VARCHAR(50) AFTER dob;
Query OK, 0 rows affected (0,09 sec)
```

Procedemos a actualizar algunos registros:

```
mysql> UPDATE estudiantes SET faculty = 'Science' WHERE student_id = 1 or student_id = 3;
Query OK, 2 rows affected (0,01 sec)

mysql> UPDATE estudiantes SET faculty = 'Engineering' WHERE student_id = 4 or student_id = 5;
Query OK, 2 rows affected (0,00 sec)
```

```
mysql> UPDATE estudiantes SET faculty = 'Healt' WHERE student_id = 6;
Query OK, 1 row affected (0,01 sec)
```

```
mysql> UPDATE estudiantes SET faculty = 'Humanities' WHERE student_id = 7;
Query OK, 1 row affected (0,06 sec)
```

```
+------------+------------+-----------+------------+-------------+-----------+
| student_id | first_name | last_name | dob        | faculty     | country   |
+------------+------------+-----------+------------+-------------+-----------+
|          1 | Levi       | Williams  | 2010-01-03 | Science     | Australia |
|          2 | John       | Smith     | 2010-05-20 | NULL        | Australia |
|          3 | Alira      | Gorrie    | 2010-07-15 | Science     | Australia |
|          4 | Carlos     | Ramirez   | 2010-11-03 | Engineering | USA       |
|          5 | John       | Taylor    | 2020-08-15 | Engineering | USA       |
|          6 | Meiling    | Zhao      | 2010-10-10 | Healt       | China     |
|          7 | James      | Wilson    | 2020-05-20 | Humanities  | UK        |
+------------+------------+-----------+------------+-------------+-----------+
```

Procedemos a realizar la consulta:

```
mysql> SELECT DISTINCT faculty, country FROM estudiantes;
+-------------+-----------+
| faculty     | country   |
+-------------+-----------+
| Science     | Australia |
| NULL        | Australia |
| Engineering | USA       |
| Healt       | China     |
| Humanities  | UK        |
+-------------+-----------+
5 rows in set (0,00 sec)
```

Tenemos que se muestran combinaciones únicas entra faculty y country. Tener presente que valores `NULL` también se consideran valores únicos cuando ejecutamos `SELECT DISTINCT`

[☝️](#temario)