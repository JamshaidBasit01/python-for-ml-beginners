#What is OOP?
#OOP stands for Object-Oriented Programming.
#Python is an object-oriented language, allowing you to structure your code using classes and objects 
# for better organization and reusability.


#What are Classes and Objects?
# and objects are the two core concepts in object-oriented programming.
#When you create an object from a class, it inherits all the variables and functions defined inside that class.

#Python Classes/Objects
#Python is an object oriented programming language.

#Almost everything in Python is an object, with its properties and methods.

#A Class is like an object constructor, or a "blueprint" for creating objects.

########################################################################################################
                                        #Create a Class
                            #To create a class, use the keyword class:
########################################################################################################
class MyClass:
    x=5

########################################################################################################
                                        #Create a Object
                            #Now we can use the class named MyClass to create objects:
########################################################################################################
p1=MyClass()
print(p1.x)

##Pass statement in class
class Student_Data:
    pass

########################################################################################################
                                        #The __init__() Method
#All classes have a built-in method called __init__(), which is always executed when the class is being
#  initiated.

#The __init__() method is used to assign values to object properties, or to perform operations that are
#  necessary when the object is being created.
########################################################################################################
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Basit",24)
print(p1.name)
print(p1.age)

#Default Values in __init__()
#You can also set default values for parameters in the __init__() method:
class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=Person("Basit",20)
print(p1.name)
print(p1.age)

##Coding Challenge
#Create a class called Person
#Add an __init__ method that takes name and age as parameters
#Add a method called greet that prints "Hello, my name is " followed by the name
#Create an object p1 of the class with name "John" and age 36
#Call the greet method on p1

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello, my name is",self.name)
p1=Person("John",36)
p1.greet()

#Challenge: __init__ Method
#Test your understanding of creating classes, __init__, properties, methods, and objects.
#Create a class called Dog
#Add an __init__ method with parameters name and age, and store them as properties using self
#Add a method called bark that prints the dog's name followed by " says Woof!"
#Create an object d1 of the Dog class with name "Buddy" and age 3
#Call the bark method on d1

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(self.name,"says Woof!")
d1=Dog("Buddy",3)
d1.bark()

##Class Properties vs Object Properties
#Properties defined inside __init__() belong to each object (instance properties).
#Properties defined outside methods belong to the class itself (class properties) and 
# are shared by all objects:

class Person:
    species="Human"   # Class property
    def __init__(self,name):
        self.name=name   #Instance Property
p1=Person("Jamshaid")
p2=Person("Ali")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

#Modifying Class Properties
#When you modify a class property, it affects all objects:

class Person:
    species=""
    def __init__(self,name):
        self.name=name
p1=Person("Basit")
print(p1.name)

Person.species="Human"   ## Modif class properties
p1.age=20

print(p1.species)
print(p1.age)

#Challenge: Class Properties
#Test your understanding of class properties by completing a small coding challenge.

#Create a class Student with an __init__ that takes name and grade, and stores them as properties
#Create an object s1 with name "Anna" and grade "A"
#Print the grade of s1
#Change the grade of s1 to "B"
#Print the updated grade

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s1=Student("Anna","A")
print(s1.grade)
s1.grade="B"
print(s1.grade)

#Challenge: Class Methods
#Test your understanding of class methods by completing a small coding challenge.
#Create a class called Rectangle
#Add an __init__ method with width and height, and store them as properties
#Add a method called area that returns the width multiplied by the height
#Create an object r1 with width 5 and height 3
#Print the area of r1

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
r1=Rectangle(5,3)
print(r1.area())

########################################################################################################
                                       #Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.
########################################################################################################
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname, self.lname)


#Create a Child Class
#To create a class that inherits the functionality from another class, send the parent class as a
#  parameter when creating the child class:
class Student(Person):
    pass

#Now the Student class has the same properties and methods as the Person class.
x= Student("Ali","Ahmed")
x.printname()

#Add the __init__() Function
#So far we have created a child class that inherits the properties and methods from its parent.
#We want to add the __init__() function to the child class (instead of the pass keyword).

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)
    def message(self):
        print("Welcome",self.fname,self.lname)
x=Student("Ahmad","Ali")
x.message()

##Challenge: Inheritance
#Test your understanding of Python inheritance by completing a small coding challenge.
#Create a parent class Animal with an __init__ that takes name
#Add a method speak that prints the name
#Create a child class Dog that inherits from Animal
#Create an object d1 = Dog("Rex")
#Call d1.speak()

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name)

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
d1=Dog("Rex")
d1.speak()


########################################################################################################
                                       #Class Polymorphism
#Polymorphism is often used in Class methods, where we can have multiple classes with the same method 
# name.
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
########################################################################################################
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail!")
c1=Car("Ford","Mustang")
c1.move()
b1=Boat("ABC","XYZ")
b1.move()

##Inheritance Class Polymorphism
#What about classes with child classes with the same name? Can we use polymorphism there?
#Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, 
# Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
c1=Car("Ford","Mustang")
c1.move()
b1=Boat("YZ","AB")
b1.move()

##Challenge: Polymorphism
#Test your understanding of Python polymorphism by completing a small coding challenge.

#Create a class Cat with a method sound that prints "Meow"
#Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
#Create objects c1 = Cat() and f1 = Fox()
#Call sound() on both objects

class Cat:
    def __init__(self):
        pass
    def sound(self):
        print("Meow")
class Fox:
    def __init__(self):
        pass
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")
c1=Cat()
f1=Fox()
c1.sound()
f1.sound()


########################################################################################################
                                       #Python Encapsulation
#Encapsulation is about protecting data inside a class.
#It means keeping data (properties) and methods together in a class, while controlling how the data 
# can be accessed from outside the class.
########################################################################################################
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  ##private property(double underscore)
p1=Person("Basit",20)
print(p1.name)
#print(p1.__age) ##give error

#Get Private Property Value
#To access a private property, you can create a getter method:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  ##private property
    def get_age(self):
        return self.__age
p1=Person("Basit",20)
print(p1.get_age())

#Why Use Encapsulation?
#Encapsulation provides several benefits:

#Data Protection: Prevents accidental modification of data
#Validation: You can validate data before setting it
#Flexibility: Internal implementation can change without affecting external code
#Control: You have full control over how data is accessed and modified

#Protected Properties
#Python also has a convention for protected properties using a single underscore _ prefix:
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #protect property
s1=Student("Ali",20)
print(s1.name)
#print(s1.__age)

#Private Methods
#You can also make methods private using the double underscore prefix:
class Calculator:
    def __init__(self):
        self.result=0
    def __validate(self,num):
        if not isinstance(num,(int,float)):
            return False
        else:
            return True
    def add(self,num):
        if self.__validate(num):
            self.result+=num
        else:
            print("Invalid Number")
cal=Calculator()
cal.add(5)
cal.add(10)
print(cal.result)

#Challenge: Encapsulation
#Test your understanding of Python encapsulation by completing a small coding challenge.
#Create a class ScoreBoard
#Add an __init__ with a score parameter and store it as a private attribute
#Add a method called get_score that returns the private score
#Create an object s1 with a score of 0
#Print the score of s1

class ScoreBoard:
    def __init__(self,score):
        self.__score=score
    def get_score(self):
        return self.__score
s1=ScoreBoard(0)
print(s1.get_score())