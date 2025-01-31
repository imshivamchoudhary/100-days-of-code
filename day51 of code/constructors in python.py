# constructor
# A constructor is a special method in a class used to create and initialize an object of a class .There are different type of constructor.
# Constructor is a invoked autometically when an object of a class is created.
from copyreg import constructor


# A constructor is a unique function that gets called autometically when an object is created of a class .
# The main purpose of a constructor is to initialize or assign a value to the data members of that class .
# It cannot return any value other than none

class person:
    def __init__ (self,name,occ):
        print('Hey I am inside constructor')
        self.name=name
        self.occ=occ
    def info(self):
        print(f'{self.name} is a {self.occ}')
a=person('Shivam','student')
b=person('Shyam','software engineer')
c=person('Manoj','Doctor')
a.info()
b.info()
c.info()

# type of constructor
# 1 parameterized constructor
# 2 default constructor
#
#
# 1 parameterized constructor in python
# When the constructor accept the arrguments along with the self it is known as parameterized
# These arrguments can be used inside the class to assign the value to the data members
#

class person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
a=person('Shivam','student')
print(a.name,a.occ)

# 2 default constructor in python
# When the constructor doesnot accept any arguments from the object and has only one arguments,self,in the constructor
# it is known as default constructor
class detail:
    def __init__(self):
        print('Hey I am inside default constructor')
a=detail()