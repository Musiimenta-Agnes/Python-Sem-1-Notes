# LOGICAL OPERATORS

# Logical operators aree special key words that help us to connect and compare different conditions.
#The main logical operators are >>>

#  and. ----For this operator, both conditions must be true
# not. -----For this operator, this reverses the true values of the condition
#  or. ----- For this operator, atleast one of the conditions is true


# Example:
# x = True
# y = False

# print(x and y) # False, this is because x is true and y is false and the 'and' condition implies that both are true.
# print(x or y) # True, This is because x is true and the 'or' operator implies that atleast one of them is true
# print(not x) # FFalse, This is beause x is and the 'not' operator implies the reverse of the condition.


#Practical Example

# Check weather certain groups of people qualify for the VIP section by considering whether 
# the person is above 18 years old and a member of the clan.


age = 18
membership_status = 'member'

inputed_age = int(input('Enter your age: \n'))
is_member = input(" Are you a clan member? yes/No: \n").upper() == 'YES'

if age>=18 and is_member:
    print('You are welcome to the VIP section!')
elif age>=18 and not is_member:
    print('Please you dont quarify to be in the VIP secton because you are not a clan member')

else:
    print('Sorry, you must be 18 years and above and also a clan member to qualify for the VIP section')


