set1 = {'C','C++','Java','JS','Kotlin','PHP'}
set2 = {'Python','C','C#','Java','PHP','Dart'}
print(set1)
print(set2)

set3 = set1.symmetric_difference(set2)
print(set3)

set1.symmetric_difference_update(set2)
print(set1)