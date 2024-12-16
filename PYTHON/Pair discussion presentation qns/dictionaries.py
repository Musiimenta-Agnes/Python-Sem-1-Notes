 # -------DICTIONARIES--------
# # #Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.

student_information = {
    'name': 'Musiimenta Agnes',
    'age': 21,
    'grade': 'Grade A'
}

name = student_information['name']
print(name)


age = student_information['age']
print(age)


grade = student_information['grade']
print(grade)


# #Intermediate: Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def age_and_names(people_data):
    people = [names for names, age in people_data.items() if age >= 21]
    return people

people_data = { "Alice": 24, 
               "Bob": 19, 
               'Charlie': 30}
people = age_and_names(people_data)
print( f"The names of people with ages above 21 are {people}")





     
# # #Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana',], and calculates the total cost.
prices = {
    'apple': 0.5,
      'banana': 0.3, 
      'orange': 0.7
}
apple = 0.5
banana =  0.3
orange =  0.7
sum = 0
list = [apple, orange, banana]
for price in list:
    sum += price
print(f"The total cost is {sum}")
    


# #Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def word_count():
    words = sentence.split()
    count_words = {}
    for word in words:
        count_words[word] = word_count.get(word,  0) + 1
    return count_words
sentence = "hello world hello"
result = word_count()
print(result)