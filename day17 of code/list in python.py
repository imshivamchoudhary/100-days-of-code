# pyhton list 
# list are ordered collection of data items.they store multiply values in a single variable
# list are changeable meaning we can alter them after creation 
l=[1,5,2,"shivam",True]
print(type(l))
print(l)
# list index
# each item/element in a list has unique index. this index can be used to access any particular item from the list. the first item has index [0]
name=["shivam",'sumit','vikash','shyam']
print(name[1]) #positive index
# negative index 
print(name[-1]) #negative index
print(name[len(name)-1]) #positive index 
print(name[len(name)-2])

# check whether an item in present in the list 
# we can check if a given item is present in the list this is done using the in keyword
if 'shyam' in name:
    print('yes')
else:
    print('no')
# same thing also applies for strings as well!
if 'shi' in 'shivam':
    print('yes')
else:
    print('no')
# range of index 
print(name[1:4:2]) #2 is jump index
# list comprehension
# list comprehension are used for creating new list from other iterables like lists,tuples dictionaries,sets and even in arry and atrings
la=[i*i for i in range(10)]
print(la)
print(len(la))