# Hands-on exercise on List of Dictionaries and
# built-in methods (items(), update())

# Assignment 4: Write a menu-driven program to create a Student Records Management System using
#               List of Dictionaries
#  1. Add Student - Take name, roll number, course, marks and email (optional) as input and store them in a list
#  2. Display students - show all stored students in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update marks - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks or name
#  7. Update record with email (if not found)
#  8. Exit

# for storing students records
# Each student records should have {"Name": name, "Roll no": roll_no, "Marks": marks}
students_records = []
# forming the skeleton of dictionary for storing student record with default null values
keys = ["Name", "Roll no", "Course", "Marks"]     # Note: Email is optional
student = dict.fromkeys(keys, ' ')


# 1. Add Student
def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll no: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    std = student.copy()

    std.update(
        {
            'Name': name,
            'Roll no': roll_no,
            'Course': course,
            'Marks': marks
        }
    )


    # for email (optional)
    ch = input("Would you like to provide Email? [y/n]")
    if ch == "y" or ch == "Y":  # if yes
        # then get the email
        email = input("Enter Email: ")

        # now add email to dictionary
        std['Email'] = email

    elif ch == "n" or ch == "N":  # if no
        print("Saving record without Email...")        
    else:
        print("Invalid choice!!. Saving record without Email")
        
    students_records.append(std)
    print("Record saved successfully....")

# 2. Display students
def display_students():
    if not students_records:
        print("No records found. Enter records first")
    else:
        print("-----------------")
        print("Students Records")
        print("-----------------")

        # iterating over list elements
        for student in students_records:
            # iterating over dictionary's key-value pair
            for key, value in student.items():
                print(f"{key}: {value}")
            print("-----------------------")

# 3. Search students
def search_student():
    # check if student record is not empty
    if not students_records:
        print("Unable to search, Please enter records first....")
        return None, None
    else:
        roll_no = input("Enter roll no of student:")
        # Method1 -------------------------------------------------
##        for student in students_records:
##            if roll_no in student["Roll no"]:
##                found = True
##                return student, students_records.index(student)
##        # if not found the print the error message
##        return None, None
        # ---------------------------------------------------------

        # Method2 -------------------------------------------------
        found_record = ([(student, index) for index, student in enumerate(students_records) if roll_no == student['Roll no']] or [(None, None)])[0]
        return found_record
        # ---------------------------------------------------------

# 4. Update the marks using roll no
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        print("---------------------")
        print("Record Found")
        print("---------------------")
        for key, value in student_found.items():
            print(f"{key}: {value}")
        print("---------------------")

        # get marks to update
        update_marks = int(input("Enter marks to update:"))
        # now, update marks
        students_records[index].update({"Marks": update_marks})
        
        print("Record Successfully updated....")
    else:
        print("Record not found!! \nUnable to update")

# 5. Delete records by marks
def delete_record():
    student_found, index = search_student()
    if student_found is not None:
        # delete record
        students_records.remove(student_found)
        print("Deleted Record Successfully")
    else:
        print("Record not found!! \nUnable to delete")

# 6. Sort records
def sort_records(sort_choice):
    if sort_choice == 'a':
        # sort by name
        students_records.sort(key=lambda x:x['Name'])
    elif sort_choice == 'b':
        # sort by marks
        students_records.sort(key=lambda x:x['Marks'], reverse=True)

    else:
        print("Invalid choice to sort")

# 7. Update record with email
def update_email():
    student_found, index = search_student()
    if student_found is not None:
        email_status = student_found.get("Email", "Not Found")
        # If email is not found
        if email_status == "Not Found":
            email = input("Please provide Email: ")

            # add new key i.e. Email 
            students_records[index]["Email"] = email
            print("Email added successfully...")
        else:
            print(f"Email already exist: {email_status}")
            print("Would you like to update the existing email? [y/n]")

            ch = input("Enter your choice: ")

            if ch == 'y' or ch == 'Y':
                email = input("Provide the new email: ")

                students_records[index].update({"Email": email})
                print("Existing email updated successfully...")

            elif ch == 'n' or ch == 'N':
                print("Okay, you don't want the update the existing email. Its Fine....")
            else:
                print("Invalid Choice!!! Saving existing email....")
    else:
        print("No record found.\n Unable to Update")

while True:
    print("-----------------------------")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Update email.")
    print("8. Exit")
    print("-----------------------------")

    option = input("Enter your option:")

    if option == '1':
        # Add Student
        add_student()
    elif option == '2':
        # Display Students Records
        display_students()
    elif option == '3':
        # Search student record
        student_, _ = search_student()
        if student_ is not None:
            print("---Student found---")
            for key, value in student_.items():
                print(f"{key}: {value}")
        else:
            print("Record not found!!!")
    elif option == '4':
        # Update student record
        update_marks()
    elif option == '5':
        # Delete student record
        delete_record()
    elif option == '6':
        # sort records
        print("--------------------")
        print(" a. To sort by name.")
        print(" b. To sort by marks.")
        choice = input("Enter Your choice:")

        sort_records(choice)
    elif option == '7':
        update_email()
    elif option == '8':
        # Exit
        break
    else:
        print("Invalid choice!!!")
