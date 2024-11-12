# empty list
my_list = []

# append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# created list 2
my_list2 = [50,60,70]

# insert
my_list.insert(1, 15)

# Extending
my_list.extend(my_list2)

# removing the last element
del my_list[-1]

# sorting
my_list.sort()

# index 30
index_of_30 = my_list.index(30)


print(my_list)