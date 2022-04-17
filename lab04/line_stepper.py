def line_stepper_q(start, k):
    """
    Complete the function line_stepper, which returns the number of ways there are to go from
    start to 0 on the number line by taking exactly k steps along the number line.

    >>> line_stepper(1, 1)
    1
    >>> line_stepper(0, 2)
    2
    >>> line_stepper(-3, 3)
    1
    >>> line_stepper(3, 5)
    5
    """
    "*** YOUR CODE HERE ***"

    # didn't find the correct base case
    if abs(start) > k:
        return 0
    elif abs(start) == k:
        return 1
    elif (k - abs(start)) % 2 != 0:
        return 0
    else:
        return line_stepper_q(start, k - 2) + abs(start) + 1

print('my solution', line_stepper_q(3, 5))

def line_stepper(start, k):

    if k == 0 and start == 0:
        return 1
    elif k == 0:
        return 0
    left = line_stepper(start - 1, k - 1)
    right = line_stepper(start + 1, k - 1)
    return left + right

print('staff solution', line_stepper(3, 5))