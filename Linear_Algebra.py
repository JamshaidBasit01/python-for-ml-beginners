#1. SCALAR
#🧠 Concept
#👉 A scalar is just a single number
#No direction
#No dimension
#Just magnitude
###################################################################################################
                                        #1. SCALAR
###################################################################################################
a=5
b=-3.2
#ML Use
#Learning rate
#Bias (b in equation)
###################################################################################################
                                        #1. VECTOR
###################################################################################################
#2. VECTOR
#🧠 Concept
#👉 A vector is a collection of numbers (1D array)
#👉 Think:
#Features of a student
#Pixel values
v=[1,2,3,4]
#Operations on Vectors
#✅ Addition
v=[1,2,3]
w=[2,4,6]
# result = [4,6]
#Scalar Multiplication
v = [1,2,3]
k = 2
# result = [2,4,6]
#NumPy Methods (IMPORTANT 🔥)
import numpy as np

v = np.array([1,2,3])
print(v.shape)    ##provide shape(rows, coloumn)
print(v.size) ## entities in list
print(v.ndim)  ## provide dimension as 1

#ML Use
#👉 Each row = one data sample

##Addtition using Numpy
v=np.array([1,2,3])
w=np.array([2,4,6])
x=v+w
print(x)
#Scalar Multiplication
v = np.array([1,2,3])
k = 2
result=k*v
print(result)
# result = [2,4,6]
###################################################################################################
                                        #3. MATRIX
                                        #Concept
                        # A matrix is a 2D collection of numbers
###################################################################################################
A = [
    [1,2],
    [3,4]
]
#Properties
#Rows × Columns
#Shape = (m, n)

A=np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)  ##2 rows 3 coloums

print(A.size)

print(A.ndim)  ##2nd dimension

#ML Use
#👉 Dataset = matrix
#👉 Rows = samples
#👉 Columns = features

###################################################################################################
                                        #3. MATRIX Operations
###################################################################################################
## Addition

A=np.array([[1,2],[4,5]])
B=np.array([[2,4],[7,8]])
print(A+B)

##Multiplication
#we use dot product in multiplication and @ symbol

c=np.dot(A,B)
print(c)
c=A@B
print(c)

print(np.matmul(A,B))  ##another way

##Transpose

A_transpose=A.T
print(A_transpose)
print(np.transpose(A))  ##another way

#ML Use
#Shape fixing
#Neural networks

###################################################################################################
                                        #3. EIGENVALUES
#Concept
#Special vectors that don’t change direction
#𝐴𝑣=𝜆𝑣
###################################################################################################
#np.linalg.eig(matrix)

print(np.linalg.eig(A))

#ML Use
#PCA
#Dimensionality reduction

##find mean
Mean=np.mean(A)
print(Mean)

##Find maximum value in matrix
Max1=np.max(A)
print(Max1)

##Find min value in matrix
Min1=np.min(A)
print(Min1)

##Linea Equaion on dataset(y=mx+b)

##Input dataset
X=np.array([[1,2,3],[2,4,6]])

##bias 
b=1

## Define Weight
W=np.array([0.1,0.2,0.3])

W_T=np.transpose(W)

y=np.dot(X,W_T)+1
print(y)


