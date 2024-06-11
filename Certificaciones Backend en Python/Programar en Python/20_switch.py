color_shirt = 'green'

match color_shirt:
    case 'green':
        print('The shirt is beautiful') 
    case 'yellow':
        print('The shirt is wonderful')
    case 'blue':
        print('The shirt is nice')
    case _:
        print('No comments')

http_status = 404

match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad Request')
    case 404:
        print('Not Found')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknow')

""" loyalty_customer = False
total_bill = 80

if loyalty_customer and total_bill > 100:
    # give 20% discount
    total_bill = total_bill - (float(total_bill / 100) * 20)

elif total_bill > 100:
    # give 10% discount
    total_bill = total_bill - (float(total_bill / 100) * 10)

else:
    # no discount, 5% charge applied
    total_bill = total_bill + (float(total_bill / 100) * 5)
    print('Sorry no discunt, ' +  '5% ' + 'charge aplied' )
 
print('Total bill: ', float(total_bill)) """



# Light is currently off
""" current = False

if current:
    current = False
    print('Turning light off')

else:
    current = True
    print('Turning light on') """



