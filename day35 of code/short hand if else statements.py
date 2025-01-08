# If.....else in one line 
# there is also a shorthand syntax for the if-else statement that can be used when the condition being tested
# is simple and the code blocks to be executed are short.

a=21
b=23
print(f'{a} is greater than {b}') if a>b else print(f'{b} is greater than {a}')
c=5 if a>b else 0
print(a+c)