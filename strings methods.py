# string are immutable
# len()
# len() is used to find the length of string
a='shivam'
print(len(a))
# string method
# Python provide a set of built-in method that we use to alter and modify the string
# 1 upper()
# the upper() method converts a string to upper case
s=('choudhary')
print(s.upper())
# 2 lower()
# the lower() method coverts a string to lower case
a1='SHIVAM'
print(a1.lower())
# strip()
# the strip() method remove any white space before and after the string
s1=('     shivam choudhary      ')
print(s1.strip())
# rstrip()
# the rstrip() remove any trailing character
a2='shivam@@@@@'
s2='@@@@shivam@@@@'
print(a2.rstrip('@'))
print(s2.rstrip('@'))
# replace()
# the replace() method all occurences of a string with another string
a3="""my name is shiv
shiv is a good boy"""
print(a3.replace("shiv","shivam"))
# split()
# the split() method splits the given at the specified instance and return the separated string as the list items
s3="shivam,age 18"
print(s3.split(','))
# capitalize()
# the capitalize() methods turns into only the first character of the string to upper case and the rest other characcter of the string are turned to lower case
heading='introduction your self.'
print(heading.capitalize())
# center()
# the center() method aligns the string to the center as per the parameters given by the user
str='hello shivam '
print(str.center(50))
print(len(str))
print(len(str.center(50)))
# count()
# the count() method returns the number of times the given value has occurred within the given string
c=('my name is shivam'
       'he is a good boy')
print(c.count('is'))
# endswith()
# the endswith() method check if string end with a given value . if yes then return true,else return false
str2='hi shivam.'
print(str2.endswith('.'))
str2='shivam'
print(str2.endswith('am',4,6))
# find()
# the find() method searches for the first occurrence of the given value and return the index where it is present it given value is absent from the string then return -1
print(c.find('shivam'))
# index()
# the index() method searches for the first occurrence of the given value and return the index where it is present it given value is absent from the string then raise an exception
# print(c.index('ch'))
# isalnum()
# the isalnum() method return true only if the entire string only consist of A-Z,a-z or 0-9 if any other character or punctuation are present then it returns false
str='shivam78'
print(str.isalnum())
# isalpha()
# the isalpha() method is return true only if the entire string only consist of A-Z,a-z if any other character or punctuation or number(0-9) are present thenn it return false
str='shivam@'
print(str.isalpha())
# islower()
# the islower() method return true if all the character in the  string are lower case else it return false
str='shivam is goOd boy'
print(str.islower())
# isprintable()
# the isprintable() method return true if all the value within the given string are printable if not then return false
str='shivam is good\n coding'
print(str.isprintable())
# isspace()
# the isspace() method return true only and only if the string contains white space else return false
str='  '
print(str.isspace())
# istitle()
# the istitle() return true only if the first latter of each word of the string is capitalized else it returns false
str='Shivam choudhary'
print(str.istitle())
# isupper()
# the isupper() method return true if  all the character in the string are upper case else it return false
str='sHIVAM'
print(str.isupper())
# startswith()
# the startswith() method checks if the string start with a given value if yes then return true else return false
str='hi shivam choudhary'
print(str.startswith('hi'))
# swapcase()
# the swapcase() method change the character casing of the string upper case are connverted into the lower case and the lower case are connverted into the upper case
str='sHIVAM cHOUDHARY'
print(str.swapcase())
# title()
# the title() method capitalizes each letter of the word within the string
str=("introduction your self")
print(str.title())