##Text File Handling Tutorial -1 
##
##1. File open
##2. File read
##3. File write
##4. File close

### ---------------------------------------------------
### Section 1: ----------------------------------------------------------------------------------
### opening a text file and read all contents
### Syntax: open("File path", mode)
### ---------------------------------------------------
##file = open("sample file.txt", mode='r')
##
### read all content from file
##data = file.read()
##
### display data
##print(data)
##
### Empty characters are read in this line, because file pointer is updated at the end of file
##data = file.read()
##print(data)
##
##
##file.close()

### ---------------------------------------------------
### Section 2: ---------------------------------------------------------------------------------------
### File opening Recommended method (It automatically closes a file)
### ---------------------------------------------------
##with open("sample file.txt", mode="r") as f:
##    data = f.readlines()
##    print(data)



### ---------------------------------------------------
### Section 3: -----------------------------------------------------------------------------------
### opening a text file and read 'n' characters
### ---------------------------------------------------
##with open("sample file.txt") as file:
##
##    # read 'n' characters
##    data = file.read(6)
##    print(data)
##
##    data = file.read(2)
##    print(data)
##
##    data = file.read()
##    print(data)


### ---------------------------------------------------
### Section 4: -----------------------------------------------------------------------------------
### open a text file and read a line
### ---------------------------------------------------
##with open("sample file.txt", mode = 'r') as file:
##
##    # read first line
##    data = file.readline()
##    print(data)
##    print(len(data))
##    # read second line
##    data = file.readline()
##    print(data)
##
##    # read third line
##    data = file.readline()
##    print(data)
##
##    # read 'n' characters from a file
##    data = file.readline(2)
##    print(data)


### ---------------------------------------------------
### Section 5: --------------------------------------------------------------------------------------
### open a text file file and read a lines into a list
### ---------------------------------------------------
##file = open("sample file.txt", mode = 'r')
##
### read all lines into a list
##data = file.readlines()
##print(data)
##
### to access each line
##print("Line1: ", data[0])
##print("Line2: ", data[1])
##
##file.close()

### ---------------------------------------------------
### Section 6: ---------------------------------------------------------------------------------------
### open a file, if file not exist then creates it and write data to it
### ---------------------------------------------------
##with open("sample file1.txt", mode="w") as f:
##    data = "Python Programming Fundamentals (PPF)"   # data to write
##    f.write(data)
##
##
### Now view new data
##with open("sample file1.txt", mode="r") as f:
##    new_data = f.read()
##    print("New data: ", new_data)
    
### ---------------------------------------------------
### Section 7: ---------------------------------------------------------------------------------------
### open a file, if file exists, then overwrite data in it
### ---------------------------------------------------
##with open("sample file1.txt", mode="w") as f:
##    data = "Now we are..."
##    f.write(data)
##
### Now view the new data
##with open("sample file1.txt", mode="r") as f:
##    data = f.read()
##    print(data)


### ---------------------------------------------------
### Section 8: ---------------------------------------------------------------------------------------
### open an existing file, and write lines from a list of strings
### ---------------------------------------------------
##with open("sample file1.txt", mode="w") as f:
##    data = ["line1\n", "line2\n", "line3"]
##    f.writelines(data)

### ---------------------------------------------------
### Section 7: ---------------------------------------------------------------------------------------
### open a file, and append data to the end of file
### ---------------------------------------------------
##with open("sample file1.txt", mode="a") as f:
##    data = "this line is appended to the end of file"
##    f.write(data)

### ---------------------------------------------------
### Section 8: ---------------------------------------------------------------------------------------
### open a file, and append data to the end of file using writelines
### ---------------------------------------------------
##with open("sample file1.txt", mode="a") as f:
##    data = ["\nnew line1\n", "new line2"]
##    f.writelines(data)


### ---------------------------------------------------
### Section 9:  r+ (read write) ---------------------------------------------------------------------
### open a file (file must exist), then Read and write
### It allows you to read and write without erasing whole file content (unlike 'w')
### ---------------------------------------------------
##
##with open("sample file1.txt", mode="r+") as f:
##    existing_data = f.read()
##    print("Before write:")
##    print(existing_data)
##
##    new_data = "\nThe quick brown fox jumps over the lazy Dog."
##    f.write(new_data)
##
##    # set pointer to the begining of the file
##    f.seek(0)
##
##    modified_data = f.read()
##    print("Updated data:")
##    print(modified_data)


### ---------------------------------------------------
### Section 10: w+ (write read) ----------------------------------------------------------------------
### creates a file if not exist, otherwise open a file and overwrite it
### ---------------------------------------------------
##with open("sample file1.txt", mode="w+") as f:
##    f.write("This is the example of w+ mode")
##
##    # set pointer to the begining of the file
##    f.seek(0)
##
##    data = f.read()
##    print(data)


### ---------------------------------------------------
### Section 11: a+  (append and read) ---------------------------------------------------------------
### Create file if not exist, otherwise append at the end of file
### ---------------------------------------------------
##with open("sample file1.txt", mode="a+") as f:
##    f.write("this is the example of a+ mode")
##
##    # set pointer to the begining of the file
##    f.seek(0)
##
##    # read content
##    data = f.read()
##    print(data)

