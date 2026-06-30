demo_list = []
try:
    nr = int(input('ENTER A NUMERATOR NUMBER   : '))
    dr = int(input('ENTER A DENOMINATOR NUMBER : '))

    result = nr / dr
    print(f'DIVISION IS - {result}')

    demo_list = [60,75,88,91,97]
    print(demo_list[55])
except ZeroDivisionError:
    print('ERROR - You can not divide any number by zero.')
except ValueError:
    print('ERROR - INVALID INPUT. PLEASE ENTER ONLY NUMBERS.')
except:
    print('ERROR - UNEXPECTED ERROR')
finally:
    demo_list.clear()
    print('All done.')
print('THE PROGRAM IS ENDING HERE.')