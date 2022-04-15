from tkinter import Y


def hop():
    """
    Q3 Calling hop returns a curried version of the function f(x, y) = y.

    >>> hop()(3)(2) # .Case 1
    2
    >>> hop()(3)(7) # .Case 2
    7
    >>> hop()(4)(7) # .Case 3
    7
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        def g(y):
            return y
        return g
    return f
    # return lambda x: lambda y: y


def digit_index_factory(num, k):
    """
    Q4 Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).

    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    "*** YOUR CODE HERE ***"

    count = -1

    def offset():
        return count

    while num > 0:
        n = num % 10
        count += 1
        if n == k:
            return(offset)
        num = num // 10

    if n != k:  # 这个if statement 很没必要
        count = -1
        return(offset)

    index = 0
    while num > 0:
        if num % 10 == k:
            return lambda: index
        num //= 10
        index += 1

    return lambda: -1
