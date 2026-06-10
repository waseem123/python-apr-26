set_x = {'C','C++','Java','JS','Kotlin','PHP','Python','C','C#','Java','PHP','Dart'}
set1 = {'C','C++','Java','JS','Kotlin','PHP'}
set2 = {'Python','C','C#','Java','PHP','Dart'}
set3 = {'HTML','CSS'}
print(set1)
print(set2)

print(set_x.issuperset(set1))
print(set1.issubset(set_x))
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set2))