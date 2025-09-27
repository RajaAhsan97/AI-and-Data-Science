# Class Encapsulation Implmentation Tutorial
# In this Encapulation techniques is applied
# 1. data attributes includes Public and Private
# 2. Getters and Setters Instance Methods to access
#    and modify Private data attributes

class Students:
    # class attributes (Public)
    institute = "Saylani Mass IT"
    
    # constructor
    def __init__(self, name, course, roll_no, percentage):
        # data attributes

        # Public attributes
        self.name = name
        self.course = course

        # Private attributes
        self.__roll_no = roll_no
        self.__percentage = percentage

    # Instance Method
    def get_rollno(self):
        return self.__roll_no

    # Instance Method
    def set_rollno(self, roll_no):
        self.__roll_no = roll_no

    # Instance Method
    def get_percentage(self):
        return self.__percentage

    # Instance Method
    def set_percentage(self, percent):
        if percent >= 0 and percent <= 100:
            self.__percentage = percent
        else:
            print("Percentage Must be between 0 and 100")

# Creating class Instance
student1 = Students("Ahsan", "AI and Data Science", 40559, 70)

# Direct Access to Name and COurse which are public
print("Name: ", student1.name)
print("Course: ", student1.course)

# Access to roll_no and Percentage using Getter instance Method
print("Roll No: ", student1.get_rollno())
print("Percentage: ", student1.get_percentage())


# Update Public attributes Name and Course
student1.name = "Aamir"
student1.course = "Agentic AI"

# Update Private attributes roll_no and precentage
student1.set_rollno(40600)
student1.set_percentage(90)

print("Updated Records")
print(f"""
Name = {student1.name}
Course = {student1.course}
Roll No = {student1.get_rollno()}
Percentage = {student1.get_percentage()}
""")

# Trying to save percentage > 100 , Which result an error
student1.set_percentage(150)
