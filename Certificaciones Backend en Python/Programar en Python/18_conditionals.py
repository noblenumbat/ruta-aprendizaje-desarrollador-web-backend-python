total_bill = 210
discount1 = 10
discount2 = 15

if total_bill > 99 and total_bill < 200:
    print('Congratulations! ha obtenido un descuento de' , discount1 , 'en su compra')
    print('El total de su compra es: ' + str(total_bill - discount1))
elif total_bill > 200 :
    print('Congratulations! ha obtenido un descuento de ' + str(discount2) + ' en su compra')
    print('El total de su compra es: ' + str(total_bill - discount2))
else :
    print('El total de su compra es: ' + str(total_bill))

    # Practicar formatos directos (input.py) y aprender dos funciones nuevas