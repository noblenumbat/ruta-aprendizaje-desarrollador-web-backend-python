from math import pi
print(pi)

names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)

numero = 1.0
print(int(numero))



for x in range(1, 4):
    # print(int((str((float(x)))))) # No se puede convertir un str a un int
    pass

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)

print("---")

def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)

str = 'Pomodoro'
for l in str:
    if l == 'o':
        new = str.split()
        print(new, end=", ")

# ['Pomodoro'], ['Pomodoro'], ['Pomodoro'], ['Pomodoro'],

# Para aplicar .split() a un string se debe asignar el resultado a una nueva variable, de lo contrario genera error.

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()

num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)

class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a()) # Function inside A, se trata de herencia multiple y despues de C sigue A (el orden importa aquí)