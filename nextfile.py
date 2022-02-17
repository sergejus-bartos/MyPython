#next file



# some_animals = animals[1:3]
# print(format(some_animals))

animals = ['me', 'you', 'him']
animals.extend(['her', 'some'])
print(animals[-1])
try:
    cat_index = animals.index('cat')
except: 
    cat_index = 'no cats'    
print(cat_index)

for animal in animals:
    print(animal.upper())
    