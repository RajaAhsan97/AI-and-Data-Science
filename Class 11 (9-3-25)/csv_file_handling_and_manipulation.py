# -----------------------------------------------------------------
# ----- .csv file Handling and data manipulation Tutorial -----
# This lesson include:
# 1. Read and write .csv file using csv module
# 2. Append data to existing csv
# 3. Modify and filter data
# 4. Perform basic data analysis 
# -----------------------------------------------------------------

# import csv module
import csv

# ------------------------------------------------------------------
### Step 1: Reading csv file ---------------------------------------
# ------------------------------------------------------------------
### Each row of the csv file is reads as list
##with open("students_50_records.csv", mode="r") as file:
##    data = csv.reader(file)
##
##    #print(type(data))
##    for row in data:
##        #print(type(row))
##        print(row)
# ------------------------------------------------------------------


# ------------------------------------------------------------------
### Step 2: Appending data to existing csv file [we use append mode]
### Note:  
###   For appending data (i.e. row)
###   1. we use writer.writerow() which writes a row adds a newline ('\n')
###   2. But if you don't use [newline=''], Python open() function will also
###      add its own newline.
###   3. This results in extra blank line
# ------------------------------------------------------------------
##with open("students_50_records.csv", mode="a", newline='') as file:
##    writer = csv.writer(file)
##
##    # write a row at a time
##    writer.writerow(['Waqas', '25', 'Male', '50.5'])
##    
# ------------------------------------------------------------------


# ------------------------------------------------------------------
### step 3: Write multiple rows ------------------------------------
# ------------------------------------------------------------------
### Multiple rows data
##rows = [
##    ["Usman", "23", "Male", "60.0"],
##    ["Saqib", "19", "Male", "70.1"],
##    ["Aleeza", "22", "Female", "90.0"],
##]
##
##with open("students_50_records.csv", mode="a", newline="") as file:
##    writer = csv.writer(file)
##
### ------------------------------------------------------------------
##    # write multiple rows to a csv file
##    writer.writerows(rows)

# ------------------------------------------------------------------

# ------------------------------------------------------------------
### step 4: Read Data from csv file in dictionary (Better Access) --
# ------------------------------------------------------------------
##
##with open("students_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##    # iterate over data
##    for row in data:
##        # firstly do this
##        #print(row)
##        # secondly do this
##        print(f"""
##            Name: {row['Name']})
##            Age: {row['Age']}
##            Gender: {row['Gender']}
##            Grade: {row['Grade']}
##        """)

# ------------------------------------------------------------------


# ------------------------------------------------------------------
### Step 5: Filtering Data (Only Males ) -- Filter Male candidates and
###                                         save their records into a new file
# ------------------------------------------------------------------

### for storing male students data 
##male_students = []
##
##with open("students_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##
##    count_male_rec = 0
##    count_female_rec = 0
##    for row in data:
##        if row['Gender'] == 'Male':
##            #print(row)
##
##            # Each student record is appended in dictionary format inside the list
##            male_students.append(row)
##
##            # count males
##            count_male_rec += 1
##        #else:
##        #    count_female_rec += 1
##
##    print(f"{count_male_rec} Male records found...")
##
### Now create new file for storing male students data
##with open("male_students_records.csv", mode="w", newline="") as file:
##    # Extract column names from keys of first student
##    column_names = male_students[0].keys()
##
##    writer = csv.DictWriter(file, column_names)
##
##    # write columns names to file
##    writer.writeheader()
##
##    # write rows (write multiple dictionaries at once)
##    writer.writerows(male_students)
##
##print("File of Male Students Records created successfully...")
    

# ------------------------------------------------------------------


# ------------------------------------------------------------------
### Step 6: Simple Analysis - Average Males and Females Age --------
# ------------------------------------------------------------------
##with open("students_50_records.csv", mode="r") as file:
##    data = csv.DictReader(file)
##
##    # store sum of male ages
##    male_age_sum = 0
##    female_age_sum = 0
##
##    # count records
##    count_male = 0
##    count_female = 0
##    
##    for row in data:
##        if row['Gender'] == 'Male':
##            male_age_sum += int(row['Age'])
##            count_male += 1
##        else:
##            female_age_sum += int(row['Age'])
##            count_female += 1
##
##    # used int() to convert calculated average age from float to integer
##    avg_age_male = int(male_age_sum / count_male)
##    avg_age_female = int(female_age_sum / count_female)
##
##    print("Males Average age: ", avg_age_male)
##    print("Female Average age: ", avg_age_female)
