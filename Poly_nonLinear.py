import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score 
x = np.array(7 * np.random.rand(100, 1) - 3) 
x1 = x.reshape(-1, 1) 
y = 13 * x*x + 2 * x + 7 
regression_model = LinearRegression() 
regression_model.fit(x1, y) 
y_predicted = regression_model.predict(x1) 
poly_features = PolynomialFeatures(degree = 2, include_bias = False) 
x_poly = poly_features.fit_transform(x1) 
lin_reg = LinearRegression() 
lin_reg.fit(x_poly, y) 
x_new = np.linspace(-3, 4, 100).reshape(100, 1) 
x_new_poly = poly_features.transform(x_new) 
y_new = lin_reg.predict(x_new_poly) 
plt.plot(x, y, "b.") 
plt.plot(x_new, y_new, "r-", linewidth = 2, label ="Predictions") 
plt.xlabel("$x_1$", fontsize = 18) 
plt.ylabel("$y$", rotation = 0, fontsize = 18) 
plt.legend(loc ="upper left", fontsize = 14) 
plt.title("Quadratic_predictions_plot") 
plt.show() 