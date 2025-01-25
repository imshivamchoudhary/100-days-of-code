# Opening a file 
# Before we can perform any operation on a file,we must first open it. Python provides the open() function to open a file.
# It takes two arguments:the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading,
# 'w' for writing,or 'a' for appending
f=open('myfile.txt','r')
print(f)
text = f.read()
print(text)



# Modes in file 
# 1 read(r):This mode opens the file for reading only and give an error if the file doesn,t exist.This is the default
# mode,if no mode is passed as a parameter

# 2 write(w):This mode open file for writing only and create a new file if the file does not exits 
f=open('file1.txt','rt')
wq=f.read()
f.close()
print(wq)
# 3 append(a):This mode opens the file for appending only and create a new file if the file does not exits 
f=open('file1.txt','a')
f.write('hey boii')
# 4 create(x):This mode create a file and gives an error if the file already exits

# 5 text(t):Apart from these modes we also need to specify how the file must be handle.t mode is used to handle text file.
# t refer to the text mode . there is a no difference between r and rt or w and wt since text mode is default.The default mode is 'r'
# (open for reading text ,synonym of 'rt')

# 6 binary(b):used to handle binary files (image,pdf,etc) 

# closing a file 
# It is important to close a file after you are done with it.This release the resources used by the file and allows
# other program to access it 

f=open('myfile.txt','r')
c=f.read()
print(c)

# the 'with' statement 
# Alternatively,you can use the statement to autometically close the file after you are done with it 
with open('me.txt','r') as d :
    o=d.read()
    print(o)