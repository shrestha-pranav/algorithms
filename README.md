# Algorithms



```python
%%timeit -n10 -r10
partition_iterative(666)
```

    1.77 ms ± 46.9 µs per loop (mean ± std. dev. of 10 runs, 10 loops each)


```python
result = partition_iterative(666)
%timeit -n1 -r1 sum_digits(result)
```

    3.3 µs ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)


```python
%timeit -n1 -r1 partition_iterative(666666)
```

    1min 47s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

