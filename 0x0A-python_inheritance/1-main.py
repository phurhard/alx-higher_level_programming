#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(f'first print before sorted {my_list}')
my_list.print_sorted()
print(f"Second print after sorted {my_list}")
print(f'this is my list {my_list}')
