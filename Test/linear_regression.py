import pandas as pd

dataset = pd.read_csv("housing_price_data_set.csv")
dataset.head()
X = dataset.iloc[:, 3:].values
Y = dataset.iloc[:, 2:3].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.33,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score
print round(r2_score(Y_test,Y_pred)*100,2), 'percent'