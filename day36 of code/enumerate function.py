# without using enumerate function
# marks=[45,23,56,78,89,9,4,5]
# index=0
# for mark in marks:
#     print(mark)
#     if index==4:
#         print('good marks')
#         index+=1
#     elif index==6:
#         print('poor marks')
#     index+=1

# Enumerate function in python
# the enumerate function is a built-in function in python that allows you to loop over sequence ( such as tuple,list or string)
# and get the index and value of each element in the sequence at the same time 
marks=[45,23,56,78,89,9,4,5]
for index, mark in enumerate(marks):
    print(mark)
    if index==4:
        print('good marks')
print('\n')
        
# changing the start index
#  By default,the enumerate function starts the index at 0, but you can specify a different 
# stating index by passing its an arguument to the enumerate function
marks=[45,23,56,78,89,9,4,5]
for index, mark in enumerate(marks,start=1):
    print(mark)
    if index==4:
        print('good marks ')