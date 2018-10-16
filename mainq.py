"""
    Peter Casey
    Oct 15, 2018
    Simple Radix10 sort for numbers
"""

from random import randint
from radix10_sort import Radix10_Sort
from timeit import Timer


#nums = [34, 5, 67, 82, 29, 401, 1, 14, 1000, 44, 17, 82]
#nums = []

MAX_INTS = 100000
MAX = 100

def do_radix():
    nums = []

    for i in range(MAX_INTS):
        nums.append(randint(1, MAX))

    sorter = Radix10_Sort()
    sorter.sort(nums)

    #print(nums)


def do_py_sort():
    nums = []

    for i in range(MAX_INTS):
        nums.append(randint(1, MAX))

    nums.sort()

    #print(nums)

t1 = Timer("do_radix()", "from __main__ import do_radix, MAX_INTS, MAX")
print("radix ",t1.timeit(number=1), "milliseconds")

t2 = Timer("do_py_sort()", "from __main__ import do_py_sort, MAX_INTS, MAX")
print("py sort ",t2.timeit(number=1), "milliseconds")




