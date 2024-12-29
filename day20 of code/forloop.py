# loops:
# sometime a programmer want to execute a group of statement a certain number of time this can be done by using loops
# loops are two types
# 1 for loop
# 2 while loop

# for loop
a='shivam'
for i in a:
    print(i)
    if (i=='a'):
        print('this is something spacial')

# we can use loops for list,set and dictionaries

# list
b=['sanwar mal choudhary','heera devi','shivam','sumit']
for i in b:
    print(i)
    for c in i:
        print(c)

for k in range(6):
    k=k+1
    print(k)
for e in range(1,24,):
    print(e)
# in for loop their are three parameters (start,stop,step)
