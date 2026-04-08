######################################################################################################
                                        #Probability & Statistics
#Concepts:
#Mean, Median, Mode
#Variance, Standard Deviation
#Probability basics
#Conditional probability
#Normal distribution
#######################################################################################################
                                                #Mean
import numpy as np
A=np.array([1,2,3,10,5])
Sum1=np.sum(A)
Mean=Sum1/len(A)
print(Mean)
#ML Use
#Dataset center point
#Feature scaling baseline
#######################################################################################################
                                                #Median
                                        #Middle value (sorted data)
print(np.median(A))
#######################################################################################################
                                                #Mode
                                        #Most Freqent Value
data = [1, 2, 2, 3, 4]
# mode = 2

#ML Use
#Categorical data analysis
#Most common behavior detection


#######################################################################################################
                                                #Variance
                                        #Data kitna spread hai mean se
print(np.var(data))  ##It first calculae mean than subtrcat each value from mean

#######################################################################################################
                                                #Standard Deviation
                                        #Variance ka square root
print(np.std(data))

#ML Use
#Outlier detection
#Data normalization

#######################################################################################################
                                          #Numpy
        #NumPy = fast numerical library used in ML for handling arrays, vectors, matrices

#What is NumPy Array?

#👉 Similar to list but:
#✔ Faster
#✔ Supports vector operations
#✔ Used in ML models

#Creating Arrays

import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6]])

##Properties
print(a.shape)   # size (rows, cols)
print(a.ndim)  #dimension
print(a.size)  ##total element
print(a.dtype)

##Indexing and Slicing
print(a[0])
print(a[0:3])

#RESHAPING
#Concept
#Change shape without changing data

print(a.reshape(1,3))