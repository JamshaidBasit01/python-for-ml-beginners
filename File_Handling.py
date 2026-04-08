#File handling refers to the process of performing operations on a file, such as creating, 
# opening, reading, writing and closing it through a programming interface. It involves managing
#  the data flow between the program and the file system on the storage device, ensuring that data
#  is handled safely and efficiently.

#Opening a File
#To open a file, we can use open() function, which requires file-path and mode as arguments.

f=open("geek.txt","r")
print(f)

##This code opens file geek.txt in read mode. If the file exists, it returns a file object connected
#  to that file; if the file does not exist, Python raises a FileNotFoundError.

##Closing a File
#The file.close() method closes the file and releases the system resources. If the file was opened in 
# write or append mode, closing ensures that all changes are properly saved.
f.close()

#Checking File Properties

#Once the file is open, we can check some of its properties:
f=open("geek.txt","r")
print(f.name)
print(f.mode)
print("Is Close?",f.closed)
f.close()
print("Is Close?",f.closed)

#Reading a File
#Reading a file can be achieved by file.read() which reads the entire content of the file. After 
# reading, it’s good practice to close the file to free up system resources.

f=open("geek.txt","r")
content=f.read()
print(content)
f.close()

#Writing a File
#In Python, writing to a file is done using the mode "w". This creates a new file if it doesn’t exist,
#  or overwrites the existing file if it does. The write() method is used to add content. After writing,
#  make sure to close the file.

f=open("geek.txt","w")
f.write("My name is Jamshaid Basit\n")
f.close()

#"w" mode opens the file for writing (overwrites existing content if the file already exists).
#write() method adds new text to the file.
#When using with, the file closes automatically at the end of the block.

#Using with Statement
#Instead of manually opening and closing the file, you can use the with statement, which automatically 
# handles closing. This reduces the risk of file corruption and resource leakage.

with open("geek.txt","r") as file:
    content=file.read()
    print(content)


##Read Lines in file
with open("geek.txt","r") as file1:
    content=file1.readline()
    print(content)

##Append (a)
# It does not overright the file, it add one more line in exisiting file

with open("geek.txt","a") as file2:
    file2.write("\nI am ML/AI Engineer")
    print(file2.tell())


#CSV FILE HANDLING
##Reading CSV File

import csv
with open("data.csv","r") as data0:
    reader=csv.reader(data0)
    for row in reader:
        print(row)

## Wriitng CSV File
with open("data2.csv","w",newline="") as data00:
    writer=csv.writer(data00)
    writer.writerow(["name","age"])
    writer.writerow(["Jamshaid",20])
