# Hands-on exercise on List and its built-in methods (append, index, remove, sort)

# Lab Task: Write a menu-driven program to create a Student Records Management System using
#               List and List methods
#  1. Add Student - Take name, roll number, subject and marks as input and store them into a list
#  2. Display students - show all stored students records in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update recored - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks
#  7. Exit

# for storing students records
# Each student should have [name, roll_no, course, marks]
students_records = []

# 1. Add student
def add_student():
    name = input("Enter student name:")
    roll_no = input("Enter student roll no:")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks:"))
    students_records.append([name, roll_no, course, marks])
    print("Student added successfully...")

# 2. display students
def display_records():
    if students_records:
        print("------------------")
        print("Students records")
        print("------------------")
        for student in students_records:
            print(f"Name: {student[0]}")
            print(f"Roll no: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
            print("-----------------------")
    else:
        print("No record found. Enter records first")

# 3. Search student from record
def search_student():
    # check if student record is not empty
    if students_records:
        roll_no = input("Enter roll no of student:")

        # Method1 ----------------------------------------------
        for index, student in enumerate(students_records):
            if roll_no == student[1]:  # roll no is at index 1
                #found = True
                return student, index    # students_records.index(student)
          # If not found then print the error message
        return None, None

    else:
        print("Unable to search. Please enter records first....")
        return None, None

# 4. Update the marks using roll no
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        # get marks and update record
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {student_found[0]}")
        print(f"Roll No: {student_found[1]}")
        print(f"Course: {student_found[2]}")
        print(f"Marks: {student_found[3]}")
        print("---------------")
        # get new marks to update
        update_marks = int(input("Enter marks to update:"))
        # update marks in records
        students_records[index][3] = update_marks
        print("Record Successfully updated...")
    else:
        print("Record not Found! \nUnable to update")
    
# 5. Delete records by marks
def delete_record():
    student_found, _ = search_student()
    if student_found is not None:
        # delete record i.e. remove found student record from the records list
        students_records.remove(student_found)
        print("Deleted Record successfully")
    else:
        print("Record not found! \nUnable to delete")
    

# 6. Sort records by marks
def sort_records():
    if students_records:
        # sort by marks [marks are saved at 3rd index of nested student record list]
        students_records.sort(key=lambda x:x[3], reverse=True)     # x = [name1, roll_no1, course1, marks1]  then x[3] will be marks1
        print("Records sorted by Marks successfully....")
        
    else:
        print("Empty Records!!! \nUnable to Sort")
    
while True:
    print("-----------------------------")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    option = input("Enter your option:")

    if option == '1':
        # Add Student
        add_student()
    elif option == '2':
        # Display Students Records
        display_records()
    elif option == '3':
        # Search student record
        student_, _ = search_student()
        if student_ is not None:
            print("---Student found---")
            print(f"Name: {student_[0]}")
            print(f"Roll no: {student_[1]}")
            print(f"Course: {student_[2]}")
            print(f"Marks: {student_[3]}")
        else:
            print("Record not found !!!")
    elif option == '4':
        # Update student record
        update_marks()
    elif option == '5':
        # Delete student record
        delete_record()
    elif option == '6':
        # sort records
        sort_records()
    elif option == '7':
        # Exit
        break
    else:
        print("Invalid Choice!!!")
