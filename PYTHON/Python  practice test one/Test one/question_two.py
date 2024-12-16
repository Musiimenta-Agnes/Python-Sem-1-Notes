# Question two.

# Using a function, create a program that calculates the volume of a cylinder.


import math

def volume_of_a_cylinder():
    radius = int(input("Enter the radius: "))
    height = int(input("Enter the height: "))
    pie = math.pi
    volume = 22/7 * radius**2 * height

    print(f"The volume of a cylinder with radius {radius} and height {height} is {volume:.2f}.")

volume_of_a_cylinder()

   
