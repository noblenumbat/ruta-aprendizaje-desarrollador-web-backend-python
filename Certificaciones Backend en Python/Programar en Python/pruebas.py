# a = [[96],[69]]
# conversion = "".join(list(map(str,a)))
# print(conversion)
# # sin join 
# #['[96]', '[69]']

# # con join
# # [96][69]

# list = ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']

# for employee in list:
#     reemplazado = employee.replace(" ","_")
#     print(reemplazado)

#list = [ function() for <item> in <list> ]

# list = [item.replace(" ","_") for item in list]

# print(list)

# output:
# ['John_Kitchen', 'Paul_House_Floor', 'Sarah_Management', 'Lisa_Cold_Storage', 'Ryan_Inventory_Mgmt', 'Gill_Cashier']

# ---------------------------------------------------------------------------------------------------

# employee_list = [
#    {"id": 12345, "name": "John", "department": "Kitchen"},
#    {"id": 12456, "name": "Paul", "department": "House Floor"},
#    {"id": 12478, "name": "Sarah", "department": "Management"},
#    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
#    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
#    {"id": 12419, "name": "Gill", "department": "Cashier"}
# ]

# employee_dict = {employee["name"][0]: employee["id"] for employee in employee_list}

# print(employee_dict)

# --------------------------------------------------------------------------------------------------

# def sum(n):
#    if n == 1:
#        return 0
#    return n + sum(n-1)

# a = sum(5)
# print(a)

# -------------------------------------------------------------------------------------------------

# numbers = [15, 30, 47, 82, 95]
# def lesser(numbers):
#    return numbers < 50

# small = list(filter(lesser, numbers))
# print(small)

# -------------------------------------------------------------------------------------------------

