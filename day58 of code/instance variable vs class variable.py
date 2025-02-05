# instance vs class variable
# In python,variable can be defined at the class level or at the instance level.Understanding he difference
# between these types of variable is crucial for writing efficint and maintainable code

# class variable
# class variable are define at the class level and are shared among all instances of the class.
# They are defined outside of any methods and are usually used to store information that is common
# to all instance of the class
class employees:
    company='google'
    no0femployes=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employees.no0femployes+=1
    def show(self):
        print(f"The name of the empolyee is {self.name} and the salary in {self.no0femployes} sized {self.company} is Rupees {self.salary}")
ep1=employees('Shivam',40000000)
ep1.show()
ep2=employees('Shyam',50000000)
ep2.company='OKX'
ep2.show()
ep3=employees('Manoj',60000000)
employees.show(ep3)
print(ep3.company)
print(ep1.company)
print(ep2.company)

# instance variable
# Instance variable are define at the instance level and are unique to each instance of the class.
# They are define inside the init method and are usually used to store information that is specific
# to each instance of the class