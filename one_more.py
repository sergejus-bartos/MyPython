# fruits = ["peach", "apple", "melon", "berry"]
# print (format(fruits))

# sorted_fruits = sorted(fruits)
# print (format(sorted_fruits))

# all_fruits = fruits + sorted_fruits
# print (format(all_fruits))

# for number in range(1,5, 2):
#    print(number)


# Create a list to hold the to-do tasks.
to_do_list = []
finished = False
while not finished:
    task = input('Enter a task for your to-do list. Press <enter> when done: ')
    if len(task) == 0:
        finished = True
    else:
        to_do_list.append(task)
        print('Task added.')

# Display the to-do list.
print()
print('Your To-Do List:')
print('-' * 16)
for task in to_do_list:
    print(task)