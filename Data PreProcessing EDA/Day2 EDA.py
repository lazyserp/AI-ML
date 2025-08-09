import pandas as pd 
from sklearn.preprocessing import LabelEncoder



#labeling Data in range of 0-1 for better understanding by Model
le = LabelEncoder()
data = pd.read_csv('./titanic_exported.csv')

df = pd.DataFrame(data)

df  = pd.get_dummies(df, columns=["Embarked"], drop_first=True)


df.to_csv('Exported_titanic_2.csv',index=False)
