# staticmethod in python are methods that belongs to a class rather than an instance of the class.They are define
# using the @staticmethod decorator and do not have access to the instance of the class (i.e self). They are called the
# class itself ,not on an instance of the class.Static method are often used to create utility function that do not need
# access to instance data.

class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add (n1,n2):
        return n1+n2
a=math(10)
print(a.num)
a.addtonum(12)
print(a.num)
print(math.add(10,20))

# For interview purpose
# Q1 == It is necessary to use 'sefl' argument while making method in a class?
# ans==No