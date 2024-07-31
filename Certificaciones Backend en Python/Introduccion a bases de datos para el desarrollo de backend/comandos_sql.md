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
