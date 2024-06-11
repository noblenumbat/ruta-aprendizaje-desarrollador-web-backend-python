# Se asigna un mismo valor a todas las variables
a = b = c = 10

print(a)
print(b)
print(c)

# Se asignan valores a las variables en su respectivo orden

d,e,f = 3,7,9

print(d)
print(e)
print(f)

# ValueError: not enough values to unpack (expected 3, got 2)

x,y,z = 2,1
print(x)
print(y)
print(z) 