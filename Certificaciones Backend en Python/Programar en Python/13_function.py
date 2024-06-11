# Making a function


def say_hello():
    return 'Hello!'

print(say_hello())

# The functions are also overwritten
def say_hello1():
    return 'Hello Jhensy' 

print(say_hello1())

def say_hello1():
    return 'Hello duplicado'

print(say_hello1())

# Function with parameter

def say_hello(you):
    return 'Hello ' + you

print(say_hello('Climaco'))