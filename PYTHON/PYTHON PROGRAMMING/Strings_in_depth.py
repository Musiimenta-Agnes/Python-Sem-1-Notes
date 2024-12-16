# MORE ABOUT STRINGS

# Strings in arry like structure
#Arrays in python are lists
#In lists we use []
#in arrays, the starting point is always a '0'

marks = [74,96,89,76,] # example of a list

#Examples

#1. Access the variable 'n' in the name Agnes
name = 'Agnes'
print(name [2])

#2. Print the last character in the name Agnes
name = 'Agnes'
print(name[4])



#2.  LOOPING THROUGH STRINGS
# here we use 'for' and 'in'
#Mind about the indentantion

for character in name:
       print(character)

address = "Kamuwokya"
for character in "Kamuwokya":
       print(character)



school = "Kisasi College"
for character in school:
       print(character)
     


#3. SLICING IN STRINGS
# This is the accessing of ranges of a character in a string.

#SLICING OF IN
#Example
name = "O s i r i a h" # Access the characters s and h
#Access siriah in osiria
print(name[1:7]) # 'siriah'

#Access si in name Osiriah
print(name[1:3]) # 'si'

#Access sir in name Osiria
print(name[1:4]) # 'sir'
# In order to access the letter you want and keep it you do plus one '+1"



#SLICE OF MESSAGE
print(name[ :4]) # In this case, wen you dont specify the first index, it always carries all the first ones up to the end index-1
#The out put here is 'Osir'
message = "Hello"
print(message[0:3])# 'Hel'


#NEGATIVE INDEXING
message = "Hello"
print(message[-1])# 'o'
print(message[-1:-5])# 'Space'
print(message[-4:-4])# 'space'
print(message[-5:-3])# 'He'
print(message[-4: ])# 'ello' this ones keeps all the items after the start index.
print(message[4: ])#'o'
print(message[4])




#INDEXING OF LISTS
#This involves lists while indexing


# Forexample printthe second word in the the following list.
list = ["apple", "banana","cherry"]
print(list[1]) # This will print out "banana" because its in the seond position of 1.




#Print the third, forth and the fifth  item in the following list
fruits = ['apple', 'baanan', 'cherry', 'orange', 'Kiwi', 'melon', 'mango']
print(fruits[2:5]) # Thhis will return items in position 2 and 5. 
#But remember 5 is NOT inclussive because the index starts from 0

#print the fruits in the third, forth, fifth and the sixth
print(fruits[2:6])
#Write a program that out puts banan,cherry,orange,kii,melon and mango
print(fruits[1:7])


#  F. STRINGS.(FORMATTING STRINGS)
name = "Dankani"
age = 21
print(" My name is " + name + " My age is " + str(age))
#Using formatting
print(f" My name is {name} and am {age} years old ")

weight = 58.41318
print(f" My name is {name}, I am {age} years old and I am {weight:.2f} meters tall ")

total_cost = 300000 # This should be 300,000
print(f"The new dress I bought was at {total_cost:,} shillings ")# This is done to put a comma to within the cost


#STRING METHODS
#1. Len() # Length
name = "Musiimenta" # 10
total_length = len(name)
print(total_length)

address = "From  Kamuwokya"
address = len(address)
print(address)

school = "kisaasi college"
school = len(school)
print(school)



#2. upper() # Upper case
name = "asingwire"
print(name.upper())

# 3. LOWER CASE
district = "KANUNGU"
print(district.lower())

# #3. ESCAPE SEQUENCES: These always start with \n
name = "agie\n Musiimenta\n"
print(name) # New line

address = "Kampala\t Ditrict\t" 
print(address) # Space between (Tab)
name = "My\name\tis\tMusimenta\tAgnes\tan\tI\tcome\tfrom\tWandegeya"
print(name)

age = "45\\ Height\\"
print(age) # 

       



