# while loop execute statements while the conditions is true as soon as the condition become false the interpeter comes out of the while loop
for i in range(10):
    print(i)
i=0
while (i<4):
    print(i)
    i=i+1

a=2
while a<=21:
    a=int(input('enter the value of a '))
    print(a)
print('done with the loop')
# else with while loop
# we can even use the else statement with the while loop essentially what the else statement does is that as soon as
# the while loop condition becomes false the interpeter comes out of the while loop and the else statement become execute
i=1
while i<=6:
    print(i)
    i=i+1
else:
    print('i am inside the else')

