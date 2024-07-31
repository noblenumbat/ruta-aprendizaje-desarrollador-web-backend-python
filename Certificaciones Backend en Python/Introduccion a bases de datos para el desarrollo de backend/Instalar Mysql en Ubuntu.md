# Pasos para instalar Mysql en Ubuntu:

## Instalación:
1. sudo apt update
2. sudo apt upgrade
3. Validar las opciones de Mysql disponibles
   sudo apt-cache search mysql-server
4. sudo apt install mysql-server
5. Confirmar el estado de MySQL
   sudo systemctl status mysql.service
6. Iniciar el servicio en caso de ser necesario
   sudo systemctl start mysql.service
   sudo systemctl enable mysql.service
7. Acceder a MySQL
   sudo mysql
8. Establecer contraseña de root
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'vozco003';
9. exit;


## Asegurar la instalación de MySQL:
1. sudo mysql_secure_installation
2. Escribir la contraseña de root asignada anteriormente
3. En cambiar password para root: No, en las demás opciones Y


## Acceder a MySQL con la contraseña:
1. mysql -u root -p


## Crear y configurar la base de datos:
1. CREATE DATABASE Pruebas;
2. CREATE USER 'jonvzcas'@'localhost' IDENTIFIED BY 'vozco003';
3. GRANT ALL PRIVILEGES ON Pruebas.* TO 'jonvzcas'@'localhost';
4. exit;


## Validación de bases de datos disponibles:
1. mysql -u root -p
2. show databases;
3. exit;
4. sudo apt update


## Instalar utilidades extras:
1. sudo snap install mysql-workbench-community
   Antes se instalaba así: sudo apt install mysql-workbench-community libmysqlclient18`
   
## Ver la instalación
1. mysql --version