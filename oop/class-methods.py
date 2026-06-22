class Pen:
    pen_brand = ""
    pen_ink = ""
    pen_type = ""
    pen_price = 0

    # setData() method is defined for taking the user input
    # and storing them for various objects
    def setData(self):
        self.pen_brand = input("Enter brand name: ")
        self.pen_ink = input("Enter ink color: ")
        self.pen_type = input("Enter pen type: ")
        self.pen_price = input("Enter pen price: ")

    def getData(this):
        print(f'PEN BRAND - {this.pen_brand}')
        print(f'PEN INK - {this.pen_ink}')
        print(f'PEN TYPE - {this.pen_type}')
        print(f'PEN PRICE - RS. {this.pen_price}')


p2 = Pen()
p3 = Pen()
p4 = Pen()
p1 = Pen()
print(p1)
print(p2)


print('ENTER DATA FOR p2 OBJECT')
p2.setData()
print('ENTER DATA FOR p3 OBJECT')
p3.setData()
print('ENTER DATA FOR p4 OBJECT')
p4.setData()
print('ENTER DATA FOR p1 OBJECT')
p1.setData()

print('==== OUTPUT OF ALL OBJECTS ====')
p1.getData()
print('___________________')
p2.getData()
print('___________________')
p3.getData()
print('___________________')
p4.getData()
print('___________________')



