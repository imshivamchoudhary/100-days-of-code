# tuples are ordered collection of data items. they store multiple values in single variable tuples are seperated by commas
# they are unchangeable
a=(1,2,3,4)
print(type(a),a)
a=(2)
print(type(a),a)
a=(1,2,4,5,6,7)
print(type(a),a)
print(a[0])
print(a[1])
print(a[2])
# print(a[7])
# negative Index
print(a[-2])
print(a[len(a)-2])
print(len(a))
# check for items
if 5 in a:
    print('yes 5 is present in a')
else:
    print('this no is not present in a')
# range of index
print(a[2:4])