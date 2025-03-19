#List Assignment

#Initialize an empty list to store result
my_list= []

#Append the numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 as the second item in the list
my_list.insert(1, 15)

#Extending the list to add more numbers
my_list.extend([50, 60, 70])

#Removing the last element in list
my_list.pop()

#Sorting the list in ascending order
my_list.sort()

#Index of value of 30
value_30= my_list.index(30)

print(f"My sorted list:",  my_list)
print(f"The value at index 30:", value_30)