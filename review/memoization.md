# Memoization
**Memoization** ensures that a function doesn't run for the same inputs more than once by keeping a record of the results for the given inputs (usually in a dictionary).

For example, a simple recursive function for computing the nnnth Fibonacci number:

```python3
def fib(n):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # Base cases
        return n

    print("computing fib(%i)" % n)
    return fib(n - 1) + fib(n - 2)
```

Will run on the same input multiple times:

```
>>> fib(5)
computing fib(5)
computing fib(4)
computing fib(3)
computing fib(2)
computing fib(2)
computing fib(3)
computing fib(2)
5
```

 We can imagine the recursive calls of this function as a tree, where the two children of a node are the two recursive calls it makes. We can see that the tree quickly branches out of control:

![](fibonacci__binary_tree_recursive.svg)
