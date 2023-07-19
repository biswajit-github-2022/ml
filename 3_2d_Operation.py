import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

arr.shape
arr.dtype
arr[1,1]#5
arr[1,:]#This will return all elements of 1st row in the form of array

rr = np.ones((4,4))
t = arr[1:3,1:3]
print(t)
# t will be a 2x2 matrix with 4 elements
# PythonCopy
# [[1. 1.]
# [1. 1.]]

arr_zeros = np.zeros((3,5))
print(arr_zeros)#all 0

arr_rand = np.random.rand(3,4)
print(arr_rand)#random

a = np.array([[1,2,3],[4,6,2],[0,7,1]]) #array with size 3x3
#Scalar operation - It will operate with scalar to each element of an array
print(a+2)
print(a-4)
print(a*3)
print(a/2)
print(a**2)

a = np.array([[1,2,3],[4,6,2],[0,7,1]]) #array with size 3x3
b = np.array([[3,6],[1,4],[7,2]]) #array with size 3x2
c = np.array([[1,0,3],[2,3,1],[0,0,1]])
add = a+c
mul = np.matmul(a,b) #Matrix multiplication of a and b
print(add)
print(mul)

print(a.transpose())