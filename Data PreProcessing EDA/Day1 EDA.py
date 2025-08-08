import pandas
import sklearn

#READ CSV FILE 
data  = pandas.read_csv('./Datasets/titanic.csv')

#convert csv file to dataframe
df = pandas.DataFrame(data)



# #Seeing top 5 rows
print(df.head())

#basic info about columns
print(df.info())

#mathematical quantities eg : mean , mode, std,min,max etc of each column
print(df.describe())

# Count missing values in each column
print(df.isnull().sum())

#Remove duplicates
df.drop_duplicates(inplace=True)


#Fill Missing values with .mean() , mode()[0] ,median()
df['Age'] = df['Age'].fillna(int(df['Age'].median()))
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])

#Rounding and Converting the 'Fare' Column to integer.
df['Fare'] = df['Fare'].round().astype(int)


#categorisation of data ( done with columns with repeating values)
df['Sex'] = df['Sex'].astype("category")
df['Embarked'] = df['Embarked'].astype("category")



#exporting data to new csv file
df.to_csv('titanic_exported.csv',index=False)