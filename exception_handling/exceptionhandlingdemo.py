try:
    nr = int(input('ENTER A NUMERATOR NUMBER   : '))
    dr = int(input('ENTER A DENOMINATOR NUMBER : '))

    result = nr / dr
    print(f'DIVISION IS - {result}')
except:
    print('ERROR - You can not divide any number by zero.')