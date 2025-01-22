import os
print(os.getcwd())


for i in range (1,5):
    os.mkdir(f"test{i} of code")

if (not os.path.exist(f"day{i} of code")):
    os.mkdir(f"test{i} of code")