# dictionary methods 
# 1 update() 
# the update() method update the value of the key provided to it if the item already exists in the dictionary,else it creates a new key-value pair
sh={'name':'shivam','state':'Rajasthan','age':21}
ya={'Name':'yash','State':'uk','Age':20,'school':'matrix',111:"sh"}
sh.update(ya)
print(sh)
print(ya)

# clear()
# the clear() method remove all the items from the dictionary
sh.clear()
print(sh)

# pop() 
# the pop() method removes the key-value pair whose key is passed as a parameter 
ya.pop('Name')
print(ya)

# popitem()
# the popitem() method removes the last key-value pair from the dictionary
ya.popitem()
print(ya)

# del: 
# we can also use the del keyword to remove a dictionary items
del ya['Age']
print(ya)