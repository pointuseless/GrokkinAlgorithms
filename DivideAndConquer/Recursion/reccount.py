def recursive_count(seq: list) -> int:
    try:
        seq.pop()
        return 1 + recursive_count(seq)
    except IndexError:
        return 0


print(recursive_count([1, 2, 3, 4, 5]))
