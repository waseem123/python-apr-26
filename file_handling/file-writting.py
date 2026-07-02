import sys

myfile = open('sample.txt','w')
print('ENTER YOUR DATA TO WRITE IN THE FILE (PRESS CTRL+D TO SAVE)')
data = sys.stdin.read()
myfile.write(data)
myfile.close()
print('File updated successfully')
