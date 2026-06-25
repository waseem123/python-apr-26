class Bank:
    def getInterest(self):
        return 0

class SBI(Bank):
    def getInterest(self):
        return 10

class BOI(Bank):
    def getInterest(self):
        return 12

class HDFC(Bank):
    def getInterest(self):
        return 13

b = HDFC()
print(b.getInterest())