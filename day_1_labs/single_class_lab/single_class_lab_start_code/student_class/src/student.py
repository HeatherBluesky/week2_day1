class Student:
    def __init__(self, input_student_name, input_cohort):
        self.name = input_student_name
        self.cohort = input_cohort
        

# functions got in here
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, Language):
        return ("I love ")  + Language
    
   