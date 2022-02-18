import os
my_current = os.getcwd()
print(my_current)

my_current = my_current + '\MyPython\data_file.txt'
print (my_current)
my_file = open (my_current)
my_file_content = my_file.read()
print(my_file_content)
my_file.close()


with  open(my_current) as my_filename:
    for my_line in my_filename:
        print(my_line.rstrip())