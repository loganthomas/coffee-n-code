"""
Episode: 2022.01
Title: Python's Built In Zip Function
Link: <TBD>

This is a placeholder for text
https://docs.python.org/3/library/functions.html#zip
"""

# Scenario for using zip
# Benefits of zip
# Syntax of zip
# Gotcha (and itertools.zip_longest)

# Caffeinated Closing
# Inverse of itself

# >>> nums = range(5)
# >>> letters = list('abcde')
# >>> zipped = list(zip(nums, letters))
# >>> zipped
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
# >>> n, l = zip(*zipped)
# >>> n
# (0, 1, 2, 3, 4)
# >>> l
# ('a', 'b', 'c', 'd', 'e')
# >>> n, l = map(list, zip(*zipped))
