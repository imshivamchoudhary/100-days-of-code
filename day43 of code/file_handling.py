# Opening a file 
# Before we can perform any operation on a file,we must first open it. Python provides the open() function to open a file.
# It takes two arguments:the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading,
# 'w' for writing,or 'a' for appending
f=open('myfile.txt','r')
print(f)
text = f.read()
print(text)
f.close()


# Modes in file 
# 1 read(r):This mode opens the file for reading only and give an error if the file doesn,t exist.This is the default
# mode,if no mode is passed as a parameter
