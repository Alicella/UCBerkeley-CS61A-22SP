from itertools import count


HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos > 0 and pos < 10:
        if pos == 8:
            return 1
        else:
            return 0
    elif pos % 10 == 8:
        return 1 + num_eights(pos//10)
    else:
        return num_eights(pos//10)

    # staff solution:
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    elif pos < 10:
        return 0
    else:
        return num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"

    if n == 1:
        return 1
    if n == 2:
        return 2

    def counting_up(n):
        up = True
        for i in range(n):
            if i % 8 == 0 or num_eights(i):
                up = not up
        return up

        # no need to change direction

    if counting_up(n):
        return pingpong(n - 1) + 1
    else:
        return pingpong(n - 1) - 1


# using assignment statement
# value = 0
# counting_up = True        #counting up when True, counting down when False

# for i in range(1, n+1):
#     if counting_up:   #the sequence is counting up
#         value += 1
#     else:               #the sequence is counting down
#         value -= 1

#     if i % 8 == 0 or num_eights(i):
#         counting_up = not counting_up   # This can be modulized

# return value
step = 1
print(-step)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if change == 0:
        return 0
    elif change <= 5:
        return 2            # charge = 5: 5 coin1, 1 coin5
    elif change <= 10:
        return 4          # charge = 10: 10 coin1, 2 coin5, 1coin5 + 5 coin1, 1 coin10
    elif change <= 25:
        return 11                    # charge = 25: 25 coin1, 5/4/3/2/1 coin5, 2/1 coin 10, 1 coin25

    # if change % 25 == 0:
    #     # ???