

# # --------------LOOPS----------
# # Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.

# def even_numbers():
#     for num in range(2,20,2):
#         print(num)
# even_numbers()


# # Method 2
# def even():
#     for numb in range (1,21):
#          if numb % 2 == 0:
#             print(f"The even numbers are : \n {numb}")
# even()

# # #Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.

# while True: # The while True loop runs untill the break statement is encountered.
#     number = int(input("Enter number that is greater than ten:\n"))
#     if number > 10:
#         print("Thank you! Your number has reached")
#         break
#     else:
#         print("Sorry! Please try again")


# # #Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

# # The outer loop
# print('The multiplication tabel from 1 to 5')
# for y in range(1,6):
#    print(f'Multiplication Table of {y}: ')

#    # The inner loop
#    for a in range(1,11):
#         print(f'{y} x {a} = {y * a}')
#    print()




# # #Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
# list = [4,7,2,9,12,15]
# odd_sum = 0

# for numbers in list:
#     if numbers %2 != 0:
#         odd_sum+=numbers
# print(f" The sum of the odd numbers is equal to: {sum}")




# # # -----------------LISTS--------------
# # #Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.

# fruits = ['Orange', 'Mango', 'Apple', 'Pineaple', 'Grape']
# for list in fruits:
#     print(list)


# # #Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].

# def squared_numbers(numbers):
#     return [n**2 for n in numbers]
# numbers = [2,3,4]
# squared_numbers = squared_numbers(numbers)
# print(squared_numbers)



# # #Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

# list1 = [1,2,3]
# list2 = [4,5,6]
# combined_list = list1 + list2
# print(combined_list)



# # #Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function
list = [3,1,4,1,5,9,2]
for x in list:
    if x >= 5:
     print(f" The greatest numbers in the list are: {x}")

             


# # # -------DICTIONARIES--------
# # #Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.

# student_information = {
#     'name': 'Musiimenta Agnes',
#     'age': 21,
#     'grade': 'Grade A'
# }

# name = student_information['name']
# print(name)


# age = student_information['age']
# print(age)


# grade = student_information['grade']
# print(grade)


# #Intermediate: Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.

# # people_data = { "name":"Alice", 'age': 24, 'name':"Bob", 'age': 19, 'name': "Charlie",'age': 30}


# # for data in people_data:
# #     if data["age"] >= 21:
# #         print(data)





     
# # #Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana',], and calculates the total cost.
# prices = {
#     'apple': 0.5,
#       'banana': 0.3, 
#       'orange': 0.7
# }
# apple = 0.5
# banana =  0.3
# orange =  0.7
# sum = 0
# list = [apple, orange, banana]
# for price in list:
#     sum += price
# print(f"The total cost is {sum}")
    


# #Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.







# -------OOPs-------

# #Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

# class Car:
#    def __init__(self,brand,color):
#       self.brand = brand
#       self.color = color

#       # Instatinating the object.
# object = Car('Toyota', 'Red')
# print(f"Brand: {object.brand}")
# print(f"Color: {object.color}")


   

# # #Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
# def start_engine(self):
#    print(f"The engine of the car has started")
# start_engine(Car)


# # #Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# # #Deposit an amount.
# # #Withdraw an amount (only if sufficient balance exists).
# # #Print the account balance.
# class BankAccount:
#    def __init__(self,account_number,balance):
#       self.account_number = account_number
#       self.balance = balance
#       # Adding a method to deposit an amount
#       def deposit(self,amount):
#          self.balance += amount
#          print(f"Deposit {amount}. New balance is {self.balance}")
#       deposit(BankAccount)

#         # Withdrawing an amount.
#       def withdraw(self,amount):
#          if amount > self.balance:
#             print("Insufficient funds!")
#          else:
#             self.balance -= amount
#             print(f"You have withdrawn {amount} and your new balance is {self.balance}")


#             # Defining the balance
#       def print_balance(self):
#          print(f"Account number {self.account_number}, Your account balance is {self.balance}")
          
#           # Creating an object to hold the data for the attributes.
#          account = BankAccount(1003456734,50000)

#          #Deposit
#          account.deposit(500)
#          #Withdraw
#          account.withdraw(200)
#          #print balance
#          account.print_balance()
      
      
      


# # #Challenge: Implement a class called Library that manages a collection of books. 
# # #Each book has a title, author, and available status. The Library class should have methods to:

# # #Add a book to the library.
# # #Remove a book from the library.
# # #Check if a book is available by title.
# # #Borrow a book (mark it as unavailable if it’s available).
# # #Return a book (mark it as available again if it was borrowed).
# class Library:
#    def __init__(self,title,author,availabe_status):
#       self.title = title
#       self.author = author
#       self.available_satus = availabe_status

# # Object
#       initials = Library('Betrayal', 'Aaiimwe', 'Availabe') 

   