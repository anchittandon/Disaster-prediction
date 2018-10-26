import pandas as pd
import numpy as np

data=pd.read_csv("Rainfall.csv")
data['JAN'].fillna((data['JAN'].mean()), inplace=True)
data['FEB'].fillna((data['FEB'].mean()), inplace=True)
data['MAR'].fillna((data['MAR'].mean()), inplace=True)
data['APR'].fillna((data['APR'].mean()), inplace=True)
data['MAY'].fillna((data['MAY'].mean()), inplace=True)
data['JUN'].fillna((data['JUN'].mean()), inplace=True)
data['JUL'].fillna((data['JUL'].mean()), inplace=True)
data['AUG'].fillna((data['AUG'].mean()), inplace=True)
data['SEP'].fillna((data['SEP'].mean()), inplace=True)
data['OCT'].fillna((data['OCT'].mean()), inplace=True)
data['NOV'].fillna((data['NOV'].mean()), inplace=True)
data['DEC'].fillna((data['DEC'].mean()), inplace=True)
data['ANNUAL'].fillna((data['ANNUAL'].mean()), inplace=True)
data['Jan-Feb'].fillna((data['Jan-Feb'].mean()), inplace=True)
data['Mar-May'].fillna((data['Mar-May'].mean()), inplace=True)
data['Jun-Sep'].fillna((data['Jun-Sep'].mean()), inplace=True)
data['Oct-Dec'].fillna((data['Oct-Dec'].mean()), inplace=True)

print(data.head())
data=np.array(data)
print(data.shape)

state = {name:i for i, name in enumerate(sorted(set(data[:,0])))}
print(state)    
df=pd.DataFrame(data[:,:14]).replace(state)
df.to_csv("data.csv") 
data2=np.array(df)
print(data2[:200])
x=[]
# x=np.array(x)
y=[]
# y=np.array(y)
count=0 #count max =35
flood_min=254
for i in range(36):
    print(data2[:,0],i)
    temp=data2[data2[:,0]==i][:,2:].flatten()
    temp=np.array(temp)
    for j in range(temp.shape[0]):
        x.append([i,temp[j]])
    print(temp)
    # temp=np.append((i*np.ones((temp.shape[0],1,temp))
    # np.append(( 
    for j in range(temp.shape[0]):
        noise=25*np.random.normal(0,0.45)
        if(temp[j]>=354+noise):
            y.append(3)
        elif(temp[j]>204-abs(noise) and temp[j] <=254):
            y.append(1)
        elif(temp[j]>254 and temp[j]<354+noise):
            y.append(2)
        else:
            y.append(0)
    # y=np.concatenate((y,i*np.ones((temp.shape[0],1)).flatten()))
# print(x.shape,y.shape)
x=np.array(x)
y=np.array(y)
y=y.reshape((y.shape[0],1))
data_final=np.concatenate((y,x),axis=1)
df2=pd.DataFrame(data_final)
df2.to_csv("final_data.csv")