# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

mark_scored = int(input("Enter your mark in percentages: "))
if mark_scored >= 90:
    print('Grade A')
elif mark_scored >= 80:
    print('Grade B')
elif mark_scored >= 70:
    print('Grade C')
elif mark_scored >= 60:
    print('Grade D')
elif mark_scored >= 40:
    print('Grade E')
else:
    print('F')
