# Class Vendor

# Give optimal change for item's cost from amount paid
# Change values:
#   Bills 100, 50, 20, 10, 5, 1
#   Coins 25, 10, 5, 1# Write your solution here!

# Given item cost and amount paid
# set change due = amount paid - item cost
# for largest to smallest denomination (bill or coin)
#   count is int of change_due / denomination
#       reduce change due by count * denomination
#       # of items in change at denomination index is count

import math


class Vendor():

    def __init__(self, name):
        self.name = name

    def make_change(self, item_cost, amount_paid):
        denominations = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]
        change = []
        due = amount_paid * 100 - item_cost * 100

        for denomination in denominations:
            count = math.floor(due/denomination)
            due -= count * denomination
            change.append(count)

        return change

    
    def plural(self, count, item):
        if count < 2:
            return item
        elif item == 'penny':
            return 'pennies'
        else:
            return item + 's'

    def say_change(self, item_cost, amount_paid):

        if item_cost == amount_paid:
            return f"There is no change due for an item that costs ${item_cost} with an amount paid of ${amount_paid}."

        if item_cost > amount_paid:
            return f"There is a balance due of ${(item_cost - amount_paid):.2f}."

        items = ['$100 bill', '$50 bill', '$20 bill', '$10 bill', '$5 bill', '$1 bill', 'quarter', 'dime', 'nickel', 'penny']

        change = self.make_change(item_cost, amount_paid)

        string = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
        
        # Need 'and'? Where?
        num_items = 0
        last_index = -1
        for i in reversed(range(10)):
            if change[i] > 0:
                num_items += i 
                if last_index == -1:
                    last_index = i 

        for index, count in enumerate(change):
            if count > 0:

                if index == last_index and num_items > 1:
                    string += 'and '

                string += f"{count} {self.plural(count, items[index])}"

                if index < last_index:
                    string += ', '

        return string + '.'