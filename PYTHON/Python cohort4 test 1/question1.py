# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
x1 = 3
x2 = 4
y1 = 8
y2 = 10
import math
distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(distance)


# Question 1(ii)
# Write a Python program to find maximum between three numbers.
numbers = [1,3,5]
for x in numbers:
    print(f"The maximum value is {max(numbers)}")

