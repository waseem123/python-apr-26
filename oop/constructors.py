class Bottle:
    def __init__(self, brand='NA', quantity='0 l', price='RS. 0'):
        print('Constructor called')
        self.brand = brand
        self.quantity = quantity
        self.price = price

    def getBottle(self):
        print(f'BOTTLE BRAND : {self.brand}')
        print(f'BOTTLE QUANTITY : {self.quantity}')
        print(f'BOTTLE PRICE : {self.price}')


b1 = Bottle('Bislery', '1l', 'RS. 20')
b1.getBottle()

b2 = Bottle('Aquafina', '2l', 'RS. 30')
b2.getBottle()

b3 = Bottle()
b3.getBottle()
