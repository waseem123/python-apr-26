class Pen:
    brand = 'Cello'
    price = 10
    pen_type = 'Gel Pen'
    pen_ink = 'Blue'


p1 = Pen()
p1.brand = 'Cello'
p1.price = 10
p1.pen_type = 'Gel Pen'
p1.pen_ink = 'Blue'

p2 = Pen()
p2.brand = 'Raynolds'
p2.price = 20
p2.pen_type = 'Ball Pen'
p2.pen_ink = 'Black'

print(f'BRAND - {p1.brand}')
print(f'PRICE - {p1.price}')
print(f'TYPE  - {p1.pen_type}')
print(f'INK   - {p1.pen_ink}')
print('______________________________')


print(f'BRAND - {p2.brand}')
print(f'PRICE - {p2.price}')
print(f'TYPE  - {p2.pen_type}')
print(f'INK   - {p2.pen_ink}')
