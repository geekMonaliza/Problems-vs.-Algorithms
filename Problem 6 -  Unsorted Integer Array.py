def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    min_val = ints[0]
    max_val = ints[0]

    for i in range(1, len(ints)):
        if ints[i] < min_val:
            min_val = ints[i]
        if ints[i] > max_val:
            max_val = ints[i]
    return min_val, max_val


import random

## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

l1 = [i for i in range(50, 500001)]  # a list containing 0 - 9
random.shuffle(l1)

l2 = []  # empty array returns None

l3 = [5, 200, 30, 56, 99, 108, 500, 3000, 389]

l4 = [5, 5, 5, 5, 5, 5, 5, 5]

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((50, 500000) == get_min_max(l1)) else "Fail")
print("Pass" if ((None, None) == get_min_max(l2)) else "Fail")
print("Pass" if ((5, 3000) == get_min_max(l3)) else "Fail")
print("Pass" if ((5, 5) == get_min_max(l4)) else "Fail")
