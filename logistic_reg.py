from sklearn import linear_model 
from sklearn.model_selection import train_test_split 
import pandas as pd 
datas = pd.read_csv('data.csv') 
X = datas.iloc[:, 2:4].values 
y = datas.iloc[:, 4].values 
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.1) 
model = linear_model.LogisticRegression() 
model.fit(x_train, y_train) 
p = float(input("enter first independent variable value: ")) //47
q = float(input("enter second independent variable value: ")) //25000
pre = model.predict([[p, q]]) 
print("predicted value is: ", pre) //[1]

# age     salary  purchased
# 19      19000      0
# 47      25000       1