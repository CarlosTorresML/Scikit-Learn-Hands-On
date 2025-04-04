import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, Normalizer

# Load dataset
df = pd.read_csv('data0303.csv')

# Display dataset shape and the first 20 rows
print(df.shape)
print(df.head(20))

# Separate features and target
X = df.drop(columns=['class'])      # Features (input variables)
y = df[['class']]                   # Target (class column)

# Split into training and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

# Apply different scalers to the training set
std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
maxabs_scaler = MaxAbsScaler()

X_train_std = std_scaler.fit_transform(X_train)
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_train_maxabs = maxabs_scaler.fit_transform(X_train)

# Print first few rows of each scaled version to compare them
print("StandardScaler:")
print(pd.DataFrame(X_train_std).head())

print("\nMinMaxScaler:")
print(pd.DataFrame(X_train_minmax).head())

print("\nMaxAbsScaler:")
print(pd.DataFrame(X_train_maxabs).head())

# Select MinMaxScaler as the preferred scaled data
X_train = X_train_minmax

# Apply different normalisation methods
l1_norm = Normalizer(norm='l1')
l2_norm = Normalizer(norm='l2')
max_norm = Normalizer(norm='max')

X_train_l1 = l1_norm.fit_transform(X_train)
X_train_l2 = l2_norm.fit_transform(X_train)
X_train_max = max_norm.fit_transform(X_train)

# Compare normalised results
print("\nL1 Normalised:")
print(pd.DataFrame(X_train_l1).head())

print("\nL2 Normalised:")
print(pd.DataFrame(X_train_l2).head())

print("\nMax Normalised:")
print(pd.DataFrame(X_train_max).head())

# Select Max Normalisation as final data
X_train = X_train_max

# Rebuild DataFrame with column names and original index
df1 = pd.DataFrame(X_train, columns=X.columns, index=y_train.index)
df2 = y_train
df_final = pd.concat([df1, df2], axis=1)

# Export final DataFrame to CSV
df_final.to_csv('0303_updated.csv', index=False)
