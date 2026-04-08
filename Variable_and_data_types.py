# Let's say I wanted to save my name which is Jamhshaid, into a variable 
# called my_name. It would look like the following

my_name = "Jamshaid"

#Note how we use the quotation marks around Paige. This is to ensure 
#that Jamshaid is interpreted as a string.

# You may have two other questions...
# First, what's with the use of the hashtag. hashtags tell the interpretor
# that these are comments for the human, therefore don't execute this!
"""
If you'd like to write multiple lines of comments you can use three 
quotation marks in a row at the start and end of your comment.
"""

# The second question you may have is, why did we name the variable 
# as my_name, what's with the lower case and underscore?
# This is about style. For variables, the PEP 8 guidelines suggest
# variable names should be lowercase, with words separated by underscores 
# as necessary to improve readability. Commonly, this is referred to as 
# snake_case

## print the name

print(my_name)

#What if we want to print “Hello Paige!” instead? Take a look at the code below.

print("Hello",my_name)

#We are using the comma to add the word “Hello” and an exclamation point to what is printed.

##One more way is to add strings
Message="Hello"+" "+my_name
print(Message)

#Now imagine if we someone to input their own name. We could make sure of the input() function. 
# The input() function takes whatever is written in the console and stores that in a variable. 
# The user has to type their name and then press enter.

my_name=input()
print("Hello",my_name)

#If you run the above code, you may find it strange that the program doesn’t prompt you to 
# type your name. Go ahead and add that now. Hint! Python executes codes sequentially from top to bottom!

print("Type your name here, followed by the enter button:")
my_name=input()
print("Hello",my_name)

#You may have some code similar to the below and are frustrated that if the numbers 5 and 6 are inputted
#  that you’re getting returned 56 and not 11!

print("Enter First Number here please!")
num1=input()
print("Enter Second Number here please!")
num2=input()
sum=num1+num2
print("Two Numbers added give to:",sum)

#Why is this? This is because the input is recording the numbers entered as strings, not integers
#  or floats. What we need to do is declare the input as either an integer or float, depending on 
# if we want whole numbers or decimals. We can do this using the int() or float() function which 
# converts information inside of the parentheses into the corresponding data type. Let’s try this 
# again with the code below

print("Enter First Number here please!")
num1=int(input())
print("Enter Second Number here please!")
num2=int(input())
sum=num1+num2
print("Two Numbers added give to:",sum)

#Ta-da! When we add together 5 and 6 we should now receive the answer 11!

##Section Challenge
#To end this section, I’d like you to write some code that takes the input of three numbers 
#and averages them.

## Take 3 numbers as input
print("Enter Number1 here:")
num1=float(input())
print("Enter Number2 here:")
num2=float(input())
print("Enter Number3 here:")
num3=float(input())

##Take average of thse three numbers

avg=(num1+num2+num3)/3
print("Average of given three numbers are:",avg)



