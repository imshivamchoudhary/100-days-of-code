class person:
    def __init__(self,name,age, gender):
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self):
        return f'The name of the person is {self.name} \n age = {self.age}\n gender = {self.gender}'