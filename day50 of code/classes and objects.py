# python class and object
# A class is blueprint or a template for creating objects,providing initial values for state (mamber variables or attributes)
# and implementations of behavior (mamber function or method).The user define object are created using the class keyword

class person:
    name='Shivam'
    occupation=input("enter your occupation: ")
    age=int(input("enter your age: "))
    def info(self):
        print(f'{self.name} is a {self.occupation} and {self.age } years old')
a=person()   #---> This is an object
print(a.name)
a.name='Shyam'
print(a.name)
print(a.occupation)
a.info()

# creating an object
# Object is the instance of the class used to access the properties of the class
a=person()   #---> This is an object

# self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class
# it must provided as the extra parameter inside the method definition