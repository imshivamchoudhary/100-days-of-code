# In python,map,filter and reduce function are built-in function that allow you to apply a function to a sequence of element and return anew 
# sequence.These function are known as higher ordeer function, as they take other function as argument

# map 
# The map() function applies a function to  each element in a sequence and return a new sequence containing the transformed element.
# The map function has the following syntax 

def cube(x):
    return x*x*x

l=[1,2,3,4,5,6,7,8]
newl=list(map(cube,l))
newl2=list(map(lambda x:x*x,l))
print(newl2)
print(newl)

# filter function 
# The filter function filter a sequence of elements based on a given predicate ( a function that return a boolean value) and return a new sequence 
# containing only the element that meet the predicate . The  filter function has following the syntax

def filer_fx(a):
    return a>2
b=list(filter(filer_fx,l))
even=list(filter(lambda a:a%2==0,l))
print(b)
print(even)

# reduce function 
# The reduce function is a higher-order function that applies a function to a sequence and return a single value . It is the part of the functools module
# in the python

# The function argument is a function that takes in two arguments and return a single value .The iterable argument is a sequence of element such as list or tuple 

from functools import reduce
l=[1,2,3,4,5]
def sum (x,y):
    return x+y
mysum=reduce(sum,l)
print(mysum)