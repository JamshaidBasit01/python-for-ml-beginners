#What is Exception Handling?
#Exception = Runtime error (program crash ho jata hai)

#Examples:

#Division by zero
#File not found
#Invalid input

##try/except
try:
    x=int(input("Enter your value:"))
    print(10/x)
except:
    print("Error Occured")

#Specific Exceptions
#Catching specific exceptions makes code to respond to different exception types differently. 
# It precisely makes your code safer and easier to debug. It avoids masking bugs by only reacting 
# to the exact problems you expect.

try:
    x=int(input("Enter the value:"))
    print(10/x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Value")

#Multiple Exceptions (One Block)
try:
    x=int(input("Enter the value:"))
    print(10/x)
except(ZeroDivisionError,ValueError):
    print("Error Occured")

#Using else
#Runs when no error occurs
try:
    x=int(input("Enter the value:"))
    print(10/x)
except ZeroDivisionError:
    print("Cannot be divid by 0")
except ValueError:
    print("Invalid Value")
else:
    print("Done")

#Using finally
#Runs always (error ho ya na ho)

try:
    f = open("geek.txt")
except:
    print("Error")
finally:
    print("This always runs")

##try: Runs the risky code that might cause an error.
##except: Catches and handles the error if one occurs.
##else: Executes only if no exception occurs in try.
##finally: Runs regardless of what happens useful for cleanup tasks like closing files.

##Raising Custom Exceptions
def check_age(age):
    if age<18:
        raise ValueError("Not Eligible for vote")
check_age(10)

##DEBUGGING BASICS

#Using pdb (Python Debugger)
import pdb
z=5
pdb.set_trace()
y=z+5

##Logging
import logging
logging.basicConfig(filename="app.log",level=logging.INFO)
##Level
#1. INFO(General)
#2. DEBUG(Detailed Info)
#3. WARNING(Something Unexpected)

#4. CRITICAL(Ver Serious)
logging.info("Started")