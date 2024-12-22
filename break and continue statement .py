# break statement
# the break statement enable a program to skip over a part of the code a break statement terminates the very loop it lies within
for i in range(11):
    if i==5:
        break
    print('4 X',i,'=',4*i)
print('loop ko chodkar nikal gya ')
# continue statement
# the continue statement skip the rest of loop statement and cause the next iteration to occur
for a in range(1,11):
    if a==4:
        print('skip the iteration')
        continue
    elif a==8:
        break
    print('2 X',a,'=',2*a)
