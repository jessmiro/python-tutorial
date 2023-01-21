# buyLotsOfFruit.py
# -----------------
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
To run this script, type
  python buyLotsOfFruit.py
Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
    Returns cost of order
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
   # first we iterate through the tuples in orderList with "items"
    for items in orderList:
      #since there's two elements in the tuples, we can use
      # [0] and [1] to take them apart
      # items[0] is the fruit name, so we check if that fruit
      # is in fruitPrices
      if items[0] in fruitPrices:
        # if it is, then we get the value using the fruit name and 
        # save it into price
        price = fruitPrices.get(items[0])

        # now we access the number of pounds of fruit with items[1]
        # and multiply it by the price to get the cost
        cost = items[1] * price

        # and then load it into the totalCost
        totalCost += cost
      
    return totalCost


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))