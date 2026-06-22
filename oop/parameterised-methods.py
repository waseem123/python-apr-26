class Computer:
    def setData(self, processor='', ram='0 GB', ssd='0 GB'):
        self.processor = processor
        self.ram = ram
        self.ssd = ssd

    def getData(self):
        print(f'PROCESSOR : {self.processor}')
        print(f'RAM : {self.ram}')
        print(f'SSD : {self.ssd}')


c1 = Computer()
c1.setData('Intel Core i5 5th Generation',
           'DDR4 - 16GB RAM',
           '1TB SSD')
c1.getData()

c2 = Computer()
c2.setData()
c2.getData()
