# Local and Global variable in python

# A local variable is a variable that is define within a function and is only accessable within that function.
# It is create when the function is called and is destroyed when the function returns.

# On the other hand , a global variable is a variable that define outside of a function and is accessable from within 
# any function in your code.

x=23   #---> this is a global variable
print(f'this is a global variable {x}')
def func ():
    y=231      #---> this is a local variable
    print(f'this is a loacal variable {y}')
    print(f'I will calling global variabble in this function the global variable is {x}')
func()
# print(y)    #this will cause an error because y is a local variable and it is not accessable outside the function


# Now, what if we want to modify a global variable from within a function we usw global keyword 

# the global keyword 
# The global keyword is used to declear that a variable is a global variable and should be accessable from the global scope 

a=32

def newfunc ():
    global a
    a=765
    b=233
    print(f'the local variable is {b}')
newfunc()
print(f'the global variable is {a}')