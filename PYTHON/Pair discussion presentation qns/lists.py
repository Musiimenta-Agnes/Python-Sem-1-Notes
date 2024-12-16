# # # -----------------LISTS--------------
# # #Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.

fruits = ['Orange', 'Mango', 'Apple', 'Pineaple', 'Grape']
for list in fruits:
    print(list)


# # #Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].

def squared_numbers(numbers):
    return [n**2 for n in numbers]
numbers = [2,3,4]
squared_numbers = squared_numbers(numbers)
print(squared_numbers)



# # #Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

list1 = [1,2,3]
list2 = [4,5,6]
combined_list = list1 + list2
print(combined_list)



# # #Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function
list = [3,1,4,1,5,9,2]
for x in list:
    if x >= 5:
     print(f" The greatest numbers in the list are: {x}")