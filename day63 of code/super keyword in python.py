# Super keyword in python
# The super() keyword in python  is used to refer to the parent class .It is especially useful when a class inherits from multiple parent classes and
# you want to call a method from one of the parent class

# When a class inherits from a parent class , it can override or extend the methods defined in the parent class.However sometime you might want to use the parent class
# method in the child class . This s where the super() keywords comes in handy

class parent_class:
    def parent_method(self):
        print("Parent method")
class child_class(parent_class):
    def child_method(self):
       print("Child method")
    def parent_method(self):
        print("Parent method from child class")
        super().parent_method()

child_object = child_class()
child_object.child_method()
child_object.parent_method()



class employees:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employees):
    def __init__(self,lang,salary,name,id):
        super().__init__(name,id)
        self.lang=lang
        self.salary=salary
shyam=programmer('kotlin','200000','shyam',1)
vikash=employees("vikash ",'02')
print(shyam.name)
print(shyam.id)
print(shyam.lang)
print(shyam.salary)
print(vikash.name)
print(vikash.id)