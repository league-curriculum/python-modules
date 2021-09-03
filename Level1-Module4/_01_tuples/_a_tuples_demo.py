"""
Demonstration of tuples
"""

# Tuples are a data structure that contains multiple items of different types.
# They are similar to lists with the following differences:
#   * They are created using parenthesis () instead of square brackets []
#   * Elements can't be changed after the tuple is created
#   * New elements can't be added after the tuple is created
#
# Below are examples of how to create a tuple and use it:

# Initializing a tuple
tup = (1, 2.5, 'hello', False)

# Getting an element from a tuple using square brackets []
element_0 = tup[0]
element_3 = tup[3]
print('tuple element 0 is ' + str(element_0))
print('tuple element 3 is ' + str(element_3))

# Getting the number of elements in the tuple
size = len(tup)
print('the tuple has ' + str(size) + ' elements!' )

# Iterating through all the elements in a tuple
for element in tup:
    print(str(element), end=', ')
print('\n')

# Iterating through all the elements in a tuple with index #1
for i, element in enumerate(tup):
    print(str(i) + '. ' + str(element))
print('')

# Iterating through all the elements in a tuple with index #2
for i in range(len(tup)):
    print(str(i) + '. ' + str(tup[i]))
