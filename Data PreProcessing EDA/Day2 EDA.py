import pandas as pd 
from sklearn.preprocessing import LabelEncoder,StandardScaler



#labeling Data in range of 0-1 for better understanding by Model
le = LabelEncoder()
data = pd.read_csv('./titanic_exported.csv')

df = pd.DataFrame(data)

#One hot encoding - making seperate columns for categorisation of data, dropping first column 
# for reducing multicollinearity.
df  = pd.get_dummies(df, columns=["Embarked"], drop_first=True)



#feature scaling - scaling values so that they can compete on same leve
# eg - age = 25 and salary = 1,00,000


# -------------------------------
# 2. Feature Engineering
# -------------------------------

# family_size = sibsp + parch + 1 (self)
df["family_size"] = df["sibsp"] + df["parch"] + 1

# is_alone = 1 if family_size == 1 else 0
df["is_alone"] = (df["family_size"] == 1).astype(int)

print("\n[INFO] Added 'family_size' and 'is_alone' columns.")
print(df[["sibsp", "parch", "family_size", "is_alone"]].head(5))

# -------------------------------
# 3. Scaling numeric columns
# -------------------------------

# We keep 'survived' untouched because it's our target variable
numeric_cols = df.select_dtypes(include="number").columns.tolist()
exclude_cols = ["survived"]  # don't scale the target
cols_to_scale = [col for col in numeric_cols if col not in exclude_cols]

# Apply StandardScaler: mean=0, std=1
scaler = StandardScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])


df.to_csv('Exported_titanic_2.csv',index=False)
