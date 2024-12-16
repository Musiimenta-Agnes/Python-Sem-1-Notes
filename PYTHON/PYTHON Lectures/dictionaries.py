# DICTIONARIES.
#=======SYNTAX========
#  The syntax or how they are represented as: 
# A dictionary stires different items using a key value pair.
# The keys are always on the left.
# The keys can never be key words.
# Clear removes everything from the dictionary
#  ******** The most questionable parts about dictionaries;
#------Syntax
#------Acess items
#------Remove items
#------Add items
#------Change items
#------Loops


student_details = {
    'name' : 'Gilian',
    'age' : 21,
    'location' : 'Wandegeya'
}

fruits = {
    1 : 'Apple',
    2 : 'Mango',
    3 : 'Orange',
}

#  =======ACCESS =====

# Qn 1. Acess Gillian:
student_details['name']
print(student_details)

# Qn 2. Access 21
student_details['age']
print(student_details)

# Qn 3. Access Wandegeya.
student_details['location']
print(student_details)


# Qn 4. Print the keys of the student details dictionary.
print(student_details.keys())

# Qn 5. print the lenght of the dictionary.
print(len(student_details))

# Qn 6. Add a key contact to the student's dictionary.
student_details['contact'] = '0742443850'
print(student_details)



# =====CHANGING ITEMS=======

# Qn 7. Update the name Gillian to Apio Gillian.
student_details['name'] = 'Apio Gillian'
print(student_details)

# Qn 8. Acces all the values of the dictionary.
print(student_details.values())

# =======REMOVING========

#Qn 9. Remove the contact key from the dictionary 

student_details.pop('contact') # We use pop to remove keys from a dictionary
print(student_details)

#Qn 10. Add the name Musimenta in the dictionary

student_details['second_name'] = 'Musiimenta'
print(student_details)







# QUESTION ONE
#Create an empty dictionayr clled dict.

dict = {}
   

#Add the pairs 'Apple', and 1, 'banana', and 2.0, and'Cherry'and 'iii'
dict['Apple'] = 1
dict['banana'] = 2.0
dict['cherry'] = 'iii'
print(dict)


#Repalce the value of Apple with 'I'

dict['Apple'] = 'I'
print(dict)

#Remove entry of banana
dict.pop('banana')
print(dict)

#Add entry date with value 4.

dict['entry'] = 4
print(dict)

# Accessing all the keys and thier values in the dictionary
print(dict.items())


# Accessing all the avlues of the dictionary

print(dict.values())

# Accessing the key in the dictionary
print(dict.keys())

# Updating the dictionary
print(dict.update())
#






