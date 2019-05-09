# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split as tts
# code starts here

df = pd.read_csv(path)
print(df.head())

X = df.drop('list_price',1)
y = df.list_price

X_train,X_test,y_train,y_test= tts(X, y, test_size = 0.2, random_state=6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        

# code starts here        
cols = X_train.columns

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))

for i in range(0,3):
    for j in range(0,3): 
            col = cols[i*3 + j]
            axes[i,j].set_title(col)
            axes[i,j].scatter(X_train[col],y_train)
            axes[i,j].set_xlabel(col)
            axes[i,j].set_ylabel('list_price')
        

# code ends here
plt.show()



# code ends here



# --------------
# Code starts here
corr = X_train.corr()
print(corr)
X_train.drop(columns=['play_star_rating', 'val_star_rating'], inplace=True)
X_test.drop(columns=['play_star_rating', 'val_star_rating'], inplace=True)


# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(round(mse,2))
print(round(r2,2))

# Code ends here


# --------------
# Code starts here


residual = (y_test - y_pred)

# plot the figure for residual
plt.figure(figsize=(15,8))
plt.hist(residual, bins=30)
plt.xlabel("Residual")
plt.ylabel("Frequency")   
plt.title("Error Residual plot")
plt.show()

# Code ends here


