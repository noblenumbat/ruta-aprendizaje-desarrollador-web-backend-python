# Temario
1. [Comandos SQL comunes](#comandos-sql-comunes)
    + [Lenguaje de definición de datos (DDL)](#lenguaje-de-definición-de-datos-ddl)
    + [Lenguaje de manipulación de datos (DML)](#lenguaje-de-manipulación-de-datos-dml)
    + [Lenguaje de control de datos (DCL)](#lenguaje-de-control-de-datos-dcl)
    + [Leguaje de control de transacciones (TCL)](#leguaje-de-control-de-transacciones-tcl)
    + [Other Querys](#others-query)
1. [Database constraints](#database-contrainsts)
1. [Crear y Eliminar una Bases de Datos](#crear-y-eliminar-una-base-de-datos)
1. [Extraer datos del campo de una tabla en una columna de otra tabla](#extraer-datos-del-campo-de-una-tabla-en-una-columna-de-otra-tabla)
1. [Actualizar datos de una tabla](#actualizar-datos-de-una-tabla)
1. [Eliminar registros de una tabla](#eliminar-registros-de-una-tabla)
1. [Ejercicios con operadores aritméticos](#ejercicios-con-operadores-aritméticos)
1. [ORDER BY](#order-by)
1. [WHERE](#where)

# Comandos SQL comunes

## Lenguaje de definición de datos (DDL)
|Comando|Sintaxis|
|---|---|
|CREATE|CREATE TABLE table_name (column_name1 datatype(size), column_name1 datatype(size), column_name1 datatype(size));|
|DROP|DROP TABLE table_name;|
|ALTER|ALTER TABLE table_name ADD (column_name datatype(size));|
|ALTER|ALTER TABLE table_name ADD primary key(column_name);|
|ALTER|ALTER TABLE table_name MODIFY name_field datatype();| 
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
);Browser Preview
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
SELECT +
FROM table_name
ORDER BY column1_name ASC, column2_name ASC|DESC; 
```

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

TAMBIEN PRÁCTICAR SU USO EN UPDATE Y DELETE

[☝️](#temario)