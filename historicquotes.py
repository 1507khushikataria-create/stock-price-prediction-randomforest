import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

data=pd.read_csv("HistoricalQuotes.csv")

print(data.head())
print(data.info())

data.columns=data.columns.str.strip()

data=data.dropna()

data["Open"]=data["Open"].replace(r'[\$,]','',regex=True).astype(float)
data["Close/Last"]=data["Close/Last"].replace(r'[\$,]','',regex=True).astype(float)
data["High"]=data["High"].replace(r'[\$,]','',regex=True).astype(float)
data["Low"]=data["Low"].replace(r'[\$,]','',regex=True).astype(float)

data=data.drop("Date",axis=1)

sns.countplot(x='Close/Last',data=data)
plt.title("distribution map")
plt.show()

sns.histplot(data['Close/Last'],bins=50)
plt.title("histogram plot")
plt.show()

X=data.drop('Close/Last',axis=1)
y=data["Close/Last"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=RandomForestRegressor()
model.fit(X_train,y_train)

predictions=model.predict(X_test)

mse =mean_squared_error(y_test,predictions)
print("mse:",mse)