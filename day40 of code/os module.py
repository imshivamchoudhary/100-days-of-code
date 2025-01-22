# os module in python
# the os module in  python is a built-in library that provides functions for interacting with the operating system.
# It allows to you perform a wide variety to task,such as reading  and writing files, interacting with file system
# and running system commands.
import os

if (not os.path.exists('day40 of code/demo')):
    os.mkdir('day40 of code/demo')
for i in range (1,8):
    os.mkdir(f'day40 of code/demo/test{i}')
    