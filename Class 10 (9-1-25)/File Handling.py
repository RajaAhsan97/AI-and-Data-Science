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
