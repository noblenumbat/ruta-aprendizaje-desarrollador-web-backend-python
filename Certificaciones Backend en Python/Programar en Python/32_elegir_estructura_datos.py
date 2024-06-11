#¿Qué estructura de datos elegir?
#Tener en cuenta: tamaño, velocidad, rendimiento

#Ejemplo: lista de empleados

# employee_list = [{'id':238732 , 'name': 'Jon' , 'department:': 'Support IT' },{'id': 244499 , 'name': 'Jhen' , 'department:': 'civil build'}]

# def get_employee(id):
#     for employee in employee_list:
#         if employee['id'] == id: 
#             return(employee)

# print(get_employee(244499))

#{'id': 244499, 'name': 'Jhen', 'department:': 'civil build'}

# El código se ejecuta bien y devolverá al usuario Jhen, ya que su ID, 244499, coincide. El desafío aparece cuando la lista se hace más grande. 

# En lugar de dos empleados, puede tener 2,000 o incluso 20,000. El código tendrá que iterar sobre la lista secuencialmente hasta que el número coincida. 

# Se podría optimizar el código para dividir la búsqueda, pero incluso con esto, seguiría teniendo un rendimiento inferior al de otras estructuras de datos, como el diccionario.

#ejemplo:
employee_dic = {
    238732:{'id':238732, 
    'name': 'Jon', 
    'department:': 'Support IT' 
    },
    244499:{
    'id': 244499, 
    'name': 'Jhen', 
    'department:': 'civil build'
    }
}

def get_employee_from_dic(id):
    return employee_dic[id]

print(get_employee_from_dic(238732))
#{'id': 238732, 'name': 'Jon', 'department:': 'Support IT'}

#Ya no se necesita iterar sobre la lista para localizarlos. Si la lista se amplía a un tamaño mucho mayor,
#el tiempo de búsqueda para encontrar al empleado siguie siendo el mismo.


