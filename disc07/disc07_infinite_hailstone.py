def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
       At the end of the sequence, yield 1 infinitely.

    >>> hail_gen = hailstone(10)
    >>> [next(hail_gen) for _ in range(10)]
    [10, 5, 16, 8, 4, 2, 1, 1, 1, 1]
    >>> next(hail_gen)
    1
    """
    "*** YOUR CODE HERE ***"

    # try:                       !!! DEAD END !!!
    #     if n == 1:
    #         yield 1
    #     elif n % 2 == 0:
    #         yield n // 2
    #         yield from hailstone(n // 2)
    #     else:
    #         yield n * 3 + 1
    #         yield from hailstone(n * 3 + 1)
    # except StopIteration:
    #     yield 1

    yield n

    if n == 1:
        yield 1
    elif n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

    yield from hailstone(n)


hail_gen = hailstone(10)
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))
# print(next(hail_gen))

print([next(hail_gen) for _ in range(10)])
print(next(hail_gen))
