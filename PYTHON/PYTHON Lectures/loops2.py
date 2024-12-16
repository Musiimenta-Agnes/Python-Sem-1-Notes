# LOOPS.

 # In marks below, loop throg the variable marks, and print the output.
marks = [60,70,80]
for mark in marks:
    print(mark)

# Calculate thee total sum of the marks above using a function.
marks = [60,70,80]
def total_marks():
    sum = 0
    for mark in marks:
        sum+=mark
    print(f"The total sum of the marks is : {sum}") # Make sure the print is at the same line with 'for' vertically not the line of the sum.
total_marks()



# ---------RANGE FUNCTION.---------
# This takes in parameters as start, stop and step.
# Range is also built on the for loop.
# The output starts from zero also.
# Basic apporoach


# Basic Examples:
# Qn. Using a loop, print all numbers from 0 to 6.(Ue a range function)

# Approach:
def numbers_of():
 for num in range(7): # By default, range starts from zero. Inotherwards, it orints +1
    print(num)

numbers_of()


    # Qn 2. Numbers between 0 and 10. 0 and 10 are inclussive
for num in range(11):# This is because it includes 10 also.
    print(num) 

    #Qn 3. Print numbers between 1 to 20.
for num in range(1,21): # This is done inorder to avoid the 0 because by default, range starts from zero.
    print(num)

    # Qn 4. Print the  following range of even numbers.(2,4,6,8,10)

def even_numbers():
    
    for x in range(2,11,2):
        print(x)

even_numbers()

# Qn 5 Print the range of these odd numbers, (3,5,7,9)

def odd_numbers():
    for y in range(0,10,3):
        print(y)
odd_numbers()




def odd_numbers():
    for y in range(2,11):
        if y % 2 !=0:
            print(y)
odd_numbers

      



