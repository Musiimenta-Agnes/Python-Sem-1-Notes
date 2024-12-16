
#  DATA COLLECTION


# The structures are;

# 1.)  LISTS

# ***** The list syntax;
# -------We define a variable name.
#---------Lists are defined using square brackets.
#---------Data stored must be of the same type.
# --------Lists are  mutable or changeble
#---------Lists with the indexing
#--------- Lists are array like structures.

# EXAMPLES.

student_names = ['Agnes', 'Phionah', 'Violah', 'Abias'] # Strings
student_marks = [90,78,76,89] # Integers
data = ['Angella', 70, 'Wandegeya'] # Mixed types 


# To access the whole list with the variable type.
print( student_names, type(student_names))


# Using the  positive indexes or indexing
print(student_names[0])# First item
print(student_names[1])# Second item
print(student_names[2])# Third item
print(student_names[3])# Forthh item



# Using negative indexing
print(student_names[-4])# First item
print(student_names[-3])# Second item
print(student_names[-2])# Third item
print(student_names[-1])# Forth item



# Adding another new items in the list.
# 1. At the end
student_names.append('Micheal')
print(student_names) # Micheal comes last

# 2. At a particular position
student_names.insert(2, 'Faith')
print(student_names) # The list is [Faith comes in the second position.]

# in the list. Peplace Abias with Asingwire Abias.
list = ['Agie', 'Abias', 'Dankani']
new_name = 'Asingwire Abias'
index = 1
list[index] = new_name
print(list) # The list has Asingwire Abias instead of Abias.