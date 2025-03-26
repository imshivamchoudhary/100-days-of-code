# dunder method in python
# These are special methods that you can define in your class, and when invoked ,they gave you a powerful way
# to manipulate  objects and their behaviours.
# Magic methods is also known as dunder methods from the double underscore surrounding their name are powerful tools
# that allows you to customize the behaviour of class .They are used to implement speical method such as the addition
# subtraction and comparision operators as well as some more advanced technique like descriptors  and properties


class employees:
    name= 'shivam'
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
e=employees()
print(e.name)
print(len(e))
from emp import person
p=person('Shivam','21','male')
print(p)