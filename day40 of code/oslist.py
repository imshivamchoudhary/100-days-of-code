import os
folders=os.listdir('day40 of code/demo')
print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f'day40 of code/demo/{folder}'))