"""
Demonstration of dictionaries
"""

# Dictionaries are data structures that hold pairs of items. For example:
#   p_table = {1 : 'Hydrogen', 2 : 'Helium', 3 : 'Lithium', 4 : 'Beryllium'}
#
# The dictionary p_table contains 4 pairs of items, separated by commas, with
# the first one being 1 : 'Hydrogen'.
# The first item, 1, is called the 'key' and the second item, 'Hydrogen', is
# called the 'value'.
#                       1 : 'Hydrogen'
#                      /          \
#                    key         value
# Given the key it's possible to get the corresponding value, but given the
# value it's not possible to get the key. For example:
#   print(p_table[3])           # prints Lithium
#   print(p_table['Helium'])    # ERROR: KeyError
#
# Dictionaries can have duplicate values, but not duplicate keys. All keys in
# a dictionary are unique. If a new key-value pair is added and that key is
# already in the dictionary it gets replaced by the new pair. For example:
#   p_table[1] = 'Deuterium'
#   print(p_table[1])           # prints Deuterium, the 1 : 'Hydrogen' pair was replaced
#
# The key-value pair types do not have to be the same for all the dictionary
# elements. For example:
#   var = {'key' : 'value', 10 : 20, True : 'True', 'Pi' : 3.14}

# Initializing a dictionary
p_table = {1 : 'Hydrogen', 2 : 'Helium', 3 : 'Lithium', 4 : 'Beryllium'}
dict_1 = {'key' : 'value', 10 : 20, True : 'True', 'Pi' : 3.14}

# Getting a value from a key
val = dict_1['Pi']
print("Getting value from key 'Pi', " + str(val))

# Adding/replacing a single element to a dictionary
p_table[5] = 'Boron'
print("Adding Boron to p_table, p_table[5] = " + str(p_table[5]))

# Adding/replacing multiple elements to a dictionary
p_table.update({6 : 'Carbon', 7 : 'Nitrogen', 8 : 'Oxygen'})

# Iterating through all the key-value pairs method #1
print("All elements in p_table:")
for key in p_table:
    # *NOTE* DO NOT rely on the order elements to be the same as
    # the order in which they were added!
    print(str(key) + " : " + str(p_table[key]))

# Get the total number of key-value pair elements using the len() function
print('dict_1 has a total of ' + str(len(dict_1)) + ' elements')

# Removing a key-value pair. This changes the size of the dictionary.
print("Removing key Pi...")
if 'Pi' in dict_1:
    del dict_1['Pi']
print('dict_1 has a total of ' + str(len(dict_1)) + ' elements')

# Iterating through all the key-value pairs method #2
print("\nAll elements in dict_1:")
for key, value in dict_1.items():
    print(str(key) + " : " + str(value))

# Iterating through all the values
print("\nAll values in p_table:")
for value in p_table.values():
    print(str(value), end=', ')
