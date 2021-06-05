# Write your unit tests here!
import unittest
from optimal_change import *

# Test computer for vending machine
# Give optimal change for item's cost from amount paid
# Change values:
#   Bills 100, 50, 20, 10, 5, 1
#   Coins 25, 10, 5, 1

class ValidateOptimalChange(unittest.TestCase):

    def test_change_1(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.make_change(62.13, 100), [0, 0,1,1,1,2,3,1,0,2])

    def test_change_2(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.make_change(31.51, 50), [0,0,0,1,1,3,1,2,0,4])

    def test_change_3(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.say_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

    def test_change_4(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.say_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

    def test_change_5(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.make_change(62.87, 100.12), [0,0,1,1,1,2,1,0,0,0])

    def test_change_6(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.say_change(62.87, 100.12), "The optimal change for an item that costs $62.87 with an amount paid of $100.12 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, and 1 quarter.") 

    def test_change_7(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.say_change(12.34, 12.34), "There is no change due for an item that costs $12.34 with an amount paid of $12.34.")

    def test_change_8(self):
        vendor = Vendor('Lollipop Machine')
        self.assertEqual(vendor.say_change(52.34, 42.34), "There is a balance due of $10.00.")

if __name__ == '__main__':
    unittest.main()
