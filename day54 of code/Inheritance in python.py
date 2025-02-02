# Inheritance in python
# When a class drives from another class.The child class will inherit all the public and protected propertie and
# method from the parent class.In addition,it can have its own propertie and method this is called as inheritance

class employees:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f'The name of employee: {self.name}\nid: {self.id}')
class programmer(employees):
    def showlang(self):
        print(f'The default language is python')

p=employees('Shivam',10)
p.show()
p1=programmer('Shyam',11)
p1.show()
p1.showlang()


# Type of inheritance in python
# 1 single inheritance
# 2 multiple inheritance
# 3 multilevel inheritance
# 4 hierarchical inheritance
# 5 hybrid inheritance

