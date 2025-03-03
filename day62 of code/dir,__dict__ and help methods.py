# dir (), __dict__ and hepl() methods in python
# Attributes/methods in python.
# They make it easy for us to understand how class resolve various function and executes code.
# In python , there are three built-in functions that are commonly used to get information about object:
# dir(),__dict__() and help().


# 1 dir() method
# the dir() function returns a list of all the attributes and methods(including dunder methods) available for an object.
# It is a usefull tool for discovering what you can do with an object.
x=[1,2,3,4,5]
print(dir(x))
print(x.__add__)

# 2 __dict__ attribute
# The __dict__ attribute return a dictionary representation of an object's attribute.It is a useful tool for introspection.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.rollno=23
p=person('vikash',21)
print(p.name)
print(p.age)
print(p.__dict__)

# 3 help() method
# The help() function is used to get help documentation for an object , including a description of its attributes and methods.
print(help(person))