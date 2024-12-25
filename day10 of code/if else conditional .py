# if-else statement
# to check the evaluation of certain expression. weather the expression evaluate to true or false if the expression evaluates to false then the program
# execution follows a different path then ot would have if the expression had evaluation true
# based on this the conditional statement are further classified into the following type
# if
# if-else
# if-else-elif
# nested if-else-elif
a=int(input("Enter a number: "))
# conditional operators
# >,<,>=,<=,==,!=
if a<0:
    print('the number is negative')
elif a>0:
    if a<=10:
        print('the num is between 0 and 10')
    elif (a>10 and a<=20):
       print('the num is between 10 to 20')
    else:
       print('nmu is greater than 20')

else:
    print('the number is positive')
print('i am happy now')
