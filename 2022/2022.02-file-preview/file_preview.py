"""
Episode: 2022.02
Title: File Previews with Python
Link: <TBD>

This is a placeholder for text
"""

# Demo pandas and numpy with simple text
# Explain frustrations with cryptic error messages
# Demo opening a file, or using !cat or !head or !tail
# What if we want to customize and do it in python?


# Disclaimer: assuming we can load the file into memory when using the "reverse" because we call .readlines()
# Up to this point, only a single line is loaded as we iterate.

# Iteration 1
def head(filename):
    with open(filename) as f:
        for line in f:
            print(line)
            # print(line.strip())

# Iteration 2
# def head(filename):
#     with open(filename) as f:
#         for i, line in enumerate(f):
#             print(i, line.strip())

# Iteration 3

# this won't work (TypeError: '_io.TextIOWrapper' object is not subscriptable)
# def head(filename, n):
#     with open(filename) as f:
#         for i, line in enumerate(f[:n]):
#             print(i, line.strip())

# this is inefficient
# def head(filename, n):
#     with open(filename) as f:
#         all_lines = f.readlines()
#         for i, line in enumerate(all_lines[:n]):
#             print(i, line.strip())

# more efficient with the zip trick

# ----- side bar ----- #
# Mention zip video and link in description
# nums = [0,1,2,3,4,5]
# letters = ['a', 'b', 'c', 'd', 'e']
# zip(nums, letters)
# list(nums, letters)
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# letters = ['a', 'b', 'c']
# list(zip(nums, letters))
# [(0, 'a'), (1, 'b'), (2, 'c')]

# from itertools import zip_longest
# zip_longest(nums, letters)
# list(zip_longest(nums, letters))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, None), (4, None), (5, None)]

# list(zip_longest(nums, letters, fillvalue='n/a'))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'n/a'), (4, 'n/a'), (5, 'n/a')]

# this is better
# def head(filename, n):
#     with open(filename) as f:
#         for i, line in zip(range(n), f):
#             print(i, line.strip())

# Iteration 4
# def head(filename, n=10, show_n=False):
#     """
#     Print the first `n` lines of a file.
#     Parameters
#     ----------
#     filename : str
#         The path to the file that should be parsed.
#     n : int, default: 10
#         The number of lines to parse from the file.
#     show_n : bool, default: False
#         Whether or not to show the line number of each parsed line.
# """
#     with open(filename) as f:
#         for i, line in zip(range(n), f):
#             if show_n:
#                 print(i, line.strip())
#             else:
#                 print(line.strip())
#             # print(i, line.strip()) if show_n else print(line.strip())


# def preview(filename, n=10, show_n=False, from_end=False):
#     """
#     Print the first n_lines of a file.
#     Parameters
#     ----------
#     filename : str
#         The path to the file that should be parsed.
#     n_lines : int, default: 10
#         The number of lines to parse from the file.
#     show_lines : bool, default: False
#         Whether or not to show the line number of each parsed line.
#     """
#     with open(filename) as f:
#         if from_end:
#             f = f.readlines()[-1*n:]
#         for i, line in zip(range(n), f):
#             if from_end:
#                 i += -1*n
#             print(i, line.strip()) if show_n else print(line.strip())

