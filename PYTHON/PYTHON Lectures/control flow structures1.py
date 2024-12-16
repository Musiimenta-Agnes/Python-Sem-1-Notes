# CONTROL FLOW STRUCTURES
# Theses determin the order in which the pogram is executed basing on the loops and conditions.

#CONDITIONAL STATEMENT
#Thee are programs that base on a particulkar condition, eg. if, elif


#Example.
# 1. Create a program that asks a user for the food type bought from the market. 
# The program should print yuo bought chicken if the user enters chicken,
# print you brought liver if the user enters liver, elsi print you bought of fish.


print('\n Please choose from chicken, liver and fish')
food_type = input("\n Enter the type of food bought: ").lower()
if food_type == 'chicken':
    print(f"You bought chicken from the market")
elif food_type == 'liver':
    print(f"You bought liver from the market")
elif food_type == 'fish':
     print(f"You bought fish from the market")
else:
    print(f" choose from chicken liver and fish") 
    # This is working with the conditional statements.



# For another approach.
if food_type != 'chicken' or food_type!= 'liver' or food_type!= 'fish':
    print('Please  choose from chicken, liver and fish')
    if food_type == 'chicken':
     print(f"You bought chicken from the market")
elif food_type == 'liver':
    print(f"You bought liver from the market")
elif food_type == 'fish':
     print(f"You bought fish from the market")
else:
    print(f" choose from chicken liver and fish")

    # MORE WORK