# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/Partition.ipynb (unless otherwise specified).

__all__ = ['partition_seq1', 'partition_seq2', 'partition', 'sum_digits', 'partition_iterative']

# Cell
import functools
import numpy as np

# Cell
def partition_seq1():
    # Alternate between {1, 2, 3, 4, ...} and {3, 5, 7, 9, ...}
    i, j = 1, 3
    while True:
        yield i
        yield j
        i, j = i+1, j+2

def partition_seq2():
    i = 1
    for ddelta in partition_seq1():
        yield i
        i += ddelta

# Cell
@functools.lru_cache(maxsize=1000, typed=True)
def partition(n:int):
    if n < 0: return 0
    elif n == 0: return 1

    delta_gen = partition_seq2()
    total = 0

    while True:
        d = [next(delta_gen) for _ in range(4)]

        total += partition(n - d[0]) + partition(n - d[1])
        total -= partition(n - d[2]) + partition(n - d[3])

        if d[3] > n: break

    return total

# Cell
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Cell
def partition_iterative(n:int) -> int:

    # Calculate how many numbers we need (+ buffer of 4 numbers)
    x = np.int(np.ceil((np.sqrt(24*n+81)-9)/6)) + 1 + 2

    deltas = np.zeros(2*x, dtype=np.int64)
    deltas[1::2] = np.arange(1, x+1)
    deltas[0::2] = np.arange(1, 2*x, 2)
    deltas = deltas.cumsum()
    deltas = list(map(int, deltas))

    flags = list(map(int, np.tile([1,1,-1,-1], x//2+1)))

    p = [1]
    for i in range(1, n+1):
        total = 0

        for j in range(0, 2*x, 4):
            if deltas[j+4] > i:
                if deltas[j+0] <= i: total += p[i - deltas[j+0]]
                if deltas[j+1] <= i: total += p[i - deltas[j+1]]
                if deltas[j+2] <= i: total -= p[i - deltas[j+2]]
                if deltas[j+3] <= i: total -= p[i - deltas[j+3]]
                break

            total += \
                p[i - deltas[j+0]] + \
                p[i - deltas[j+1]] - \
                p[i - deltas[j+2]] - \
                p[i - deltas[j+3]]

        p.append(total)

    return p[-1]