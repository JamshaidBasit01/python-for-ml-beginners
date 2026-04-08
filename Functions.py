#What is a Function?
#A function is a reusable block of code that performs a specific task.
#Benefits:
#Code reuse
#Cleaner programs
#Easy debugging

##Function Defination

def greet():
    print("Hello Jamshaid")

## Call Function
greet()

##Return Statement (return)

#Used to send value back from function.

def sum(a,b):
    sum1=a+b
    return sum1
##Call Function
print(sum(2,5))

#Key Points:
#return ends function execution
#Can return multiple values

def calc(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
##Call the function
addition,subtraction=calc(10,5)
print("Sum of two numbers are:",addition)
print("Subtraction of two numbers are:",subtraction)

##Arguments (Types of Inputs)
# Positional Arguments

def sum(a,b):
    sum1=a+b
    return sum1
##Call Function
print(sum(2,5))

# Keyword Arguments

def sum(a,b):
    sum1=a+b
    return sum1 
print(sum(a=5,b=10))   ## This is Keyword Arguments

##Default Arguments
def greet(name="Junaid"):
    print("Hello",name)
greet()    ## wil use default value
greet("Jamshaid")  ## force input argument

#*args (multiple values)
def values(*numbers):
    sum1=0
    for num in numbers:
        sum1+=num
    return sum1
print(values(1,2,3,4))

#**kwargs (key-value pairs)
def info(**data):
    return data
print(info(name="Jamshaid",age=15))

#Recursion (Function calling itself)

def factorization(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*factorization(n-1))   ##Recursion
print(factorization(2))

#Lambda (Anonymous Functions)

square=lambda x:x**2
print(square(10))





