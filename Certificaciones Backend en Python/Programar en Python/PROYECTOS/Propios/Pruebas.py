scanner_pool = []

""" scanner_pool.append([  
    "   _____ " ,
    "  /    / " , 
    " /____/  "  
   ])   """

scanner_pool.append([  
    " 1 " ,
    " 2 " , 
    " 3 "  
   ])  

scanner_pool.append([  
    " 4 " ,
    " 5 " , 
    " 6 "  
   ])  

scanner_pool.append([  
    " 7 " ,
    " 8 " , 
    " 9 "  
   ])  

print(scanner_pool)

num_lineas = len(scanner_pool[0])

print(num_lineas)

for i in range(num_lineas):
        for figure in scanner_pool:
            print(figure[i], end = ' ') # Imprimir cada línea de cada figura en la misma fila
        print() # Salto de fila despues de imprimir todas las figuras de una fila