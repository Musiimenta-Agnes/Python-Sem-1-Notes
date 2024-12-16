
#create a class, a class name starts with a capital letter and always in singular
# class Cohort:
#name
#description
#start date
#end date
#total students number


# Qn 1. Within a class called Cohort class, add a constructer in the Cohort class.
# Adding a constructor
class Cohort_class:
  def __init__(self,name, description, start_date, end_date, number_of_students):
      self.name = name
      self.description = description
      self.start_date = start_date
      self.end_date = end_date
      self.number_of_students = number_of_students


# Create a function/method to the class that prints the Cohort name, and the total number of students.
# Adding a method.
  def print_cohort_class_info(self):
    print(f"Cohort Name: {self.name}")
    print(f"Total number of Students: {self.number_of_students}")

      

 # Qn 3. Create a new instance/object of the cohort class.  

# New object/instance
cohort = Cohort_class(
   name = 'Musiimenta',
   description = 'Cohort4',
   start_date = '20th August',
   end_date = '26th June',
   number_of_students = 56
)
cohort.print_cohort_class_info()
