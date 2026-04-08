## What is conditional
#First, let's imagine a real-world scenario. We all in our lives face any situation where we need to make a decision based on a condition. Like it's really common to say,
#"If it rains, we won't play".
#So you can see that here's the possibility of playing depending on if it rains or not. Here we're making a decision based on a condition.

#Similarly, in programming, sometimes we also need to execute a block of code based on a decision or a program will run if it satisfies a condition. Basically this concept is known as 'Conditionals'. Now let's dive into it!

#For conditionals, in python program, there are if, elif and else statements to perform this decision-making programs. We'll learn all of these one by one.

#We'll try to understand conditional through a simple project:

#Let's try to make a ticket system for a rollercoaster ride.

#We have the following conditions:

#If your height is over 120cm, you ride the rollercoaster.
#If your height is less than 120cm, you can't ride the rollercoaster.
#Your height is over 120cm but you're less than 12 years old, pay 4$
#Your height is over 120cm but you're less than 18 years old, pay 6$
#Your height is over 120cm but you're over 18 years old, pay 8$
#To implement this real-life scenario into code, we need decision-making features. For that we're going to use conditionals.

## IF ELSE Condition
print("Enter Your age")
age=int(input())
if(age>18):
    print("Valid for Vote")
else:
    print("Not Valid")

##IF ELIF ELSE Condition

#Practice problem
#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#BMI=weight(kg)/height**2(m)

#It should tell them the interpretation of their BMI based on the BMI value.

#Under 18.5 they are underweight
#Equal to or over 18.5 but below 25 they have a normal weight
#Equal to or over 25 but below 30 they are slightly overweight
#Equal to or over 30 but below 35 they are obese
#Equal to or over 35 they are clinically obese.

#Use input functions to take weight and height input from the user.

print("Enter your Weight in kg")
weight=int(input())
print("Enter your Height in meters")
height=int(input())
BMI=weight/height**2
print("BMI Score is:",BMI)
#Under 18.5 they are underweight
if(BMI<18.5):
    print("UnderWeight")
#Equal to or over 18.5 but below 25 they have a normal weight
elif(BMI>=18.5 and BMI<25):
    print("Normal")
#Equal to or over 25 but below 30 they are slightly overweight
elif(BMI>=25 and BMI<30):
    print("OverWeight")
#Equal to or over 30 but below 35 they are obese
elif(BMI>=30 and BMI<35):
    print("Obese")
#Equal to or over 35 they are clinically obese.
elif(BMI>=35):
    print("Clinically Obese")
