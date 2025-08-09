# This is an empty list
my_list = [] 
print("Initial list:", my_list)

# Appending an element to the list
my_list.append(10) 
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending elements:", my_list)

# Inserting the value 15 at a second position
my_list.insert(2, 15)
print("List after inserting 15 at position 2:", my_list)

# Extending the list with another list
my_list.extend([50, 60, 70])
print("List after extending with [50, 60, 70]:", my_list)

# Removing the last element from my_list
my_list.pop()
print("List after removing the last element:", my_list)

# Sorting my_list in ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)  

# Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)
index_of_20 = my_list.index(20)
print("Index of value 20:", index_of_20)
