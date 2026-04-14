import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


#Load dataset as a pandas dataframes
df1=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")

#select important fetaures on basis of correlation btw target and features
features = ['OverallQual','GrLivArea','TotalBsmtSF',
            'GarageCars','GarageArea','Total_Bathrooms','1stFlrSF']

train_x=df1[features]
test_x=df2[features]

#deciding target variable
train_y=df1['Saleprice']

# Handle missing values
train_x = train_x.fillna(0)
test_x = test_x.fillna(0)


#model selection
model=linear_model.LinearRegression()

#model training
model.fit(train_x,train_y)

#model prediction
pred=model.predict(test_x)

#Creating a submition csvfile
submission = pd.DataFrame({
    'Id': df2['Id'],
    'SalePrice': pred
})

submission.to_csv("submission.csv", index=False)
