#####################################################################################################
                                            ##While Loop
#####################################################################################################

#Loops allow up to repeat code and iterate over large data sets. The latter, 
# we’ll be getting more into in the next session. Loops come in two varieties, 
# you have while loops and for loops. While loops will run the code while a condition 
# is met. For loops will run the code for a specified number of times.

#While Loops
#We’re going to create some code that allows the user to guess a number between 1 – 10,
#  however, the user only has 3 guesses. Let’s run the code below to start off.

#i=1  ## initial values
#while i<3:  ## Condition set to run loop
#    print("Guess a value between 1-10 please")
#    guess=int(input())

#What happened when you ran the code? You’ll have found it would continuously loop indefinitely. 
# This is because, in our loop, we’re not increasing the value of i by 1. Go ahead and see if 
# you can solve this problem.

#i=1  ## initial values
#while i<3:  ## Condition set to run loop
#    print("Guess a value between 1-10 please")
#    guess=int(input())
#    i+=1

#Next, we need to get the program to generate a number between 1 and 10 then tell us if we’re
#  right and what the right number is if we don’t guess it. We’ll start off by randomly generating 
# a number.

#import random

#number=random.randint(1,10)
#print("Random Number is:",number)

#i=1
#while i<3:
#    print("Guess a value between 1-10 please")
#    guess=int(input())
#    i+=1

#Now the program is generating a number. For testing purposes, I’ve added the program to 
# print the correct answer before we guess so we can test it. Next, we need the program to 
# tell the user if their guess is right or wrong. For you to do! I’d like you to add an if 
# statement to the code above to tell the user if they’ve guessed correctly.

import random

number=random.randint(1,10)
print("Random Number is:",number)

i=1
while i<=3:
    print("Guess a value between 1-10 please")
    guess=int(input())
    if(guess==number):
        print("You are Right!")
        break
    elif(guess!=number):
        remaining=3-i
        print("Incorrect! You have ", remaining, " attempts remaining.")
    i+=1
else:
    print("You've run out of attempts, the correct number was", number)

#------------------------------------------------------------------------------------------------------
#####################################################################################################
                                            ##For Loop
#####################################################################################################
#Let’s move onto for loops that run for a number of iterations. The syntax is the same as while loops,
#  we just replace while with for. In our for loop, we’re going to be using the range() function, which 
# allows us to specify the number of times the code will run.
for i in range(10):
    print(i)

#By default, python will increment the value i but 1. You can change this by adding a third argument 
# to the range() function. We will be covering arguments, for now just know it’s the values we place 
# in the parentheses of the function. To change the increments from the default of 1 to your specified
#  number, I’m going to use 2, try the following code.

for i in range(1,11,2):
    print(i)

#Session Challenge!
#I’d like you to create a program that simulates a coin toss. Your program will ask the user how 
# many times they would like to toss a coin. Then simulate a coin toss as many times as the user 
# requested. To finish with, the program will tell the users how tosses they were in addition to 
# how many heads and how many tails. You can use the code below to get started.

import random

print("How many times you want to Toss the coin")
coin=int(input())
Head=0
Tail=0
for i in range(0,coin):
    flip=random.randint(0,1)
    ## 0 for head, 1 for tail
    if(flip==0):
        Head+=1
    elif(flip==1):
        Tail+=1
print("Total Heads get by user is:",Head)
print("Total Tails get by user is:",Tail)