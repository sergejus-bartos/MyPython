my_dict = {
    "brand": "KIA",
    2.0: 1.6,
    "year": 2008,
    "who": "Me"
}

for key_variable in my_dict:
    print('the key {0} and the value {1}'.format(key_variable, my_dict[key_variable]))



my_tuple = ('one','two','three')

for number_var in my_tuple:
    print (number_var)
    
print(type(my_tuple))
print(type(my_dict))
print(max(my_tuple))
print(min(my_tuple))