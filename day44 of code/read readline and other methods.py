# readline() method 
# The readline() method reads a single line from the file .If we want to read multiple lines,we can use a loop 
a=open('sub.txt','r')
i=0
while True:
    i=i+1
    b=a.readline()

    if not b:
        break
    m1=int(b.split(',')[0])
    m2=b.split(',')[1]
    m3=b.split(',')[2]
    print(b)
    print(f'marks of student {i} in math is {(m1*2)}')
    print(f'marks of student {i} in hindi is {(m2)}')
    print(f'marks of student {i} in sst is {(m3)}')

# writelines() method 
# The writelines() method in python write a squence of string to a file .The sequence can be any iterable object ,such as a list or a tuple 
s=open('news.txt','w')
q=['line1\n','line2\n','line3\n']
w=s.writelines(q)
s.close