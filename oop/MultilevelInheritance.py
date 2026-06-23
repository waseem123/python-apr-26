class Box:
    def setBox(self):
        self.boxWidth = input('Enter box width: ')
        self.boxHeight = input('Enter box height: ')
    def getBox(self):
        print(f'BOX WIDTH: {self.boxWidth}')
        print(f'BOX HEIGHT: {self.boxHeight}')

class ColoredBox(Box):
    def setColoredBox(self):
        self.boxColour = input('Enter box colour: ')
    def getColoredBox(self):
        print(f'COLORED BOX COLOUR: {self.boxColour}')

class ShippedBox(ColoredBox):
    def setShippedBox(self):
        self.boxWeight = input('Enter box weight: ')
        self.shippingCost = input('Enter shipping cost: ')
    def getShippedBox(self):
        print(f'SHIPPED BOX WEIGHT: {self.boxWeight}')
        print(f'SHIPPING COST: {self.shippingCost}')


s = ShippedBox()
s.setBox()
s.setColoredBox()
s.setShippedBox()
s.getBox()
s.getColoredBox()
s.getShippedBox()