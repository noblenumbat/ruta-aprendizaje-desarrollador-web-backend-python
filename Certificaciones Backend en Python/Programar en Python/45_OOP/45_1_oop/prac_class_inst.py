class House:
    '''
    This is a stub for class representing a house that can be used to created objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House() 
print(house.bathrooms) # 2
print(house.num_rooms) # 5
print(House.num_rooms) # 5
house.num_rooms = 7 # este objeto no cambia la propiedad de la clase
print(house.num_rooms) # 7
print(House.num_rooms) # 5 por eso aquí imprime 5
House.num_rooms = 9 # el cambio que se hizo en la clase afecta a todas las instancias que no tengan una variable propia de instancia num_rooms
print(house.num_rooms) # 7  Esto imprime 7 porque house tiene su propia variable de instancia num_rooms con el valor 7. El cambio en la variable de clase num_rooms no afecta la variable de instancia num_rooms en house.

other_house = House()
print(other_house.num_rooms) # 9