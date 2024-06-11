class A:
    pass

class B(A):
    pass

class C(B):
    pass 

print(C.mro())

# output:

# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(help(C))

""" Help on class C in module __main__:

class C(B)
 |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
 |
 |  Data descriptors inherited from A:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object """