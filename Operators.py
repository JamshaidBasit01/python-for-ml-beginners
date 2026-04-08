# Look at the code below to see some arithmetic operators, feel free to play around with the code below
##Define soma variables

##########################################################################################
                                    ##Arithmatics Operators
##########################################################################################
x=10
y=5

##Sum operator
z=x+y
print("sum of",x,"and",y,"is:",z)

##Subtract Operator
z=x-y
print("Subtraction of",x,"and",y,"is:",z)

## Multiple Operators
z=x*y
print("Multiplicaiton of",x,"and",y,"is:",z)

##Division
z=x/y
print("Division of",x,"and",y,"is:",z)

##Modulss
z=x%y
print("Mpdulus of",x,"and",y,"is:",z)  #Remainder

##Exponentiaion
z=x**y
print("Exponentiation of",x,"and",y,"is:",z)    #Power

##Floor Dvision
z=x//y
print("Floor Division of",x,"and",y,"is:",z)  #Integer division (no decimal)

##########################################################################################
                                    ##Logical Operators
##########################################################################################

#Used for decision making / conditions
#and operator
if(x>5 and y<10):
    print("Valid")
else:
    print("Not Valid")

#or operator
if(x>5 or y>10):
    print("Valid")
else:
    print("Invalid")

#not operator
if(not(x<5)):
    print("Valid")
else:
    print("Invalid")

#======================================================================================================

#Comparison (Relational) Operators
##Equal
if(x==5):
    print("Valid")
else:
    print("Invalid")

##Not Equal
if(x!=5):
    print("Valid")
elif(x==5):
    print("Good Chance")
else:
    print("Invalid")

#=========================================================================================================

#Assignment Operators
## Assign
x=5
print("Value of x is:",x)

## Sum with assign value
x+=10       ##x=x+10
print("New Value of x is:",x)

## Subtract with assign value
x-=5        ##x=x-5
print("New Value of x is:",x)

## Multiple with assign vaue
x*=5        ##x=x*5
print("New Value of x is:",x)

## Division with assign value
x/=5        ##x=x/5
print("New Value of x is:",x)

## Modulus with assign value
x%=3       ##x=x%3
print("New Value of x is:",x)

## Power with assign value
x**=2     ##x=x**2
print("New Value of x is:",x)

#--------------------------------------------------------------------------------------------------




