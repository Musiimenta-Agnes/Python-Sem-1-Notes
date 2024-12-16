# -------OOP-------

# #Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

class Car:
   def __init__(self,brand,color):
      self.brand = brand
      self.color = color

      # Instatinating the object.
object = Car('Toyota', 'Red')
print(f"Brand: {object.brand}")
print(f"Color: {object.color}")


   

# #Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.

class Car:
   def __init__(self,brand,color):
      self.brand = brand
      self.color = color


def start_engine(self):
   print(f"The engine of the car has started")

   # Creating an instance and calling the method
cars = Car("Toyota", "Red")   
start_engine('self')


# # #Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# # #Deposit an amount.
# # #Withdraw an amount (only if sufficient balance exists).
# # #Print the account balance.
class BankAccount:
   def __init__(self,account_number,balance):
      self.account_number = account_number
      self.balance = balance
      # Adding a method to deposit an amount
      def deposit(self,amount):
         self.balance += amount
         print(f"Deposit {amount}. New balance is {self.balance}")
      deposit(BankAccount)

        # Withdrawing an amount.
      def withdraw(self,amount):
         if amount > self.balance:
            print("Insufficient funds!")
         else:
            self.balance -= amount
            print(f"You have withdrawn {amount} and your new balance is {self.balance}")


            # Defining the balance
      def print_balance(self):
         print(f"Account number {self.account_number}, Your account balance is {self.balance}")
          
          # Creating an object to hold the data for the attributes.
         account = BankAccount(1003456734,50000)

         #Deposit
         account.deposit(500)
         #Withdraw
         account.withdraw(200)
         #print balance
         account.print_balance()
      
      
      


# # #Challenge: Implement a class called Library that manages a collection of books. 
# # #Each book has a title, author, and available status. The Library class should have methods to:

# # #Add a book to the library.
# # #Remove a book from the library.
# # #Check if a book is available by title.
# # #Borrow a book (mark it as unavailable if it’s available).
# # #Return a book (mark it as available again if it was borrowed).
class Library:
   def __init__(self,title,author,availabe_status):
      self.title = title
      self.author = author
      self.available_satus = availabe_status

# Object
      initials = Library('Betrayal', 'Aaiimwe', 'Availabe') 