# function arguments and return statement 
# there are four types of arguments that we can provide in a function 
# 1 default argumrnt: we can provide a default value while creating a function.
def sum (a=5,b=7):
    print('the sum is:',a+b)
sum()
# 2 keyword argument: we can change the order of arguments 
def value (a=1,b=5):
    print('the value of is',a,'and',b)
value(b=3,a=8)
# 3 variable length argument: sometime we may need to pass more aargument than those defined in the actual function this can be done using variable length arguments 
def naam (*num):
    print('friends',num)
naam('shivam','sumit','shyam','ravi','vikash')
# 4 required argument:in case we don't pass the argument with a key = value syntax then it is necessary to pass the argument in the
#  corrct positional order and the number of argument passed should match with actual function define
def multiply(a,b):
    print('the multiplication of',a,'and',b,'is',a*b)
multiply(9,8)

# return statement
# the return statement is used to return the value of the expression back to the calling function 
def divide (a,b):
    return (a/b)
s=divide(5,2)
print(s,'\n')

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
        # return 9
        return sum/len(numbers)
d=average(2,3,4,5)
print(d)
