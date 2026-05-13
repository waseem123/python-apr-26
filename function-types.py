# 1. Default Arg functions
# 2. Keyword Arg functions
# 3. Arbitrary Arg functions
# 4. Keyword Arbitrary Arg functions

def add(n1=0,n2=0):
    print(n1+n2)
    
add(100,20)

# 1. Default Arg Functions
def showData(name="xyz",city="pqr"):
    print(f'My name is {name}. I live in {city}')
    
showData()
showData("waseem","solapur")
# for i in range(1,100000):
#     showData("Solapur")

# 2. Keyword Arg functions
def showName(fname,lname,city):
    print(f'My full name is {fname} {lname}. I live in {city}')
    
showName('Solapur','Attar','Waseem')
showName(city='Pune',lname='Attar',fname='Waseem')

# 3. Arbitrary Arg functions
def showValues(*data):
    print(f"My name is {data[0]} {data[1]}")
    
showValues('Waseem','Attar','Solapur')

def printdata(**data):
    print(f"My name is {data['fname']} {data['lname']}. I live in {data['city']}")
    
printdata(fname='Waseem',lname='Attar',city='Solapur')
