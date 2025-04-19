# Single inheritance in python
# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class .This is the simplest
# and most common form of inheritance
#
# syntax
# The syntax for single inheritance in python is straightforward and eassy to understand . To create a new class that inherits from a parent class
# simple specify the parent class in the class defination,inside the parentheses like this


class animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("Sound make by the animal")
class dog(animal):
    def __init__(self,name):
        animal.__init__(self,name)
        self.name=name
    def make_sound(self):
        print("bark!")

d=dog("dog")
d.make_sound()
an=animal("dog")
an.make_sound()