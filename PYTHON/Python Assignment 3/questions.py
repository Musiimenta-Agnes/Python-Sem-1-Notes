#From this list, ['Sandra', 'Patricia', 'Phionah', 'Anitah'] and marks marks = [80,56,78,90].


# a).Print Patricia, Faith, Phionah and Anitah.
student_list = ['Sandra', 'Patricia', 'Phionah', 'Anitah']
student_marks = [80,56,78,90]

student_list.insert(2, 'Faith')
student_list.remove('Sandra')
print(f"TThe updated list of with Faith added and Sandra removed is : {student_list}")



 # b). Add the name Masha at the 4th position.
student_list = ['Sandra','Patrica', 'Phionah', 'Anitah']
student_list.insert(4, 'Masha')
print(f" The updated list with Masha in the third position is : {student_list}")


# c). Update the name Phionah to Phionah Aladinah.

new_name = 'Phionah Aladinah'
index = 2
student_list[index] = new_name
print(f"The new updated list with the name Phionah replaced with Phionah Aladinah is : {student_list}")


# d). Display the length of the students list. 
length = len(student_list)
print(f" The length of the student list is : {length}")


# #e). Print all the student names using a for loop.

for x in student_list:
    print(x)



# f). Calculate the total marks for the student marks variable and the answer should be 304.

sum = 0
student_marks = [80, 56, 78, 90]
for mark in student_marks:
        sum+=mark
print(f"The total marks for all student marks is {sum}")