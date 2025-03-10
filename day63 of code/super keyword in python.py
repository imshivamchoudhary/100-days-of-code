# Super keyword in python
# The super() keyword in python  is used to refer to the parent class .It is especially useful when a class inherits from multiple parent classes and
# you want to call a method from one of the parent class
When a class inherits from a parent class , it can override or extend the methods defined in the parent class.However sometime you might want to use the parent class
method in the child class . This s where the super() keywords comes in handy

class parent(object):
    def parent_method(self):
        print("this is the  parent method ")

class child(parent):    
