from turtle import Turtle


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    for i in range(k):
        result = result * (n - i)
    return result


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    i = 1
    ttl = 0
    # cur_y = y
    # while cur_y > 0:
    #     ttl += cur_y % 10
    #     cur_y = y // (10 ** i)
    #     i += 1
    # return ttl

    # for i in range(len(str(y))):
    #     ttl += y % 10
    #     y = y // 10
    # return ttl

    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        dgt = n % 10
        n = n // 10
        if dgt == 8:
            ajct_dgt = n % 10
            if ajct_dgt == 8:
                return True

    return False


# Q5: Digit Position Match
def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    # index = 0
    # while index < k:
    #     n = n // 10
    #     index = index + 1
    # return n % 10 == k

    n = n // (10 ** k)
    return n % 10 == k


print(digit_pos_match(98276, 2))
