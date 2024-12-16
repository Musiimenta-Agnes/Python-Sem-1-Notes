# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user


def numbers ():
    total_sum = 0
    while True:
        number = int(input("Enter number that is greater than 0: "))
        if number == 0:
            break
        total_sum += number
    print(f" The total sum of the nmbers is {total_sum}")
numbers()
    

# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

def even_numers():
    for num in range(1,101):
        if num %2 == 0:
            print(num)

even_numers()
