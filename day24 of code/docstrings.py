# docstrings in python
# python docstring are the string literals that appear right after the definition of a function,method,class or module 
def sum (x,y):
    '''Take in a number x and y, returns the sum of x and y'''   #----> it is a docstring
    print(f'the sum of {x}+{y} is equal to {x+y} ')
sum(4,5) 
# by change docstring the program can be changed the outputs of the program can be changed
print(sum.__doc__)

# Comments vs docstrings
# comments
# comments are descriptions that help programmers better understand the intent and functionality of the program. they are completely ignores by the pyhton interpreter

# docstring
# as mentioned above,python docstring are string used right after the definition of a function ,method,class or module (like in example 1).They are used to document our code 
# docstring is right below the function 


# PEP8
# pep 8 is document that provide guidelines and best practices on how to write python code 
import this
