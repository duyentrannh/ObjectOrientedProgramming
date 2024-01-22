# This program is to test the Customer class from excercise Business P9.26 

def demo():
    import argparse
    import textwrap
    from P9_26 import Customer


    parser = argparse.ArgumentParser(prog='My test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                        Customer Loyalty Marketing Campaign
                                    ----------------------------------------------------
                                    A simulated class to handle the customer loyalty marketing campaign,
                                    that accumulated in purchases $100 and then the customer will get $10 discount on the next purchase.
                                    
                                    Methods:
                                    1) getTotalpurchase : Gets the total purchases made by the customers.
                                    @return the total purchases

                                    2) getDiscount : Gets the discount amounts.
                                    @return the discount amounts                                                          
                                                                 
                                    3) makePurchase : Adds the purchase amount into the total purchases.
                                    @param amount the amount of the purchase
                                    
                                    4) discountReached : a method to check if the discount is reached based on the total purchases(>=$100).
                                    If the total purchases are greater than or equal to $100:
                                        - Apply a $10 discount
                                        - Set total purchases to $0 (discount applied)
                                    If the total purchases are less than $100:
                                        - Keep the total purchases and continue to add it to the next purchase( for further checking if the discount is applied or not)
                                    @return True if the customer is eligible for a $10 discount, False otherwise.
                                                                                                                                                                                                                                                       
                                    '''),
                                    epilog=textwrap.dedent('''\
                                            Usage
                                    --------------------------------------
                                    customer.getTotalpurchase() # Gets the  total purchases
                                    customer.getDiscount() # Gets the discount amount
                                    customer.makePurchase(120) # Adds the purchase amount to total purchases
                                    customer.discountReached() # Checks if the customer eligible for $10 discount.                                                                                                                            
                                    ''')
                                    )
    
    parser.add_argument('--run_demo',action='store_true',help='Runs this demo')
    args = parser.parse_args()

    if args.run_demo:
        customer = Customer()
        customer.makePurchase(120) #test value: first purchase 
        print('The first total purchases is ${}'.format(customer.getTotalpurchase())) # print out the total purchases 

        if customer.discountReached(): # check if the total purchases >= $100
            print("Customer is eligible for a $10 discount on the next purchase.") # if it is true, print out the message the customer is eligible to get discount 
            print("Discount amount: ${} ".format(customer.getDiscount()))                                          # and the discount amount
        else:
            print("Customer is not eligible for a discount yet.") # if not, print out the message that customer is not eligible to get the discount yet.

        # Second purchase, over $90, but less than $100.

        customer.makePurchase(95) #test value: second purchase 
        print('The second total purchases is ${}'.format(customer.getTotalpurchase()))

    # Check if the customer is eligible for a second discount (should not be eligible)
        if customer.discountReached():
            print("Customer is eligible for a $10 discount on the next purchase.")
            print("Discount amount: ${} ".format(customer.getDiscount())) 
        else:
            print("Customer is not eligible for a second discount.") # This time the customer is not eligible for the discount because the total purchase is $ 95 
                                                                     # which is over $90 but less than $100.

    # Third purchase that triggers the second discount
        customer.makePurchase(20)  # test value : Third purchase
        print('The third total purchases is ${}'.format(customer.getTotalpurchase()))

        # Check if the customer is eligible for a second discount after the third purchase
        if customer.discountReached():
            print("Customer is eligible for a $10 discount on second discount.") # This time the discount is applied because total purchases from
            print("Discount amount: ${} ".format(customer.getDiscount()))        # from the second purchase and third purchase is $95 + $20 = $115 > $100. 
        else:
            print("Customer is not eligible for a second discount.")


if __name__ == '__main__':
    demo()

