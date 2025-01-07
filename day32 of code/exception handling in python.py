# 1 exception handling
# exception handling is the process of responding to unwanted or unexcepted event when a computer program runs . 
# exception handling deals with these event to avoid the program or system crashing and without this process exception 
# would disrupt the normal operation of a program
# 2 Exceptions in python
# python has many built-in exception that are raised when you program encounter an error (something in the program goes worng )
# when these exceptions occur,the python interpreter stops thhe current process and passes it to the calling process until it is 
# handled.if not handled the program will crash


a=input('Enter the number: ')   #--->  In this code if you will give input a string then its occurs an error
print(f'Multiplication table of {a} is')

for i in range (1,11):
    print(f'{int(a)} x {i} = {int(a)*i}')

# try and except in python
# try.....except block are used in python to handle errors and exceptions.the code in try block runs when these is no error 
# if the try block catches the error, then the except block is executed

a=input('Enter the number: ')   #--->  In this code if you will give input a string then its occurs an error
print(f'Multiplication table of {a} is')


try:
    for i in range (1,11):
        print(f'{int(a)} x {i} = {int(a)*i}')
except:
    print('invalid input')
print('end of program')

try:
    b=int(input('enter the number'))
    c=[1,2,3]
    print(c[b])
except ValueError:
    print('number entered is not an integer')
except IndexError:
    print('index error')