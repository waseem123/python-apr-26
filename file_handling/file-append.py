import sys

myfile = open('sample.txt', 'a')
data = input('ENTER YOUR DATA TO APPEND - ')
myfile.write('\n' + data)
myfile.close()
print('FILE UPDATED SUCCESSFULLY')
