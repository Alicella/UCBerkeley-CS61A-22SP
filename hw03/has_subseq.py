import doctest


def has_subseq(n, seq):
    """
    Complete has_subseq, a function which takes in a number n and a "sequence"
    of digits seq and returns whether n contains seq as a subsequence, which
    does not have to be consecutive.

    >>> has_subseq(123, 12)
    True
    >>> has_subseq(141, 11)
    True
    >>> has_subseq(144, 12)
    False
    >>> has_subseq(144, 1441)
    False
    >>> has_subseq(1343412, 134)
    True
    """
    "*** YOUR CODE HERE ***"

    # take the last number x in seq, loop through n to find the position of x
    # take the 2nd last number y in seq, loop through n until the position of x to find y
    # until all digits in num has been found
    # or one digit in num can't be found in seq
    
    # while seq:
    #     seq_digit = seq % 10
    #     find_digit = False
    #     while n:
    #         num_digit = n % 10
    #         if seq_digit == num_digit:
    #             find_digit = True
    #             break
    #         n = n // 10
    #     if not find_digit:
    #         return False

    #     seq = seq // 10

    # return True

    # Using recursion, staff solution
    if n == seq:
        return True
    if n < seq:
        return False
    without = has_subseq(n // 10, seq)
    if seq % 10 == n % 10:
        return has_subseq(n // 10, seq // 10) or without  # !!!!!!!
    return without

# print(has_subseq(144, 1441))

if __name__ == '__main__':
    doctest.testmod(name='has_subseq', verbose=True)
