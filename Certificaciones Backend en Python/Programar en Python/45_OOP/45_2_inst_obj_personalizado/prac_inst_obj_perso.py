# class Recipe():
""" 
    cls no es una palabra clave sino, una convención, actua como marcador de posición para pasar la 
    clase como su primer argumento, que se utilizará para crear un nuevo objeto vacío. 
    Este primer método permite crear y devolver un nuevo objeto vacío
    """
    # def __new__(cls) -> Self: 
    #     pass

    # def __init__(self) -> None:
    #     pass
                
""" 
    el segundo método init es similar a lo que se conoce como un constructor en otros lenguajes de programación,
    toma los objetos creados utilizando el nuevo método con otros argumentos para inicializar el nuevo objeto que se 
    esta creando.
    El método de entrada toma el nuevo objeto como su primer argumento. La palabra "self" aquí es otra convención. 
    No tiene ninguna función en sí, pero sirve como un marcador de posición para la autoreferencia por el objeto de instancia.
    """

# --------------------------------------------------------------------------------------------------------

class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")
        
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)
print(pizza.contents())