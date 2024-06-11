studies = {
    1:{
        'name': 'Jonathan',
        'edad': 39,
        'matricula': 150
    },
    2:{
        'name': 'Climaco',
        'edad': 74,
        'matricula': 130
    }
}

#items = [studies[key]["name"] for key in studies]
#['Jonathan', 'Climaco']

#PASAR DATOS DE UN DICCIONARIO A UNA LISTA

items = [(studies[key]["name"],studies[key]['edad']) for key in studies]
#[('Jonathan', 39), ('Climaco', 74)]

print(items[0])

#SUMAR DATOS DE UN DICCIONARIO
print(sum(studies[key]['matricula'] for key in studies))
