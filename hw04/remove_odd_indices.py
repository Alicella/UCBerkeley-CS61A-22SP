import doctest

def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"

    cp = lst.copy()
    # if odd:
    #     return [del cp[i] for i in range(len(lst)) if i % 2 != 0]

    # else:
    #     return [cp.pop(i) for i in range(len(lst)) if i % 2 != 0]
    
    
    for el in lst:
        if odd and lst.index(el) % 2 != 0:
            cp.remove(el)
        elif not odd and lst.index(el) % 2 == 0:
            cp.remove(el)
    return cp

# s = [5, 6, 7, 8]
# t = remove_odd_indices(s, False)
# print(s, t)

if __name__ == '__main__':
    doctest.testfile("remove_odd_indices.py", verbose=True)