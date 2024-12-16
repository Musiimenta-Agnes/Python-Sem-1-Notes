#These are used to store data or they are called ata containers
# RULES OF VARIABLES

# 1. variable names start with letters or underscores(_)
age=20
_age=20
marks=50
_marks=57


#2. variable names contain letters, numbers and underscores
age=20
_age=29
age4=56


#3. variables are case sensetive forexample A and a are different things.
Total=674
total=674


#4.  Avoid using pyhthon keywords as variable names 
#if,were,else,while etc


#5.  choose meaningfull variable names


# variable naming conventions


#1.    SNAKE CASE
#Here words are seperted by underscores and letters are always in lowercase
#ie my_name_is_musiimenta_agnes
first_name = 'musiimenta_agnes'
last_name = 'Agnes'
my_age = '20'



#2.    CAMEL CASE
#The first letters of the word ust be in lower case and all the other words in the same sentence or statement 
# should tart with capital letters or upper case and this does not use underscores 
#ie  myNameIsMusiimentaAgnes
firstName ='Asingwire'
lastName ='Abias'
myAge = 25

#Accessing the variable values
print(firstName)
print(lastName)
print(myAge)

#3.   PASCAL CASE
#The first letter of the first words must be in upper case throughout and this has no space and does not use underscores
#ie MyNameIsMusiimentaAgnes
FirstName ='Nahurira'
SecondName ='Osiria'



# Accessing Variable Values.
print(first_name)
print(last_name)
print(" Name: " + FirstName + SecondName + " Age: " + str(myAge ))


# You can also access the variables using the 'f' string formatter

print(myAge)
print(F"{FirstName} {SecondName} {myAge} {firstName} {lastName} {myAge }")

    
    # WORKING WITH INPUT
first_name = input("Enter your name:\t")
second_name = input("Enter your name:\a")
_age = input("Enter your age:\a")
print(first_name)
print(second_name)
print( _age)



