
# FUNCTIONS.

#--------- They are used in programming to perform a particular task.
# --------A method and a function are always the same.

# --------The syntax of crating a function (Rules  to follow when creating a function).

# 1.Define and use a def function_name():
#        body
#       We use pass if there is no function
# Then call the function outside the body. (Use the same naming convesion and in the same line with def at the biginning).

# PARAMETERS
# ------These are the data or information  where values are passed into the function to perform a particular task (Variables tht store values)

# ARGUMENTS (Values)
#-------These are the values  to be used in the function. ie.(4) 


#EXAMPLE

# 1). Create a function that returns the main components of functions in python.
# The out put should say main components are Parameters,


# def function_basics():
#     print(' The main components of functions are : \n  Function parameters \n  Function arguments \n  Function body \n Function names')


# function_basics()



# # # 2). Create a function  that returns  your student name, registration number and student age.

# def student_details():

#     student_name = 'Musiimenta' # This is a local ariabe
#     student_reg = '2024/DSC/090' # This is a local variable
#     student_age = 21             # This is a local variable

#     print(f'The student name is {student_name}')
#     print(f'The student regestration number is {student_reg}')
#     print(f'The student age is {student_age}')


# student_details() # Call the function






#  # ----------- USING PARAMETERS IN THE QUESTIONS------------.
#  # Whenever we have parameters, we dont re-define the variables again because the parameters are the variables.

#  # 3.) Create a function that returns your student name , regestration number and age as parameters.( This one has parameters).


# def student_data (name, age, reg_number):
#     print(f"{name}, {age}, {reg_number}")


# student_data( 'The student details are ' 'Musiimenta', 21, '2024/DSC/0051/SS') # You indicate the values (arguments) in the brackets at the time calling the functions
    



# # RETURN VALUES
# # This also works as print.
# # 

# # create a program that returns your name.
def my_name ():
    return 'Agnes'
# To view the output, 
name = my_name()
print(name)




# # Aporoach two

# def name():
#     my_name = 'Musiimenta Agnes Angella' 
#     return my_name # This returns the parameters (variabels)

# name()
# the_name = name() # This is going to help you view the output.
# print( f" My name is {the_name}")


# # 4). Create a function that calculates the area of a triangle. The base and height must be function parameters.

# def area_of_triangle (base, height):

#     area = int(1/2*base*height)
#     print(f"The are of the triangle with base {base} and height {height} is {area}")

# area_of_triangle(4,5)



# # Approach two. (( When the user is to enter the values from the keyboard.)) This strictly cannot allow the use of parameters.
# def area_of_triangle ():
#     base = int(input(" Enter the base: "))
#     height = int(input(" Enter the height: "))
#     area = int(1/2*base*height)
#     print(f"The area of the triangle with base {base} and height {height} is {area}")

# area_of_triangle()




# Qn. Write a function double_number(num) that takes an integer and returns its duble.

# def double_number(num):
#     return num*2
# the_number = double_number(2)
# print(f'The double of the number 2 is:  {the_number}')


# Qn. Write a function that returns the sum of 5 and 7
# def add_numbers(a,b):
#     return a+b
# num1= 5
# num2 = 7
# numbers = add_numbers(num1,num2)
# print(numbers)


# Method 2
# Doing the above qn using print just and parameters.
# def total(b,c):
#     print(f" {b} {c}")
# total('b represents Brenda ans c represents Cetty')











# def adding_numbers():
#     a = 3
#     b = 4
#     sum = a + b
#     print(sum)
# adding_numbers()



