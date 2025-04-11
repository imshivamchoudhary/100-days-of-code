# method overriding in python
# method overriding is a powerful feature in object oriented programming that alllow you do redefine a method
# in a derived class . the method in the derived class is said to override the method in the base class.
# When you created an instance of the derived class and call the overriden method ,the version of the method in the derived
# class is executed rather than the version of the base class.
#
# In python ,method overriding is a way to customize the behavior of a class based on the its specific need .
#

class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14*super().area()


rec=shape(1,2)
print(rec.area())
c=circle(5)
print(c.area())