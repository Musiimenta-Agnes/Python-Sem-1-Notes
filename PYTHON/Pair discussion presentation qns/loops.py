# # --------------LOOPS----------
# # Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.



def even():
    for numb in range (1,21):
         if numb % 2 == 0:
            print(f"The even numbers are : \n {numb}")
even()

# # #Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.

while True: # The while True loop runs untill the break statement is encountered.
    number = int(input("Enter number that is greater than ten:\n"))
    if number > 10:
        print("Thank you! Your number has reached")
        break
    else:
        print("Sorry! Please try again")


# # #Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

# The outer loop
print('The multiplication tabel from 1 to 5')
for y in range(1,6):
   print(f'Multiplication Table of {y}: ')

   # The inner loop
   for a in range(1,11):
        print(f'{y} x {a} = {y * a}')
   print()




# # #Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
list = [4,7,2,9,12,15]
odd_sum = 0

for numbers in list:
    if numbers %2 != 0:
        odd_sum+=numbers
print(f" The sum of the odd numbers is equal to: {odd_sum}")