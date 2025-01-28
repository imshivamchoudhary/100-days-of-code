# lambda function in python 
# In python,a lambda function is a small anonymos function without a name .It is define using the lambda keyword and has the 

# Lambda function are often used in situation where a small function is requred for a short period of a time. 
# They are commonly used as arguments to higher order function such as map,filter, and reduce
# Lambda function can have multiple arguments,just like a regular function 

# def cube (x):
#     return x*x*x
# print(cube(2))
def sqr(x,value):
    return 1+x(value)
cube=lambda x:x*x*x
sum=lambda a,b:a+b
print(sqr(cube,3))
print(sum(1,2))
print(cube(2))
print(sqr(lambda x:x*x,4))