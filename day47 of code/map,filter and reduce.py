# In python,map,filter and reduce function are built-in function that allow you to apply a function to a sequence of element and return anew 
# sequence.These function are known as higher ordeer function, as they take other function as argument

# map 
# The map() function applies a function to  each element in a sequence and return a new sequence containing the transformed element.
# The map function has the following syntax 

def cube(x):
    return x*x*x

l=[1,2,3,4]
newl=list(map(cube,l))
newl2=list(map(lambda x:x*x,l))
print(newl2)
print(newl)