# class method
# A class method is a type of method that is bound to the class and not the instance of the class .
# In other words,it operates on the class as a whole,rather than on a specific instance of the class.
# class method are define using @classmethod decorator.followed by a function definition.
# The first argument of the function is always 'cls' which represent the class itself

class employee:
    company='google'
    def show(self):
        print(f"the name is {self.name} and  company is {self.company}")
    @classmethod
    def newcompany (cls,new_company):
        cls.company=new_company
e=employee()
e.name='Shivam'
e.show()
e.newcompany('OKX')
e.show()
print(employee.company)