x=int(input('enter the value of x '))
match x:
    case 0:
        print('x is zero')
    case 3:
        print('x is 3')
    case _ if x>80 and x<100:
        print('x is graeter then 80')
    case _ if x<40:
        print('x less than 40')
    case _:
        print('the value of x is',x)