# how importing in python works
# Importing in python is the process of loading code from a python module into the current script.
# This allows you to use the function and variable define in the module in your current script ,as well as 
# any additional modules that the imported module may depends on

# To import a module in python , you use the import statement 
# for example import math module which contains a variety of mathmatical fuction you would use the followin function 
import math
a=math.floor(65.65)
print(a)

# from keyword 
# you can also import specific function or variable from a module using the from keyword 
from math import sqrt,floor
a=floor(sqrt(67))
print(a)


#importing everything
# It's also possible to import all function and variables from a module using the * wildcard.
# however this is generally not recommendable as it can lead to confuse and make it harder to understand
# where specific function and variable are comming from\

from math import *
a=math.floor(65.65)
print(a)
print(pi)

# the as keyword 
import math as m 
a=m.pi**2
print(a)

# the dir function 
# Finally,python has a built-in function called dir that you can use to view the names of all the function 
# and variable defined in a module . this can be helpful foe exploring and understanding the content of a new module
print(dir(math))
print(math.sqrt,type(math.nan))

from shivam import*
welcome()
print(shivam)
