#Importing libraries
import pandas as pd

#Loading the dataset
df = pd.read_csv('orders_info.csv')

#Reviewing dataset
df.head()


#Separating features and labels
X = df.iloc[:, :-1].values
y = df.iloc[:, 3:].values
print X, y

#Check for missing data
df.isnull().sum()

#Handling Missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, :2])
X[:, :2] = imputer.transform(X[:, 2:3])
print X

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features  = [0]) #Index of the categorical column
print X.shape
X = onehotencoder.fit_transform(X).toarray()

labelencoder_y = LabelEncoder()
y[:, 0] = labelencoder_y.fit_transform(y[:, 0]) #Trivia : Why are we not using OneHotEncoder?
print X.shape, y.shape

#Splitting into Train and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0) #Trivia : What is random_state?
print 'X Train', X_train, '\n\nX Test', X_test, '\n\nY Train', y_train, '\n\nY Test',y_test

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #Trivia :
print X_train, X_test

