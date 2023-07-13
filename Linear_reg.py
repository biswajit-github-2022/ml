import numpy as np 
import matplotlib.pyplot as plt 
def plot_regression_line(x, y, b): 
 plt.scatter(x, y, color="m",marker="o", s=30) 
 y_pred = b[0] + b[1]*x 
 plt.plot(x, y_pred, color="g") 
 plt.xlabel('x') 
 plt.ylabel('y') 
 plt.show() 
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
n = np.size(x) 
x_mean = np.mean(x) 
y_mean = np.mean(y) 
Sxy = np.sum(x*y) - n*x_mean*y_mean 
Sxx = np.sum(x*x) - n*x_mean*x_mean 
b1 = Sxy/Sxx 
b0 = y_mean-b1*x_mean 
p = float(input("enter the value of x to predict y: ")) 
y_pred = b1 * p + b0 
print("value at", p, "is", y_pred) 
plot_regression_line(x, y, [b0, b1]) 
INPUT SET: 
OUTPUT SCREEN: 
 
X 0 1 2 3 4 5 6 7 8 9 
Y 1 3 2 5 7 8 8 9 10 12