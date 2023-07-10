def partition(n, step, seq):
    if len(seq) < n:
        return []
    elif len(seq) == n:
        return [seq]
    else:
        return [seq[:n]] + partition(n, step, seq[step:])

print(partition(3, 1, [1, 2, 3, 4, 5, 6, 7, 8]))