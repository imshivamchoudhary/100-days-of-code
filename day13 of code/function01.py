# function
# it is used to seperate the code and reduced the line of code-and it helps in repeat the code without any extra typing
print('not using  function')
a=2
b=8
gmean1=(a*b)/(a+b)
print(gmean1)

c=4
d=2
gmean2=(c*d)/(c+d)
print(gmean2,'\n')

# here i write a block of code it use at-least 10 line
# now i use function to reduce line and when ever i need this code i do not need to write it again
print('using function')
def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
gmean(2,4)
gmean(2,8)

def counting (a,b):
    for a in range(a,b):
        a=a+1
        print(a)
counting(40,50)

# function are two types
# 1 built-in function: these function are defined and pre-coded in python some examples of built-in function
# min(),max(),len(),type(),range(),etc
# 2 user defined function: we can create function to perform specific task as per our need such function are called used-defined function

# calling function
# we call a function by giving the function name followed by parameters (if any ) in the parenthesis
