set1 = {'C','C++','Java','JS','Kotlin','PHP'}
set2 = {'Python','C','C#','Java','PHP','Dart'}
print(set1)
print(set2)

set3 = set1.intersection(set2)
print(set3)

set2.intersection_update(set1)
print(set1)
print(set2)