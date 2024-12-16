#ASSIGNMENT OPERATORS (These operate using equal signs ie ==)
 # This means sum = sum + 6

# Given that we have 2 products a mouse and a laptop, such that  the price of a laptop is sh.300,000 and the price of
#  a mouse is sh. 50,000 us a for loop to find the total sum of the products.

mouse = 50000
laptop = 300000
sum = 0
product_prices = [mouse, laptop]
for price in product_prices:
    sum += price
print(f"The total sum of the products is {sum:,}")

#(The final value is always got when the print is pushed to the edge.)


# More Work.