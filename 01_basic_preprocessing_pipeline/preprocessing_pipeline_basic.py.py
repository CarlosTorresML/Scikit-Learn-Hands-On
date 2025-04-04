import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Define the raw data
data = [
    [25, 30000, 'Oslo', 'M'],
    [None, 50000, 'Bergen', 'F'],
    [35, None, 'Oslo', None],
    [42, 80000, 'Stavanger', 'M'],
    [None, None, 'Bergen', 'F']
]

columns = ['age', 'income', 'city', 'gender']

# Create the initial DataFrame
df = pd.DataFrame(data, columns=columns)

# Impute missing numerical values using the median
median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df[['age']] = median_imputer.fit_transform(df[['age']])
df[['income']] = median_imputer.fit_transform(df[['income']])

# Impute missing categorical values using the most frequent value
freq_imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df[['city']] = freq_imputer.fit_transform(df[['city']])
df[['gender']] = freq_imputer.fit_transform(df[['gender']])

# One-hot encode 'city'
encoder_city = OneHotEncoder(dtype=int, sparse_output=False)
city_encoded = encoder_city.fit_transform(df[['city']])
city_df = pd.DataFrame(city_encoded, columns=encoder_city.get_feature_names_out(['city']), index=df.index)

# One-hot encode 'gender'
encoder_gender = OneHotEncoder(dtype=int, sparse_output=False)
gender_encoded = encoder_gender.fit_transform(df[['gender']])
gender_df = pd.DataFrame(gender_encoded, columns=encoder_gender.get_feature_names_out(['gender']), index=df.index)

# Combine all columns into a final DataFrame
df_final = pd.concat([df.drop(columns=['city', 'gender']), city_df, gender_df], axis=1)

# Display the final DataFrame
print(df_final)













