set1 = {'C','C++','Java','JS','Kotlin','PHP'}
set2 = {'Python','C','C#','Java','PHP','Dart'}
print(set1)
print(set2)

set3 = set1.difference(set2)
print(set3)

set4 = set2 - set1
print(set4)

set2.difference_update(set1)
print(set2)