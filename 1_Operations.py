import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing addition using arithmetic operator
add_ans = a+b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a, b)
print(add_ans)

# The same functions and operations can be used for multiple matrices
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)

add_ans = np.add(a, b, c)
print(add_ans)
#####################################################################################################

import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing subtraction using arithmetic operator
sub_ans = a-b
print(sub_ans)

# Performing subtraction using numpy function
sub_ans = np.subtract(a, b)
print(sub_ans)
#####################################################################################################

import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing multiplication using arithmetic operator
mul_ans = a*b
print(mul_ans)

# Performing multiplication using numpy function
mul_ans = np.multiply(a, b)
print(mul_ans)
#####################################################################################################


import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing division using arithmetic operators
div_ans = a/b
print(div_ans)

# Performing division using numpy functions
div_ans = np.divide(a, b)
print(div_ans)
#####################################################################################################


# Performing mod on two matrices
mod_ans = np.mod(a, b)
print(mod_ans)

#Performing remainder on two matrices
rem_ans=np.remainder(a,b)
print(rem_ans)

# Performing power of two matrices
pow_ans = np.power(a, b)
print(pow_ans)
#####################################################################################################



# Getting mean of all numbers in 'a'
mean_a = np.mean(a)
print(mean_a)

# Getting average of all numbers in 'b'
mean_b = np.average(b)
print(mean_b)

# Getting sum of all numbers in 'a'
sum_a = np.sum(a)
print(sum_a)

# Getting variance of all number in 'b'
var_b = np.var(b)
print(var_b)
