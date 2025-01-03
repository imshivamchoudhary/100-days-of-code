# methods of sets

# joining sets 
# sets in pythn more and less work in the same way as sets in mathematics.
# We can perform operation like union and intersection on the sets just like math 

# union() and update()
# the union() and  update() methods print all items that are present in the two sets 
# the union() method return a new set whereas
# update() method adds items into the existing set from another set

s={1,2,3,4,5}
s1={4,5,6,7,8,9}
print(s.union(s1))
s.update(s1)
print(s)

# intersection and intersection_update()
s={1,2,3,4,5}
s1={4,5,6,7,8,9}
print(s.intersection(s1))
s.intersection_update(s1)
print(s)

# symmetric_difference and symmetric_difference_update()
# symmetric_difference() and symmetric_difference_update() method print only items that are not similer 
# to both the set the symmetri_difference() method returns a new set whereas symmetric_difference_update()method update 
# into the existing set from another set
s={12,14,1,2,3}
s1={5,6,12,14}
print('symmetric diff',s.symmetric_difference(s1))
s.symmetric_difference_update(s1)
print(s)

# difference() and difference_update()
# the difference() and difference_update() method prints only items that are only present in 
# the original set and not in both the set the difference() method returns a new set wheres difference_update() method udates 
# into the existing set from another set 
s={1,2,3}
s1={4,5,2}
print(f'the difference {s1.difference(s)}') 

# set method() 
# 1 isdisjoint()
# the isdisjoint() method checks if items of given set are present in another set . 
# this method returns false if items are prsent else it return true 
s={1,2,7}
s1={3,4,5}
print(f'this is disjoint is true or false ={s.isdisjoint(s1)}')

# 2 issuperset() 
# the issuperset() method check if all the items of a particular aet are present 
# in the original set it returns true if all the items are present ,else it returns false
s={1,2,3,}
s1={1,2}
print(f'this is super set is {s.issuperset(s1)}')

# 3 issubset() 
# the issubset() method checks if all the items of the original set are present in 
# the particular set it returns true if all the items are present ,else it returns false 
s={1,2,3}
s1={1,2,3,4}
print(f'this subset is {s1.issubset(s)}')

# 4 add()
# if you want to add a single item to the set use the add() method 
s={'manoj','shyam','ravi','vikash','sumit'}
s.add('shivam')
print(s)


# 5 update()
# if you want to add more than one items simply create another set or any
#  other iterable object (list,tuple,dictionary),and use the update() method to add it into the existing set 
s={'shyam','manoj','ravi'}
s1={'vikash','shivam','sumit'}
s.update(s1)
print(s)

# 6 remove()/discard()
# we can use remove() and discard() method to remove items from set 
s={'shyam','shivam','sunday','sumit','manoj','ravi','vikash','sam'}
s.discard('sam')
s.remove('sunday')
print(s)
# the main difference bwtween remove and discard is that if we try to delete
#  an item which is not present in set then remove() raise an error whereas discard() does not raise any error

#  7 pop() 
# this method removes the last item of the set but the catch is
#  that we don't know which item gets popped as sets are unorderd however .
#  you can access the popped items if you assign a pop() method is variable
s={'shyam','shivam','sunday','sumit','manoj','ravi','vikash','sam'}
s1=s.pop()
print(s)
print(s1)

# del
# del is not a method rather it is a keyword which deletes the set entirely
s={'shyam','manoj','ravi'}
s1={'vikash','shivam','sumit'}
del s
# print(s1+s)

# 8 clear()
# this method clears all items in the set and print an empty set 
s={1,2,3,4,5}
s.clear()
print(s)


# check if item exist 
s={'shyam','shivam','sunday','sumit','manoj','ravi','vikash','sam'}
if 'manoj' in s:
    print('manoj is present ')
else:
    print('manoj is abbsent ')