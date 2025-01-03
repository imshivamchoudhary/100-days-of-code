# python sets
# sets are un ordered collection of data items.they store multiple items in a single variable.
#  set items are seperated by commas and enclosed within curly brackets{}.sets are unchangeable 
# meaning you cannot change items of the set once created . sets do not contain duplicate value
s={1,2,3,4,5,5,6,6,4,3,2,}
print(s)
s1={'carla',19,False,5.9,19}
print(s1)

# quick quiz:try to create an empty set. check using the type() function
s2=set()
print(type(s2))

# accessing set items
for value in s1:
    print(value)