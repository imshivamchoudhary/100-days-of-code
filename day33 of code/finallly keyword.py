# finally clause
# the finally code block is a part of exception handling when we handle exception using the try and except block,
# we can include a finally block at the end. The finally block is always execute,so it is generally used for doing 
# the concluding task like closing file resources or closing database connection or may be ending the program
# execution with a delightful message.
try:
    a=[1,2,3,4]
    i=int(input('enter the index value'))
    print(a[i])
except:
    print('some error occurred')
finally:
    print('i am always run')

print('i am always run')  #-----> In this case it is always executed.

def list1 ():
    try:
        a=[1,2,3,4]
        i=int(input('enter the index value'))
        print(a[i])
        return 1
    except:
        print('some error occurred')
        return 0
    
    
   
    print('i am always run')   # ----> In this case it is not executed 
x=list1()
print(x)