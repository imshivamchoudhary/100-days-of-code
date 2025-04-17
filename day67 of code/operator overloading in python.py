# Operator overloading in python introduction:
# Operator overloading is a feature in python that allows developers to redefine the behavior of mathematical and comparison
# operator for custom data type. This mean that you can use the standard mathematical operator (+ - % / etc)
# and comparison operation (>,<,==,etc) in your own class ,just as you would for built-in data type like int ,float,etc.
#
# why do we need operator overloading
# operator overloading allows you to create more readable and intuitive code .For instance consider a custom class that represent a
# point in 2d space .You coould define a method called 'add' to add two points together

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)
v=vector(1,2,3)
print(v)
v1=vector(9,8,7)
print(v1)
print(v+v1)
print(type(v+v1))