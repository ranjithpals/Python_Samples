# Lists
# Since the List as mutable, once a method of the list object is run, it updates the list automatically
l1 = [1, 2, 3]

# Append item to a list
l1.append(5)
print(l1)

# Extend a list to an existing list
l2 = [4, 6]
l1.extend(l2)
print(l1)

# Sort the list
l1.sort()
print(l1)

# Count the list items
print(len(l1))

# Remove the specified list item
l1.remove(6)
print(l1)

# Remove the nth item of the list
l1.pop(2)
print(l1)

# Search within the list and return the index (position) of the element
print(l1.index(5))

# list sort based on a certain key
l = ['Tea', 'Coffee', 'Ice-cream', 'Sundae', 'Chai', 'Chai', 'Sundae', 'Coffee', 'Coffee']
l.sort(key=len, reverse=True)
print(l)

from collections import Counter
# Count the elements of a list
print(Counter(l).most_common(2)[0][0])
# most_common returns a List type object
print(type(Counter(l).most_common()))

l2 = [('Tea', 1), ('Coffee', 2), ('Ice-cream', 2), ('Sundae', 5), ('Chai', 4), ('Chai', 5), ('Sundae', 6), ('Coffee', 4), ('Coffee', 2)]
l2.sort()
print(l2)