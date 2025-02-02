# Getters
# Getters in python are methods that are used to access the value of an object's property.They are used to return
# the value of specific property,and are typically define using the @property decorator .

class person:
    def __init__(self,value):
        self.sh=value
    def show(self):
        print(f'The value is {self.sh}')
    @property
    def sh1(self):
        return 10*self.sh
obj=person(10)
obj.show()
print(obj.sh1,'\n')

# Setters
# It is important to note that the getters do not take any parameters and we can not set the value through getter method.
# For that we need setter method which can be added by decorating method with @property_name.setter


class person:
    def __init__(self,value):
        self.sh=value
    def show(self):
        print(f'The value is {self.sh}')
    @property
    def sh1(self):
        return 10*self.sh
    @sh1.setter
    def sh1(self,new_value):
        self.sh=new_value/10
obj=person(10)
obj.show()
obj.sh1=200
obj.show()
print(obj.sh)