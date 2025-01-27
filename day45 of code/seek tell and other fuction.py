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