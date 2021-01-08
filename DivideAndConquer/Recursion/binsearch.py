from typing import Optional, Union


def binary_search(term: Union[int, float, str],
                  seq: list[Union[int, float, str]]) -> Optional[int]:

    if not seq:
        return None     # Base Case 1

    mid = (len(seq) - 1) // 2
    mid_item = seq[mid]

    if mid_item == term:
        return mid      # Base Case 2
    elif mid_item > term:
        return binary_search(term, seq[:mid])
    elif mid_item < term:
        return binary_search(term, seq[mid + 1:]) + mid + 1


print(binary_search('f', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
