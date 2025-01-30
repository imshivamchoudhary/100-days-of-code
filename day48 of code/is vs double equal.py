# 'is ' vs '==' in python
# In python 'is' and == are both comparison operator that can be used to check if two value are equal.However there are
# some important difference between the two that you should be aware of

# The 'is ' operator compare the identity of two objects ,while the == operator compares the values of the object .
# This mean that is will only return true if the object being compared are the exact same object in memory ,while ==
# will return true if the object have the same value.

a=3
b=3
print(a is b) #exact location of object in memory
print(a==b)#value