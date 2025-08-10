# Feature selection: keep only the most useful columns for predicting the target.

# Near-zero variance: columns that hardly change → not useful.

# Multicollinearity: two features are highly correlated → keep one.

# Mutual Information: measures how much a feature tells us about the target.


import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split



df = pd.read_csv('./Datasets/Exported_final.csv')
assert "Survived" in df.columns

# split into features (X) and target (y)
y = df["Survived"] # the thing we want to predict (here, survived).
X = df.drop(columns=["Survived"]) # the input columns used to predict.



#Remove zero-variance features

#What are zero-variance features?
# A column where all values are the same (or almost the same) for every row.

# Example: If a column "ship_name" was "Titanic" for all passengers, it tells the model nothing — it’s useless.
#We drop these because:

# They don’t help prediction (no variety = no information).

# They just waste memory and can slow training.


vt = VarianceThreshold(thresold=0.0) #drop columns with exactly 0 variance

# Apply to X (features only)
X_vt = vt.fit_transform(X)

#get list of columns we kept
kept_by_vt = X.columns[vt.get_support()].tolist()


# List of dropped columns
dropped_vt = [col for col in X.columns if col not in kept_by_vt]

print("Dropped zero-variance columns:", dropped_vt)
print("X shape before:", X.shape, " | after:", X_vt.shape)



#Remove highly correlated fields
# Why remove highly correlated features?
# If two columns are very similar (e.g., correlation ≥ 0.9), they carry almost the same information.

# This can cause multicollinearity, which:

# Makes models unstable (especially linear models like Logistic Regression).

# Can slow training without improving accuracy.

# Example:

# "fare_usd" and "fare_euro" might have a correlation of 1.0 (just currency conversion).

# Keeping both is redundant → we drop one.



import numpy as np

corr_matrix = X.corr().abs()

#look at only uppper traingle to avoid duplicates
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape) k=1).astype(bool))

#find features with correaltion >=90
to_drop_corr = [column for column in upper.columns if any(upper[columns] >= 0.90)]

#drop them
X = X.drop(columns=to_drop_corr,errors="ignore")



# What is Mutual Information (MI)?
# MI measures how much knowing a feature reduces uncertainty about the target.

# Higher MI score → the feature is more useful for predicting y.

# Unlike correlation, MI can detect non-linear relationships too.

# Think of it like:

# “How much does this feature help me guess the answer?”


from sklearn.feature_selection import SelectKBest, mutual_info_classif

#how many top features to keep
K = min(10,X.shape(1)) #keep upto 10 or all if fewer

#create selector
selector = SelectKBest(score_func=mutual_info_classif,k=k)

#fit on Data
kept_by_mi = X.columns[selectpr.get_support()].tolist()


# Show features with scores
scores = selector.scores_
feature_scores = list(zip(X.columns,scores))
feature_scores = sorted(feature_scores,key=lambda t: t[1],reverse=True)

#keep only top features
X =X[kept_by_mi]



#training and test split
# Why split the dataset?
# We train the model on training data and check its performance on unseen test data.

# This ensures we know how well the model will generalize to real-world cases.

# If we trained & tested on the same data → accuracy would be misleading.

# Stratified splitting
# Our target (survived) has two classes: 0 (died) and 1 (survived).

# Stratification keeps the same class ratio in both train & test sets.

# Without it, you might get too many survivors in train and too few in test (or vice versa).

from sklearn.model_selection import train_test_split

#splitting data into train and test
X_train, X_test , y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

train_df = X_train.copy()
train_df["Survived"] = y_train

test_df = X_test.copy()
test_df["Survived"] = y_test

