import random
from typing import Union


def quicksort(seq: list[Union[int, float, str]]):

    max_index = len(seq) - 1

    if max_index < 1:
        return seq      # <--- Base Case
    else:
        index = random.randint(0, max_index)        # <--- Random index gives us n*log(n) time on average
        picked = seq.pop(index)
        left = [i for i in seq if i < picked]
        right = [i for i in seq if i >= picked]
        return quicksort(left) + [picked] + quicksort(right)


print(quicksort([0, 9, 3, 6, 7, 0, 3, 4, 7, 4, 11, 2, 9]))
