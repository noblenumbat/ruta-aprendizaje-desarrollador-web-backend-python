# Temario
* [Comandos SQL comunes](#comandos-sql-comunes)
    +[Lenguaje de definición de datos (DDL)](#lenguaje-de-definición-de-datos-ddl)
    +[Lenguaje de manipulación de datos (DML)](#lenguaje-de-manipulación-de-datos-dml)
    +[Lenguaje de control de datos (DCL)](#lenguaje-de-control-de-datos-dcl)
    +[Leguaje de control de transacciones (TCL)](#leguaje-de-control-de-transacciones-tcl)
    +[Other Querys](#others-query)

# Comandos SQL comunes

## Lenguaje de definición de datos (DDL)
|Comando|Sintaxis|
|---|---|
|CREATE|CREATE TABLE table_name (column_name1 datatype(size), column_name1 datatype(size), column_name1 datatype(size));|
|DROP|DROP TABLE table_name;|
|ALTER|ALTER TABLE table_name ADD (column_name datatype(size));|
|ALTER|ALTER TABLE table_name ADD primary key(column_name);|
|ALTER|ALTER TABLE table_name MODIFY <field> datatype();| 
|TRUNCATE|TRUNCATE TABLE table_name;|
|COMMENT|--Retrieve all data from a table <br> SELECT * FROM table_name;|


## Lenguaje de manipulación de datos (DML)

|Comando|Sintaxis|
|---|---|
|SELECT|SELECT * FROM table_name;|
|INSERT|INSERT INTO table_name(column1,column2,column3) VALUES(value1,value2,value3);|
|UPDATE|UPDATE table_name SET column1=value1, column2=value2 WHERE condition;|
|DELETE|DELETE FROM table_name WHERE condition;|


## Lenguaje de control de datos (DCL)

|Comando|Sintaxis|
|---|---|
|GRANT|proporciona al usuario de la base de datos los privilegios necesarios que permiten que los usuarios accedan y manipulen la base de datos|
|REVOKE|quita permisos a cualquier usuario|


## Leguaje de control de transacciones (TCL)

|Comando|Sintaxis|
|---|---|
|COMMIT|guarda todo el trabajo realizado en la base de datos|
|ROLLBACK|restaura una base de datos al último estado confirmado|

## Others query

|Comando|Proposito|
|---|---|
|SHOW columns FROM table_name;|Describe los campos y tipos de datos de una tabla|
|mysql --version|Muestra la versión instalada de Mysql|
