import doctest


def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
    right = num % 10
    count = 0
    while num > 0:     # while num is enough
        num = num // 10
        next = num % 10
        count += 1
        if next > right:
            return count
    return -1


def filter_sequence(cond, start, stop):
    """
    Returns the sum of numbers from start (inclusive) to stop (inclusive) that satisfy
    the one-argument function cond.

    >>> filter_sequence(lambda x: x % 2 == 0, 0, 10) # .Case 1
    30
    >>> filter_sequence(lambda x: x % 2 == 1, 0, 10) # .Case 2
    25
    """
    "*** YOUR CODE HERE ***"

    ttl = 0
    while start <= stop:
        if cond(start) == True:  # if cond(curr): is enough
            ttl += start
        start += 1
    return ttl


if __name__ == '__main__':
    doctest.testmod(name='filter_sequence', verbose=False)
