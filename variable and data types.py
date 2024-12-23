# variables are like container that holds the date
from dataclasses import dataclass

a=1
b=True
c='Shivam'
d=None
print(a)
print(b)
print(c)
print(d)
# Data type: data type specific the type of value a variable is hold
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#built in data type
#int,float,complex this are numeric data
x=1
y=1.1
z=2+3j
s=complex(3,2)
print(s)
print(x)
print(y)
print(z)
# text data
#string
x1="shivam"
print(x1)
#boolean data
#boolean data is consists of value true or false

# sequenced data
# list,tuple are sequenced data
# list is an order of collection of data with elements of seperated by comma and enclosed within square bracket
list1=[2,3.4,-2],['shivam','choudhary']
print(list1) #we can change the list
# mutable means change hona
#tuple
# a tuple is an order of collection of data with element seperated by a comma and enclosed with in parentheses. Tuples are immutable.and can not be modified after creation
# immutable means change na hona

tuple1=(('shivam','choudhary'),34,3.4)
print(tuple1)

# mapped data
# dict:collection of key value pairs
dict1={'name':'shivam','age':18,"canvote":False}
print(dict1)
# in python everything is object
