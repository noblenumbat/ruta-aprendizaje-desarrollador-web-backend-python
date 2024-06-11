# SCOPES            : El propósito del alcance es proteger la variable, 
                    # para que no se modifique por otras partes del código.
# -------------------------------------------------------------------------
# Built-in Scope    : palabras clave reservad, como 'print' y 'def' 
                    # cubre todo el lenguaje de Python (alcances internos y externos en clases de funciones)
# Global Scope      : son accesibles desde cualquier parte del código.
# Enclosing Scope   : desde fn2() puedo acceder a enclosed_v
                    # la función más interna tiene acceso a casi todo desde el exterior, también
                    # puede acceder a la variable global
                    # no se puede acceder acceder desde el Global Scope
# Local Scope       : no puedo acceder a una variable local desde el global scope.  

#global scope
my_global = 10

def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
    fn2() # se invoca a la función 

fn1()

#print('Cant access local', local_v) 

# --------------------------------------------------------------------
#other example
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    #print(double)

    return total
get_total(5,5)