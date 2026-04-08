#we have been using variables that are storing one piece of data. Usually, when working with
#  data we want to store more than one value. Python does have the ability to work with arrays,
#  vectors, and import excel spreadsheets or .csv files, so on and so forth!. Although we’ll get 
# to that later in the lesson. First, we’re going to cover python’s built-in data structures which
#  are lists, tuples, sets, and dictionaries

list1=[1,2,3,4]   ## integer list
list2=["a","b","c","d"]  ## string list

# note the square brackets 
# additionally note how each piece of information in the list is 
# refered to as an element. You may also seem them refered to as an item.

tuple1=(1,2,3,4)  ##tuple list

# note the paratheses

set1={1,2,3,4}

# note the curly brackets

dictionary1={
    "Name":"Jamshaid",
    "Age":10,
    "Education":["Metric","Bsc","Msc"]   # You can even store lists, tuples and sets
}


# we can use a comindation of the print() and type() function to get python
# to tell us what it is if we needed (you could also look in the variable
# explorer in spyder)

print(type(dictionary1))


## Each data type has its own advantages and disadvantages, they can store all the basic
#  data types we covered in a previous lesson. When deciding what data type to use, kind 
# about the characteristics of that data type, to help you decide. The list data type gives
#  you a lot of freedom and flexibility. However, what if this flexibility causes you to accidentally 
# overwrite some important data? If that is a major concern, then you’d consider using a Tuple, since 
# they are not changeable. Because they’re not changeable, tuples use less memory, meaning your program 
# will execute faster. Lists and tuples are very common. However, sets have a more niche use case. Sets 
# don’t have an order and don’t allow duplicates, which means they’re very suited to checking to see if 
# the same elements are in the set or not or other similar membership tests. Dictionaries can store all 
# the data types, it’s useful if you’d like to categorise your data but keep it within the same data frame.


#########################################################################################################
                                                #LISTS
                                #Ordered, mutable (changeable), allows duplicates
##########################################################################################################

#These data types allow us to store multiple values in a single variable. I’ll be very honest with you, 
# I’m biased. I’ve only ever really used Lists, and the occasionally Dictionary. So we are going to be
#  focusing on Lists! When we start using packages, we’re going to be learning new data structures! 
# One great thing about lists, is that we can access elements in the list via their index. For example,
#  the first element in the list has an index of zero, because remember python is zero-indexed. 
# Let’s combine this knowledge of being able to access data in a variable by its index using loops.

my_list=[1,2,3,4,5]

##Methods
#1. Append(x)  to add a number at the end of list
my_list.append(6)
print(my_list)

#2. extend(iterable)  Add multiple values
iter=[7,8,9]
my_list.extend(iter)
print(my_list)

#3. insert(i, x)   insert at specific index
my_list.insert(3,10)  ##  will insert at index 3 start from 0
print(my_list)

#4. remove(x)   remove specific value
my_list.remove(10)
print(my_list)

#5. pop(i)   remove by index
my_list.pop(2)
print(my_list)

#6. index(x)  find index of specific number
index1=my_list.index(8)
print(index1)

#7. count(x)  count occurance of specific number in list
count1=my_list.count(2)
print(count1)

#8.sort()  sort list
my_list.sort(reverse=False)
print(my_list)

my_list.sort(reverse=True)
print(my_list)

#9. copy()  Copy list
new_list=my_list.copy()
print(new_list)


#########################################################################################################
                                                #TUPLE
                                #Ordered, Immutable (non-changeable), allows duplicates
##########################################################################################################
my_tuple=(1,2,3,1)

##Methods
#1. count(x)    Count occurrences
count11=my_tuple.count(1)
print(count11)

#2. index(x)  Find index
Index11=my_tuple.index(3)
print(Index11)

#########################################################################################################
                                                #SETS
                                #Un-Ordered, mutable (changeable), not allow duplicates
##########################################################################################################
set1={1,2,3,4}
set2={3,2,4,5}

##Methods
#1. add(x)  Add Element
set1.add(5)
print(set1)

#2. update(iterable)  Add Multipe Elements
data1=[6,7,8]
set1.update(data1)
print(set1)

#3. remove(x)   Remove (error if not found)
set1.remove(5)
print(set1)

#4. discard(x)  remove safely
set1.discard(5)
print(set1)

#5. We use also Pop in this but as list we donot give it any index
set1.pop()  ## remove random
print(set1)

#########################################################################################################
                                                #DICTIONARIES
                                #Key-Value pairs, unordered (Python 3.7+ ordered), mutable
##########################################################################################################
dictionary1={
    "Name":"Jamshaid",
    "Age":18
}

##Methods
#1. get(key)   Safe access
print(dictionary1.get("Name"))

#2. keys()   get all Keys 
print(dictionary1.keys())

#3. valuess()  get all values
print(dictionary1.values())

#4. items()  Key-value pairs
print(dictionary1.items())

#5. Add new value in dictionary
dictionary1["Age"]=20   ##Update value of age  key
print(dictionary1.items())


#########################################################################################################
                                                #NESTED STRUCTURES
                                         #Data structures inside another
##########################################################################################################
# Nested List
matrix=[[1,2,3],[4,5,6]]
print(matrix[1][1])

#Nested Dictionary
student_data={
    "Name":"Jamshaid",
    "marks":{
        "math":25,
        "english":26
    }  
}
print(student_data.get("marks").get("math"))  ##one way
print(student_data["marks"]["math"])  ##other way



## Challenge
#What we want to create is a program that will ask someone how many animals they can remember
#  and then it tells them how many they remember, feel free to make your own or you can use the 
# code below!

remember_aniamls=[]  ## define empty list

print("Enter anaimal that you remember")
while True:  ##Run until it not break
    animal=input()   ##user inout
    if (animal=="Done"):
        break
    else:
        remember_aniamls.append(animal)  ##add new animal in list
        print(animal,"added to your list")
print("You Remember only",len(remember_aniamls),"animals")
print("Here is List of that animals")
print("=========================================")
for i in range(len(remember_aniamls)):
    print(i+1,".",remember_aniamls[i])


