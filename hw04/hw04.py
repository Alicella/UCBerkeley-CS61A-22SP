def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"

    if lst1 == [] or lst2 == []:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        # coin = Coin(self.year)
        # return coin
        return coin(self.year)    # ??? why
    
    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        # value = self.cents #+ Mint.present_year - self.year - 50 
        return self.cents + max(0, Mint.present_year - self.year - 50)


class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


mint = Mint()
print(mint.year)
dime = mint.create(Dime)
print(dime.year)
Mint.present_year = 2101 
nickel = mint.create(Nickel)
print(nickel.year)
print(nickel.worth())








class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    Nothing left to vend. Please restock.
    >>> v.add_funds(15)
    Nothing left to vend. Please restock. Here is your $15.
    >>> v.restock(2)
    Current candy stock: 2
    >>> v.vend()
    You must add $10 more funds.
    >>> v.add_funds(7)
    Current balance: $7
    >>> v.vend()
    You must add $3 more funds.
    >>> v.add_funds(5)
    Current balance: $12
    >>> v.vend()
    Here is your candy and $2 change.
    >>> v.add_funds(10)
    Current balance: $10
    >>> v.vend()
    Here is your candy.
    >>> v.add_funds(15)
    Nothing left to vend. Please restock. Here is your $15.

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    Current soda stock: 3
    >>> w.restock(3)
    Current soda stock: 6
    >>> w.add_funds(2)
    Current balance: $2
    >>> w.vend()
    Here is your soda.
    """
    "*** YOUR CODE HERE ***"
    
    def __init__(self, product, price):
        # initialize the product of this vending machine, and the price for each;
        # initial stock of the product and fund is 0
        self.product = product
        self.price = price
        self.stock = 0
        self.fund = 0
    
    def restock(self, added_stock):
        # update the stock of this product and print the current stock
        self.stock += added_stock
        print(f'Current {self.product} stock: {self.stock}')
    
    def add_funds(self, fund):
        self.fund += fund
        if self.stock != 0:
            print(f'Current balance: ${self.fund}')
        else:
            print(f'Nothing left to vend. Please restock. Here is your ${self.fund}.')
            self.fund = 0


    def vend(self):
        if self.stock == 0:
            print('Nothing left to vend. Please restock.')
        else:
            if self.fund < self.price:
                print(f'You must add ${self.price - self.fund} more funds.')
            else:
                if self.fund == self.price:
                    print(f'Here is your {self.product}.')
                else:
                    print(f'Here is your {self.product} and ${self.fund - self.price} change.')
                
                self.stock -= 1
                self.fund = 0

# All above print should be return

# v = VendingMachine('candy', 10)
# v.restock(2)
# v.vend()
# v.add_funds(7)
# v.vend()
# v.add_funds(5)
# v.vend()
# v.add_funds(10)
# v.vend()
# v.add_funds(15)