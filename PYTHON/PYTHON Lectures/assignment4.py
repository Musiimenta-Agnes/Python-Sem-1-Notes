# Qn 1. Within a class called Cohort class, add a constructer in the Cohort class.
class Cohort_class:
   name = 'Musiimenta'
   description = 'Cohort4'
   start_date = '20th August'
print(Cohort_class)

# Adding a constructor
class Cohort_class:
  def __init__(self,name, description, start_date):
      self.name = name
      self.description = description
      self.start_date = start_date


Cohort_class = Cohort_class('Musiimenta', 'Cohort4', '20th August')

print(Cohort_class.name) 
print(Cohort_class.description)
print(Cohort_class.start_date)
        


# Create a function/method to the class that prints the Cohort name, and the total number of students.
# Adding a method.

class Cohort_class:
   def __init__(self,name, description, start_date):
    self.name = name
    self.description = description
    self.start_date = start_date


   def total(self):
            print(f'The total number of students is 59  {self.name}')
Details = Cohort_class('Musiimenta', 'Cohort4', '20th August')
Details.total()       

 # Qn 3. Create a new instance/object of the cohort class.  

# New object

class Cohort_class:
     def __init__(self,name, description, start_date):
          self.name = name
          self.description = description
          self.start_date = start_date
     def Cohort_class_func(self):
      print(self.name, self.description, self.start_date)
class Subject(Cohort_class):
     def __init__(self, name, description, start_date ):
        super(). __init__(name, description, start_date)
        self.Subject = 'Computer Science' 
details = Subject('Musiimenta', 'Cohort4', '20th August')
print(details.Subject)