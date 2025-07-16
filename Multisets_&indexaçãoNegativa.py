from collections import Counter

# Creating a multiset (bag of elements) using Counter
c = Counter(a=4, b=3, c=2)

# .elements() returns an iterator of all elements in the Counter (repeats according to count)
print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']

# Most common elements (sorted by count, descending)
print(c.most_common())         # [('a', 4), ('b', 3), ('c', 2)]
print(c.most_common(2))        # [('a', 4), ('b', 3)]

# ----------------------
# NEGATIVE INDEXING AND SLICING

lst = [1, 2, 3, 4, 5, 6]
# Last element:
print(lst[-1])   # 6
# Second-to-last:
print(lst[-2])   # 5
# Third-to-last:
print(lst[-3])   # 4

# Negative slicing: [start:stop] with negative indices
print(lst[-4:-2])    # [3, 4]
# Negative step: reversed, every 2 elements
print(lst[::-2])     # [6, 4, 2]
"""
Negative indexing/slicing lets you access elements from the end of the list.
- lst[-1] is the last element
- lst[::-1] reverses the list
- lst[::-2] reverses and skips every other element
"""
