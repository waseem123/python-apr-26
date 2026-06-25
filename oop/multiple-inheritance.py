class Watch:
    brand = 'Fast Track'

    def getFeatures(self):
        print(f'BRAND - {self.brand}')

class Android:
    features = ['Calls and Messages','Notifications','Music Control','Health and Fitness']

    def getFeatures(self):
        print(f'FEATURES - {self.features}')

class SmartWatch(Watch, Android):
    price = 5000
    color = "black"

    def getSmartWatch(self):
        print(f'PRICE - {self.price}')
        print(f'COLOR - {self.color}')

sw = SmartWatch()
sw.getFeatures()
sw.getSmartWatch()