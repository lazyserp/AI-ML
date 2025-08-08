import pandas
import sklearn


data  = pandas.read_csv('titanic.csv')
df = pandas.DataFrame(data)

df['Age'] = df['Age'].fillna(int(df['Age'].median()))

df.drop_duplicates()

df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df['Fare'] = df['Fare'].round().astype(int)



#categorisation of data
df['Sex'] = df['Sex'].astype("category")
df['Embarked'] = df['Embarked'].astype("category")







df.to_csv('titanic_exported.csv',index=False)