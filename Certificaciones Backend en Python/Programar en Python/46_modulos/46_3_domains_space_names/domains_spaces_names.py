# CODE #1
""" a = "alpha"

print(id(a)) """

# CODE #2

""" country = "USA"
print("Country name: " + country)
print(globals())
print("-------------")

def b():
    country = "Germany"
    print("Country name: " + country)
    print(locals())

b()
print("Country name: " + country) """

# salida del código

""" Country name: USA
{'__name__': '__main__', '__doc__': ' a = "alpha"\n\nprint(id(a)) ', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7a7a1c3c45f0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/jonathan/Documentos/Cursos/Certificaciones Backend en Python/Programar en Python/46_modulos/46_3_domains_space_names/domains_spaces_names.py', '__cached__': None, 'country': 'USA'}
-------------
Country name: Germany
{'country': 'Germany'}
Country name: USA """

# CODE #3

# Ejemplo: para entender la idea de ámbito para un atributo.

def d():
    animal = "elephant"
    def e():
        nonlocal animal 
        animal = "giraffe"
        print("Inside nested function: " + animal) 

    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal) 

animal = "camel"
d()
print("Global animal: " + animal) 
