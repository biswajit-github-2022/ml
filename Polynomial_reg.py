import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt
datas = pd.read_csv('4.data.csv')
X = datas.iloc[:, 1:2].values
y = datas.iloc[:, 2].values
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
poly.fit(X_poly, y)
lin = LinearRegression()
lin.fit(X_poly, y)
p = float(input("enter first independent variable value: "))
predarray = np.array([[p]])
y_pred = lin.predict(poly.fit_transform(predarray))
print("value at", p, "is", y_pred)
plt.scatter(X, y, color='blue')
plt.plot(X, lin.predict(poly.fit_transform(X)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')
plt.show()
