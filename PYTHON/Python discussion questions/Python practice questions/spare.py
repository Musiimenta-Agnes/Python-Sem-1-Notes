def Sacco_transaction():
      account_balance = 0
      run = 1
      while run == 1:
            

            print('Welcome to WITU Guild Sacco')
            print('1. Deposite')
            print('2. Withdraw')
            print('3. Balance')

            student_choice = int(input('Enter your selection (1,2 or 3): \n'))


            if student_choice == 1:
                  print('\n Processing....')
            deposite_amaount = int(input('\n Enter your amount to be deposited: '))
            if deposite_amaount < 1000:
                  print('\n Minimum amount to deposite is 1000')
            else:
                  account_balance += deposite_amaount
                  print(f" Dear student, you have deposited {deposite_amaount} and your account balance is {account_balance + deposite_amaount:}")


            if student_choice == 2:
                    print('\n Processing...')
                    withdraw_amount = int(input('Enter your amount to withdraw: '))

            if account_balance == 0:
                  print('Account balance is 0')
            elif withdraw_amount > account_balance:
                   print('Withdraw failed, insuffecient Funds')
            elif withdraw_amount < 500:
                  print('Minimum withdrw amount is 500, please try again')


            else: account_balance -= withdraw_amount
            print(f'you have successfuly withdrawn {withdraw_amount} and your account balance is {account_balance-withdraw_amount} ')

            if student_choice == 3:
                  print(f'\n Your accoutn balance is {account_balance:,}')
            else:
                  print('\n You have entered a wrong choice please select fro either 1,2 or 3')
              
            run = int(input("Enter 1 to continue or any number to exit:  "))

            if run!=1:
                  
                  print('Thanks for using our Sacco.')

Sacco_transaction()
                        





             
                  


