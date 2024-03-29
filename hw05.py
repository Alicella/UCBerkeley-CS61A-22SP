passphrase = '*** PASSPHRASE HERE ***'

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
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

    def change_first(self, other):
        # to change the first
        self.first = other
    
    def change_rest(self, other):
        self.rest = other

def has_path(t, term):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular term.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(term) > 0, 'no path for empty term.'
    "*** YOUR CODE HERE ***"

    # pseudocode
    # iterate through the item string, 
    # if a character doesn't match any label of the subtree root/node
    # return false, otherwise true

    # recursively? if term only has one char, then just find if the root label matches
    # if len(term) == 1:
    #     return t.label == term
    # # if term has >= 2 chars, but t is a leaf, then can't find the term
    # else:
    #     if t.is_leaf():
    #         return False
    #     elif t.label == term[0]:
    #         return (t.branches, term[1:])
    #     else:
    #         return False

   
    if t.label != term[0]:  
        return False

    elif len(term) == 1:     # basecase: root label matches first and only char in term      
        return True   

    else:
        for subt in t.branches:                 # try each subtrees until find the one that met has_path
            if has_path(subt, term[1:]):
                return True
        return False                            # if can't find a matching subtree return false
        
# greetings = Tree('h', [Tree('i'),
#                         Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
#                                    Tree('y')])])

# # print(greetings)
# print(has_path(greetings, 'hil'))


def duplicate_link(lnk, val):
    """Mutates `lnk` such that if there is a linked list
    node that has a first equal to value, that node will
    be duplicated. Note that you should be mutating the
    original link list.

    >>> x = Link(5, Link(4, Link(3)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(3))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    """
    "*** YOUR CODE HERE ***"


    if lnk is Link.empty:       # need to include such this case!
        return
        
    elif lnk.first == val:
        lnk.rest = Link(val, lnk.rest)
        
    else:
        duplicate_link(lnk.rest, val)

# Testing：   
# x = Link(5, Link(4, Link(3)))
# # x.rest = Link(5, x.rest)
# # x.rest = x                !!! This doesn't work !!!
# duplicate_link(x, 4)
# print(x)



def deep_map_mut(fn, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"

    if lnk is Link.empty:                   # the element is empty
        return
    elif not isinstance(lnk.first, Link):   # the element isn't a linked list
        lnk.first = fn(lnk.first)      
    else:
        deep_map_mut(fn, lnk.first)

    deep_map_mut(fn, lnk.rest)

# link1 = Link(3, Link(Link(4), Link(5, Link(6))))
# deep_map_mut(lambda x: x * x, link1)
# print(link1)
