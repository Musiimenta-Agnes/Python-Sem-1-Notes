# #1. The volume of a sphere with radius r is (4/3)* pie r**2.
# # What is the volume of a asphere with radius 5
# #Make sure the prigaram enters the radius from the keyboardand provide the answer in 2 decimal places.

# r = int(input("Enter radius: "))
# import math
# pie = math.pi
# volume = (4/3)*pie*r**2
# print(f"The volume of a sphere whose radius is 5 is {volume:.2f}")



# #2. Create a program to calculate the area of a triangle (1/2* base*height).
# #Base and hehghst should be enterd using the keyboard.

# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area = 1/2*base*height
# print(f"The area of a triangle is {area}")


# #3. WITI has tasked you to automate a simple grading system,
# #As a python student, write a program used to display the grades that
# #the students wil be receiving based on the mark scored in a subject.
# #The gardes are:
# # 90% -100%  Grade is A
# # 80% - 89%  Grade is B
# # 70 - 79%   Grade is C
# # 60% -69%  Grade is D
# # 50% - 59%  Grade is E
# # 50% - Fail

# def calculate_grades():
 
#  print("\n Calculating the student's grades")
#  mark = int(input("Enter the mark: "))

#  if 90<=mark<=100:
#         print(f"Grade A")
#  elif 80<= mark<=89:
#         print(f"Grade B")
#  elif 70<=mark<=79:
#         print(f"Grade C")
#  elif 60<=mark<=69:
#         print("Grade D")
#  elif 50<= mark<=59:
#         print(f"Grade E")
#  else:
#         print(f"Fail")

#         calculate_grades()


#4. WITI academy is proposing a sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI sacco.
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
# Ensure that if the students selects 1, money is deposited and the minimum
# deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the sudebnts selects 3, the account balance should be displayed.


def sacco_usage():
      print("Welcome to Sacco: \n Please choose from the following options: \n 1: Deposit \n 2: Withdraw \n 3: Check Balance")
      choice = int(input("Enter your option, it should be either 1, 2, or 3: \n"))
      initial_amount = 0
      if choice == 1:
            print("Processing.....")
            amount_deposited = int(input("Enter amount to be deposited:  "))
            minumum_deposite = 1000
            if amount_deposited > minumum_deposite:
                  total_balance = initial_amount + amount_deposited
                  print(f"Your total balance is {total_balance}")
            else:
                  print("Please! The amount you entered is below the required. Please try again.")
      if choice == 2:
            print("Processing.....")
            amount_withdraw = int(input("Enter the amount to be withdrawn: "))
            minimum_withdraw = 500
            if amount_withdraw > minimum_withdraw:
                  withdrawn_amount = total_balance - amount_withdraw 
                  print(f"You have withdrawn {amount_withdraw} and your account balance is {withdrawn_amount}")
            else:
                  print("Please! Wrong choice")
                  
sacco_usage()
                  
            
            
      




