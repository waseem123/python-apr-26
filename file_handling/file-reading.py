try:
    myfile = open('demo.txt', 'r')
    data = myfile.read()
    print(data)
    myfile.close()
except FileNotFoundError:
    print('ERROR : FILE NOT FOUND')

print('--------------------------------')

try:
    myfile = open('demo.txt', 'r')
    data = myfile.readlines()
    if len(data) > 0 and len(data[0]) < 5:
        for i in range(len(data)):
            print(data[i])

    print()
    myfile.close()
except FileNotFoundError:
    print('ERROR : FILE NOT FOUND')
print('--------------------------------')

try:
    myfile = open('demo.txt', 'r')
    for line in myfile:
        print(line)
    myfile.close()
except FileNotFoundError:
    print('ERROR : FILE NOT FOUND')