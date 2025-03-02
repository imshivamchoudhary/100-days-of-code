# Class Methods as Alternative Constructors
# In object oriented programming the term 'constructor' refers to a special type of method that is autometically
# executed when a object is created from a class . The purpose of a constructor is to initialize the object attributes allowing the object
# to be fully functional and ready to use
# However there are time when you may want to create aan object in a different way, or with different initial value
# than what is provided by the default constuctor .This is where class method can be used as alternative constructor

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e=employee('Shivam',40000000)
print(e.name)
print(e.salary)
e1=employee('vikash',300000)
print(e1.name)
print(e1.salary)
string="shyam-50000000"
e1=employee.fromstr(string )
print(e1.name)
print(e1.salary)