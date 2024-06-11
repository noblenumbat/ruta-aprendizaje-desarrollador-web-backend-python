favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# Loop while

# count = 0

# while count < len(favorites):
#     print('I like this desert: ',favorites[count])
#     count += 1



# Loop for

# Function enumerate() permite recorrer una secuencia sin usar un contador

for idx, item in enumerate(favorites):
    print(idx, item)


# for item in favorites:
#     print('My favorite desert is: ',item)


# Function range() permite imprimir un loop determinado número de veces

for i in range(7):
    print('Time',i)

# for i in range(10): 
#     print('Looping ..',i)

# str = 'Looping'

# for item in str:
#     print(item)

