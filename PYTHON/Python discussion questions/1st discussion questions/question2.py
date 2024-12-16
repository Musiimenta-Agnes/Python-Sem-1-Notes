# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 


def calculate_bmi():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
    BMI = (weight/height)
    if BMI < 18.5:
        print('Under weight')
    elif 18.5 <= BMI <= 24.9:
        print('Normal weight')
    elif 25.9 <= BMI <= 29.9:
        print('Over weight') 
    else:
        print('Obese')
calculate_bmi()
 

# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)


def volume_of_cylinder():
    radius = int(input("Enter the radius r: "))
    height = int(input("Enter the height h: "))
    import math
    pie = math.pi
    volume = pie*radius**2*height
    print(f"The volume of a cylinder with radius {radius} and height {height} is equal to {volume:.2f} ")
volume_of_cylinder()