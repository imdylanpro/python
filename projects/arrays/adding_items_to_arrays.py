# Dylan Nelson
# October 09, 2024
# adding_items_to_arrays.py

'''Arrays and lists are mostly synonomous in Python. They will be referred to 
    as lists from this point forward.'''

FORMATTING_STRING = '-'*50

# Creating an empty list.
mylist = []

# Creating a list with integers inside
myintegerlist = [1, 2, 3, 4, 5]

# Creating a list with strings inside
mystringlist = ['Jacob', 'Mark', 'Sally', 'Jessica']

# In Python lists can be populated with dissimilar data types.
myvariedlist = ['James', 1]

# Lists may be nested within each other, creating a 2D list.
mylist.append(myintegerlist)
mylist.append(mystringlist)
mylist.append(myvariedlist)

# Print the contents of a list sequentially
print(FORMATTING_STRING)
print(mylist)

# Using a for loop to access the contents of a list
print(FORMATTING_STRING)
print('For loop example: ')
for i in mylist:
    print(i)

# Using a nested for loop to print the contents of a nested list
print(FORMATTING_STRING)
print('Nested for loop example: ')
for i in mylist:
    for t in i:
        print(t)

# Using a while loop and a flag to print the contents of a list
print(FORMATTING_STRING)
print('While loop example: ')
list_done = 0
length_of_list = len(mylist)
while list_done != length_of_list:
    print(mylist[list_done])
    list_done += 1

# Accessing a specific item in a list
print(FORMATTING_STRING)
print('Accessing a single item in a list example: ')
print(mylist[1])

# Accessing a specific item in a nested list, grabbing the item in the 1 spot 
#   of the outer list and the item in the 2 location on the inner list.
print(FORMATTING_STRING)
print('Accessing a single item in a nested list example: ')
print(mylist[1][2])

# Removing an item from a list. Define what list you want to remove from, then
# provide the index / subscript that the item is located at.
print(FORMATTING_STRING)
print('Removing an item from a list example: ')
print(f"Original list contents: {mylist}")
print(f"Item that is to be removed: {mylist[0]}. ")
mylist.remove(mylist[0])
print(f"Modified list contents: {mylist}")

# Use a for loop to iterate backward through a list, decrementing a custom 
#   number of times.
print(FORMATTING_STRING)
print('Using a for loop to iterate backward down a list with a custom step.')
print(f"Original list contents: {myintegerlist}")
# the first number indicates the starting point, -1 is the last item in the 
#   list. The second number indicates the number after the end point, so the 
#   for loop will actually go to the 0 index not -1 index. The third number is 
#   the step value, the list will derement by 1 each iteration.
for i in range(len(myintegerlist) -1, -1, -1):
    print(myintegerlist[i])
print(FORMATTING_STRING)