def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"

    # ?what's prev_digit doing?

    # solving idea: not using recursion. Parse from the rightmost digit
    # to left, and check the digit to its left or right
    # until reaching the leftmost digit
    

    # same_digit_total = 0
    # # only include cases for above three digits.
    # while num // 100:
    #     right_digit = num % 10
    #     mid_digit = num // 10 % 10
    #     left_digit = num // 100 % 10
        
    #     if right_digit == mid_digit:
    #         same_digit_total += 2
    #         if left_digit == mid_digit:
    #             same_digit_total += 1
    #     elif left_digit == mid_digit:
    #         same_digit_total += 2
        
    #     num = num // 10
    # return same_digit_total

    # staff solution:
    if num < 10:
        return int(num == prev_digit)
    last = num % 10
    rest = num // 10
    return int(prev_digit == last or rest % 10 == last) + neighbor_digits(num // 10, last)

