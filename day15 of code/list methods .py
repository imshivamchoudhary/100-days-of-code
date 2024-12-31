l=[4,5,1,6,9,4,8,4,7,4,2,4]
print(l)
print(type(l))
# list method
# 1 list.sort():this method sort the list in ascending order.the original list is updated
l.sort()
print(l)
# the list in descending order we must give reverse=True as a parameter in the sort method
l.sort(reverse=True)
print(l)
# 2 reverse(): this method reverse the order of the list 
l.reverse()
print(l)
# 3 index():this method returns the index of the first occurrence of the list items
print(l.index(6))
# 4 count():return the count of number of item with the given value 
print(l.count(4))
# 5 copy();return copy of the list this can be done by perform operation on the list withot modifying the original list 
s=l.copy()
s[0]=0
print(s)
print(l)
# 6 append():this method appened items to the end of the existing list 
l.append(99)
print(l)
# 7 insert(): this method inserts an item at the given index.user has to specify index and the item to be insert within the insert() method 
l.insert(2,54)
print(l)
# 8 extend():thos method adds an entire list or any other collection datatype (set,tuple,dict) to any existing list 
m=[1400,5000,6000]
m.extend(l)
print(m)
