# python-else in loop \
# as you have learned before the else clause is used along with the if statement 

# python allows the else keyword to be used with the for and while loops too.
#  the else block aappears after the body of the loop .
#  the statement in the else block will be executed after all iteration are 
# completed the program exits the loop only after the else block is executed
for i in range(5):
    print(i)
# else:
#     print('sorry no i')

for w in range (6):
    if w==4:
        break
else:
  print('sorry no w')   