
# OPERATOR PRECEDENCE.
# This is an expressionthat determins the range/ order in which the operation is done.
# Operators with the higher precedence(Numbers with powers.) are always executed first.
# Numbers with powers are are executed first before using them anywhere.
# result = 3*4+5
# ie 
#BODMAS
result = 3*(4+5)
result_1 = 3*4+5
result_2 = 3*4+5-1
result_3 = 3*(4+5)-1
print(f"The output of result is: {result}")
print(f"The output of result two is: {result_1}")
print(f"The output of the third result is: {result_2}")
print(f"The output of the forth result is: {result_3}")


# What will be the output of the precedet such that we have 5*3**2 and (5+2)*2**2-10/2
result = 5*3**2
print(result)
result2 = (5+3)*2**2-10/2
print(result2)

number = 25/5+2*1
second_number = (25//5)+2*1
print(f"The result fo number is {number}")
print(f"The result fo the secod number is {second_number}")


# MORE  WORK