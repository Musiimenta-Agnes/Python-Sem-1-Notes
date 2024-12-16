
# # SOME PRACTICE QUESTIONS


# # 1).Using a function and variables enterd from the keybard, write a progra that allows the user to input a number.
#  # If the input is an even number, returns the input divded by two plus 1
# # If the input is an odd number, returns a squre of the input.

def even_or_odd_number ():
    number = int(input('Enter the number: \n'))
    if number %2 == 0:
        result =(number/2)+1
        print(f"{result}")
    else:
        result = number**2
        print(f"{result}")
even_or_odd_number()

# Even this below is correct.

def even_and_odd_numbers():
    number = int(input("Enter the numebr: "))
    if number %2 == 0:
        result = number/2 + 1
        print(f"Number: Even:\n Result: {result:.0f}")
    else:
        #Odd number
        result = number**2
        print(f"Number: Odd:\n Result:{result:.0f}") 

even_and_odd_numbers()


# # 2). Design a program that asks a user to enter a store's sales for each day of the week. The amounts should be stored in a list.
# # Use a loop to calculate the total sales for the week and display the result.



def total_weekly_sales ():

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sales = []
    total_weekly_sales = 0

    for day in days:
        sales_amount = int(input(f"Enter the sales amount for:  {day} : "))
        sales.append(sales_amount)


    for sale in sales:
        total_weekly_sales+=sale
        print(f"The weekly total sales for the store is: {total_weekly_sales}")

        
total_weekly_sales()           


# Add the following numbers using a loop. [2,4,6,8,9]

def addition():
    numbers = [2,4,6,8,9]
    sum = 0
    for number in numbers:
        sum+=number
        print(f"The sum of the numbers in the above list is {sum}")
addition()


# # Qn. Write a program to convert temperature  to and from celicius and faranheight. Formular  = (F = 9/5C+32)



print("Temperatue converter")
print("1. From Celicius to Faranheight")
print("1. Frm Faranheight to Celicius")

option = int(input("Enter your option and choose either 1 or 2:  "))
if option == 1:
    celicius = int(input("Enter tempertaure in celicius degrees: "))
    faranheight = (9/5* celicius) + 32
    print(f" The {celicius} degrees are equal to {faranheight} degrees")
elif option == 2:

    faranheight = int(input("Enter tempertaure in Faranheight degrees: "))
    celicius= (9/5* faranheight) - 32
    print(f" The {faranheight} degrees are equal to {celicius} degrees")
else:
    print("Invalid option")



    # Qn. Your university decided to give 8% bonus to some employees if his/her years of service are more than 4.
    #  Then 5% bonus for the employees whose years of servce are 3. Else no bonus.
    #  Write a program that asks the employees for thir salary and thier years of service and display the net bonus  amount.
    #  Make sure you run the program until you decide ti quit.


while True:
        i = 1
    
        salary = int(input("Enter your salary: "))
        years_of_service = int(input("Enter your years of service: "))


        if years_of_service > 4:
            net_bonus = (8/100 * salary)
            final_pay = salary + net_bonus
            print( f"Your net bonus is {net_bonus} and you final pay is {final_pay}")

        elif years_of_service == 3:
            net_bonus = (5/100 * salary)
            final_pay = salary + net_bonus
            print( f"Your net bonus is {net_bonus} and your final pay is {final_pay}")

        else:
            net_bonus = 0
            final_pay = salary + net_bonus
            
            print(f"Your net bonus is: {net_bonus}")

            i = int(input(" Enter 1 to continue or any number to quit."))
        if i != 1:
            break
            



# Qn. Create a program that allows the user to deposit, withdraw and ceck their balance. The process should continue until the user chooses to quit.

print("Welcom to SACCO!")

while True:
     print('Choose options either: \n1. Deposit \n 2. Withdraw \n  3. Balance \n 4. Quit')
   
     initial_balance = 0
     choices = input("Enter your options here: ")
     if choices == '1':
          print('Preocessing........ ')
          deposit_amount = int(input("Enter amount: "))
          total_balance = initial_balance + deposit_amount
          print(f"You have deposited {deposit_amount} and your account balance is {total_balance}")

     elif choices == '2':
          print('Preocessing........ ')
          withdraw_amount = int(input("Enter amount: "))
          balance = total_balance - withdraw_amount
          print(f"You have withdrawn  {withdraw_amount} and your account balance is {balance}")


     elif choices == '3':
          print(f"Your account balance is {total_balance}")

     elif choices == '4':
          break
     

     else:
          print('You have entered a wrong choice please try again later!')

          
            
          


          



