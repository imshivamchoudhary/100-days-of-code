# Raising custom error in python
# In python,we can raise custom error by using the raise keyword .

a= int(input('enter the value between 1 and 5 '))
if a<1 or a>5:
    raise ValueError('value should be between 1 and 5')
print('you enter the correct value ')

# we learn differrent built in exception in python and why it is important to handle exception. However sometime we may need
# to create our own custom exception that serve our purpose


# Defining custom exception
# In python we can define custom exception bt creating a new class that is derived from the built in exception class 
