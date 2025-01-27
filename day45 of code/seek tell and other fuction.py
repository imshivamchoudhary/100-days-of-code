# seek() and tell() function 
# In python,seek() and tell() function are used to work with file objects and their position within a file. 
# These function is a part of built-in io module , which provide a consistent interface for a reading and writing to various
# file like objects,such as file,pipes and in-memory buffer 


# seek() function 
# The seek() function allows you to move the current position within a file specific point.The position is specified in bytes,and you can move 
# either forword and backward from the cuurrent position 

with open('sh.txt','r') as a:
    # move to the 4th byte in the file 
    a.seek(4)

    # read the next 6 bytes 
    d=a.read(6)
print(d)

# tell() function 
# The tel() function return the current position within the file , in bytes. This can be usefull for keeping track
# of your location within the file or for seeking to a specific position relative to the current position
# print(f'it show the current byte position is {a.tell()}')
with open('sh.txt','r') as a:
    #read the first 10 bytes
    d=a.read(10)
    print(a.tell())
    print(d)

# truncate() function 
# When you open a file in python using the open() function, you can specify the mode in which you want to open the file.
# If you specify the mode as 'w' or 'a' the file is opened in write mode and you can write the file .however if you want 
# to truncate the file to a specific size , you  can use the truncate function
with open('sam.txt','w') as s:
    s.write('''Hey Shivam ,What's up ?''')
    s.truncate(5)
with open('sam.txt','r') as s:
    q=s.read()
    print(q)