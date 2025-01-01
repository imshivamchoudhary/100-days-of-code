# string formating in python
# string formatting can be done in python using format method 
a='My name is {} and I am from {}'
name='Shivam'
country='India'
b=a.format(name,country)
print(b)
# f-string in python
print(f'My name is {name} and I am from {country}')
print(f'we use f-string like this: My name is {{name}} and I am from {{country}}')