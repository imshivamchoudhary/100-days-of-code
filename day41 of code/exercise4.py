# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode


a=input('enter your massage ')
words=a.split(' ')
b=int(input('press 1 for coding or 0 for decoding'))
if b==True:
    b==1
    print('you choose coding ')
    if b:
        e=[]
        for word in words:
            if(len(word)>=3):
              r1 = "werdsf"
              r2 = "tyrty"
              stnew = r1+ word[1:] + word[0] + r2
              e.append(stnew)
            else:
                e.append(word[::-1])
        print(" ".join(e))
else:
    print('you choose decoding')
    e=[]
    for word in words:
        if(len(word)>=3): 
         stnew = word[3:-3]
         stnew = stnew[-1] + stnew[:-1]
         e.append(stnew)
        else:
            e.append(word[::-1])
    print(" ".join(e))