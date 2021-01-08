def recursive_sum(seq: list[int]) -> int:
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + recursive_sum(seq[1:])


print(recursive_sum([1, 2, 3, 4, 5, 6]))
