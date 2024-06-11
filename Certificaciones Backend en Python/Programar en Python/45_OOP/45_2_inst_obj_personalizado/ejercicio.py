class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index) # Escriba una sentencia "print" mediante la función print() y pase la variable "class" accediendo a ella. 
        print(philosopher + " escribió el libro: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")