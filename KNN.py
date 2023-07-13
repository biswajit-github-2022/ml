import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report, confusion_matrix 
df = pd.read_csv("prostate2.csv") 
scaler = StandardScaler() 
scaler.fit(df.drop('target', axis=1)) 
scaled_features = scaler.transform(df.drop('target', axis=1)) 
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1]) 
X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['target'], test_size=0.30) 
knn = KNeighborsClassifier(n_neighbors=1) 
knn.fit(X_train, y_train) 
pred = knn.predict(X_test) 
print(confusion_matrix(y_test, pred)) 
print(classification_report(y_test, pred)) 
error_rate = [] 
for i in range(1, 40): 
    knn = KNeighborsClassifier(n_neighbors=i) 
    knn.fit(X_train, y_train) 
    pred_i = knn.predict(X_test) 
    error_rate.append(np.mean(pred_i != y_test)) 
plt.figure(figsize=(10, 6)) 
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', 
markersize=10) 
plt.title('Error Rate vs. K Value') 
plt.xlabel('K') 
plt.ylabel('Error Rate') 
plt.show() 


# [[22 3]
#  [2 3]]
#     pre     recall  f1-sc   support
# 0   0.92    0.88    0.90    25
# 1   0.50    0.60    0.55    5

