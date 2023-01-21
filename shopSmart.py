# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:
Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    storeCost1 = 0.0
    storeCost2 = 0.0
    shopSave = None;

    # since shop has a method for getting the price of an order
    # we use that.

    #first we iterate through the shops though
    for shopping in fruitShops:
        # we get the price and set it to the storeCost2 because for our
        # second store, that's where it gets saved first
        price = shopping.getPriceOfOrder(orderList)
        storeCost2 = price

        # this should only be hit on the second iteration
        # we check if the cost of store 1 is less than store 2
        # and make sure it's the second iteration because if it's
        # the first iteration, storeCost1 is still 0
        if(storeCost2 > storeCost1 and storeCost1 != 0.0):
            # if we hit this return, it means store 1 had a better deal.
            return shopSave

        # we save the first store, that way we can access the prev
        # store to return
        shopSave = shopping

        # now we store the first store's price
        storeCost1 = price


    # this can either be shopSave or shopping, it doesn't matter
    # since we change shopSave if we don't hit the first return
    # which is always the second shop
    return shopping


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is",
          shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is",
          shopSmart(orders, shops).getName())