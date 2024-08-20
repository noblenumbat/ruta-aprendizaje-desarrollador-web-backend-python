# Python module to import

print("File two __name__ is set to: {}" . format(__name__))

def function_three():
    print("Function three is excecuted")

def function_four():
    print("Function four is executed")

if __name__ == '__main__':
    print("File two excecuted when ran directly")
else:
    print("File two excecuted when imported")