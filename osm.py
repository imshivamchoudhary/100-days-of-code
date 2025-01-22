import os
print(os.getcwd())
if (not os.path.exist(f"day{i}")):
    os.mkdir(f"day{i} of code")

for i in range (40,101):
    os.mkdir(f"day{i} of code")
