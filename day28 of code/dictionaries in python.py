# Python dictionaries
# dictionaries are ordered collection of data items . they store multiple items in a single 
# variable dictionary items are key-value pairs 
# that are seperated by commas and enclosed within curly bracket {}
dic={
'shivam': 'human being',
'jaipur': 'place',
123 : 'counting'

}
print(dic[123]) # it will show you an error

# accessing dictionary items
# values in a dictionary can be  accessed using keys.we can access dictionary values by mentioning keys either in 
# square brackets or by using get method 
print(dic.get(123)) # it will show you none value instent of error
print(dic.keys())
for key in dic.keys():
    print(f'the value is corresponding to the key {key} is {dic[key]}')

# accessing multiple values
# we can print all the value in the dictionary using value() method 
print(dic.values())
 
# accessing key-value pairs
# we can print all the key-value pairs in the dictionary using items() method 
print(dic.items())
for key,value in dic.items():
    print(f'the value is corresponding to the key {key} is {value}')
