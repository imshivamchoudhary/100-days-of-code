# access specifiers/modifiers
# Access specifier or access modifier in python programming are used to limit the access of class variables and class
# methods outside of class while implimenting the concept of inheritance
# type of access specifiers
# 1 public access modifiers
# All the variable and methods (members function) in python are by default public.Any instance variable in a class followed by the
# 'self' keyword.i.e self.name are public accessed
class Person:
    def __init__(self):
        self.name='Shivam'
p=Person()
print(p.name)
# 2 private access modifiers
# Private members of a class(variables or methods) are those members which are only accessible inside the class.
# We cannot use private members outside of class.
# In python,there is no strict concept of 'private' access modifier like in some other programming languages.However a convention
# has been established to indicate that a variable or method should be consider private by prifix its name with a
# double undrescore (__) .This is know as 'weak internal use indicator'
class per:
    def __init__(self):
        self.__name='Shivam'
s=per()
# print(p.__name) --->cannot be accessed  directly
print(s._per__name)    #-----> can be accessed indirectly


# 3 protected access modifies
