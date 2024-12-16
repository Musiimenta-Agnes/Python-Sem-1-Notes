
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

list = ["Fish", "Chicken", "Maize", "Irish", "Rice"]
print("My favourite foods: \n")
print(list) 

# Adding an item to my list
print("My favourite foods with an added item: \n")
list.append("Matooke")
print(list)

# Removing an item from my list
print("My favourite foods after removing one item: \n")
list.remove("Fish")
print(list)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.


numbers = [2,5,8,10,3,6]
print(f"The first element is {numbers[0]}")
print(f"The last element is {numbers[5]}")
numbers.reverse()
print(f"The reversed numbers list is : {numbers}")
total = sum(numbers)
print(f" The sum of {numbers} is {total}")