# class MyClass:
#     a = 5
#     print("Hello")

# myc = MyClass() # Hello
# print(MyClass.a) # a
# print(myc.a) # referencia de atributo

# ----------------------------------------

class MyClass:
    a = 5
    def hello(self): # agrego self para poder llamar al método 
        print("Hello world!")

myc = MyClass()
print(myc.a)
print(myc.hello()) # el método

# 5
# Hello world!
# None -> retorna none porque no hay una instrucción return en el método hello.