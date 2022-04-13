# Q5: Merge Numbers
# Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order 
# and returns a single number with all of the digits of the two, in decreasing order. 
# Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.


def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"

    #base case: both numbers have one digits and one of them is 0
    big = max(n1, n2)
    small = min(n1, n2)
    if small == 0 and big < 10:
        return big
    else:
        small_one = n1 % 10
        small_two = n2 % 10
        if small_one <= small_two:
            return merge(n1 // 10, n2) * 10 + small_one
        elif small_one > small_two:
            return merge(n1, n2 // 10) * 10 + small_two



# Q6: Is Prime
# Write a function is_prime that takes a single argument n and 
# returns True if n is a prime number and False otherwise. 
# Assume n > 1. We implemented this in Discussion 1 iteratively, 
# now time to do it recursively!

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    

# solution: https://cs61a.org/disc/sol-disc03/
        


