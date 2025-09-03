##File Handling and data manipulation Tutorial
##
##Description:
##    As we know that performing File I/O operation on a text file in Python
##    represents the content of file to be treated as strings. So the basic
##    string operations can be applied to it also...
## ===========================================================================
##  Task 1: Read all lines from a file and print
##  Task 2: Replace a word in File content
##  Task 3: Delete Specific line
##  Task 4: Insert line at specific position
##  Task 5: Read lines from a file and get the line starting with letter 'O',
##          convert all characters to uppercase and save it to new file
##  Task 6: Search name and count repeating names from the file
## ===========================================================================

## ----------------------------------------------------------------------------
### Task 1: Read all lines from a file and print ------------------------------
## ----------------------------------------------------------------------------
##with open("file data manipulate.txt") as f:
##    lines = f.readlines()
##    # lines data in form: ["first_line\n, second_line\n", "Third_line"]
##
##    for line in lines:
##        print(line.strip('\n'))


## ----------------------------------------------------------------------------
### Task 2: Replace a word in File content --------------------------------------
## ----------------------------------------------------------------------------
### read data from file
##with open("file data manipulate.txt", mode="r") as f:
##    data = f.read()
##
##print("data:\n",data)
##
##new_data = data.replace("Tahir", "Waqas")
##print("new Data:\n",new_data)
##
##with open("file data manipulate.txt", mode="w") as f:
##    f.write(new_data)

## ----------------------------------------------------------------------------
### Task 3: Delete Specific line ----------------------------------------------
## ----------------------------------------------------------------------------
##
##with open("file data manipulate.txt", mode="r") as f:
##    lines = f.readlines()
##
##removed_line = lines.pop(1)
##
##with open("file data manipulate.txt", mode="w") as f:
##    f.writelines(lines)


## ----------------------------------------------------------------------------
### Task 4: Insert line at specific position ----------------------------------
## ----------------------------------------------------------------------------
##with open("file data manipulate.txt", mode="r") as f:
##    lines = f.readlines()
##
### insert a line to be inserted in the list position
##lines.insert(1, "Osama\n")
##
##with open("file data manipulate.txt", mode="w") as f:
##    f.writelines(lines)

## ----------------------------------------------------------------------------
### Task 5: Read lines from a file and get the line starting with letter 'O',
### convert all characters to uppercase and
### save it to new file
## ----------------------------------------------------------------------------
##with open("file data manipulate.txt", mode="r") as f:
##    lines = f.readlines()
##
### Method 1 ------------------------
####get_lines = []
####
####for line in lines:
####    cleaned_line = line.strip()
####    if cleaned_line[0] == 'O':
####        get_lines.append(cleaned_line.upper() + "\n")
### ---------------------------------
##
### Method 2 ------------------------ [List comprehension]
##get_lines = [line.strip().upper()+"\n" for line in lines if line.strip()[0] == 'O']
###-----------------------------------
##with open("file data manipulate2.txt", mode="w") as f:
##    f.writelines(get_lines)

## ----------------------------------------------------------------------------
### Task 6: Search name and count repeating names from the file
## ----------------------------------------------------------------------------
##with open("file data manipulate.txt", mode="r") as f:
##    lines = f.readlines()
##
##count_records = 0
##for line in lines:
##    if line.strip() == "Ahsan":
##        count_records += 1
##
##print("Number of records: ", count_records)
