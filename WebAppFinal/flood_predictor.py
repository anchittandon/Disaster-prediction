import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
data=pd.read_csv("final_data.csv")
data=np.array(data)
data=data[:,1:]
msk1 = np.random.rand(len(data)) < 0.7
train = data[msk1]
test = data[~msk1]
x_train=train[:,1:]
y_train=train[:,0]
x_test=test[:,1:]
y_test=test[:,0]
lr.fit(x_train,y_train)
def prediction():
    #learn the regressor
    #print(lr.predict(data))
    count=0
    for i in range(x_test.shape[0]):
        if(lr.predict([x_test[i]])==y_test[i]):
            count+=1
    print("efficiency"+str((count/x_test.shape[0])*100))
def prediction1(data):
    return ((lr.predict(data)))
