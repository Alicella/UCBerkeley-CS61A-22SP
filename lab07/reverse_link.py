from re import A


def reverse_link(lnk):
    """
    Given a linked list lnk, return a new linked list which has all the
    elements of lnk but in reverse order.
    
    >>> s = Link(1, Link(2, Link(3, Link.empty)))
    >>> reverse_link(s)
    Link(3, Link(2, Link(1)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> k = Link(3, Link(5, Link(7, Link(9))))
    >>> reverse_link(k)
    Link(9, Link(7, Link(5, Link(3))))
    >>> k
    Link(3, Link(5, Link(7, Link(9))))
    """
    "*** YOUR CODE HERE ***"

    #how to iterate lnk? get lnk.first, then let lnk = lnk.rest
    # when lnk.rest is empty, then reach the end

    # how to build the reversed lnk? start from the last element of the orginal lk ls.
    # then build upwards, adding reversed_lnk.first

    # if lnk is Link.empty:
    #     return lnk
    # elif lnk.rest is Link.empty:
    #     reversed = Link(lnk.first)
    # else:
    #     lnk = lnk.rest

    reversed = Link.empty         

    while lnk is not Link.empty:       # iterate until find the innermost linked list
        reversed = Link(lnk.first, reversed)
        lnk = lnk.rest
        
    return reversed





class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


k = Link(3, Link(5, Link(7, Link(9))))
r = reverse_link(k)
print(r)
print(k)