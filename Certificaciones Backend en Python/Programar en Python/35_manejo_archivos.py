#manejo de archivos en Python

#there are two function: 'open' and 'close'
# open() allow reading wrinting creating

#SINTAXIS
#open(<FILE_NAME> <FILE_LOCATION>, <MODE>) accept two arguments
 
#<MODE> specific action as : reading, writing, creatig
#also specific if the output is in text or binary

#Mode sets

#Mode = 'r'
#open and read (text format)

#Mode = 'rb'
#open and read (binary format)

#Mode = 'r+'
#open for reading and writing

#Mode = 'w' sobreescribe
#open for writing

#open(<FILE_NAME>, 'a') 
#open for editing or appending data

# -----------------------------------------------------------------

#close() closed the conexion with the open files

#SINTAXIS
#close() No arguments

# -----------------------------------------------------------------
#other way of open and close files on Python

#with open('testing.txt', 'r') as file
# cierra el archivo automáticamente

# -----------------------------------------------------------------
# difference between text and binary format

#text format: is friedly
#binary:  is compact, better performance, the human cannot read it
#to configure the managenmet of files binary you need to pass the letter 'b'
#example:

#open(<FILE_NAME>, rb)
#open(<FILE_NAME>, rb+)
#open(<FILE_NAME>, wb)
#open(<FILE_NAME>, ab)

  