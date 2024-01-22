# This module defines the Customer class
# A simulated class to handle the customer loyalty marketing campaign
    # that accumulated in purchases $100 and then the customer will get $10 discount on the next purchase.

class Customer:
    # Construct a customer class with total purchases and discount amount.
    def __init__(self):
        self._total_purchases = 0
        self._discount = 10

    #Define a method to get the total purchases made by the customer.
    def getTotalpurchase(self):
        return self._total_purchases
    
    #Define a method to get the discount amount.
    def getDiscount(self):
        return self._discount

    # Define a method to add the purchase amount into the total purchases.
    # @param amount the amount of the purchase
    def makePurchase(self,amount):
        self._total_purchases = self._total_purchases + amount

    # Define a method to check if the discount is reached based on the total purchases (>= $100).
    # If the total purchases are greater than or equal to $100:
    #   - Apply a $10 discount
    #   - Set total purchases to $0 (discount applied)
    # If the total purchases are less than $100:
    #  - Keep the total purchases and continue to add it to the next purchase( for further checking if the discount is applied or not)
    # @return True if the customer is eligible for a $10 discount, False otherwise.
    def discountReached(self):
        if self._total_purchases >= 100:
            self._discount = 10
            self._total_purchases = 0
            return True
        else:
            return False
    







