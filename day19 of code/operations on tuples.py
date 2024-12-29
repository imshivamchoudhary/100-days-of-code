# manipulating tuples
# tuples are immutable hence if you want to add ,remove and change tuples items then first you must convert the tuples to a list 
a=('manoj','shyam','ravi','vikash','sumit','amit','sh')
b=list(a)
b.append('shivam') #add item
b.pop(5)   # remove item
b[5]='choudhary' #change item
a=tuple(b)
print(a)

# it have limited build in method 
# tuples methods
# 1 count methos()
# the count method of tuple returns the number of time the given element appears in the tuple
x=(1,3,4,5,6,5,4,4,3,3,2,4,6,)
y=x.count(4)
print('in tuple 4 is',y,'time')
# 2 index method()
# tuple.index(element,start,end)
# the index method returns the first occurrence of the give element from the tuple 
y=x.index(4)
print('the index of 4 is',y)
y=x.index(4,5,12)
print('the index of 4 is',y)
# length method()
# it is find to length of tuple 
y=len(x)
print('length of tupke is',y)
