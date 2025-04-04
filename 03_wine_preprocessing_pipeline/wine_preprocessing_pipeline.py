import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Normalizer, MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.decomposition import PCA


# Loading the dataset
data, target = datasets.load_wine(return_X_y=True)
data = pd.DataFrame(data)
data['class'] = target

# Applying SimpleImputer to fill nan values
si = SimpleImputer(missing_values=np.nan, strategy='mean')
data_imputed = si.fit_transform(data.drop(columns=['class']))
data_imputed = pd.DataFrame(data_imputed, columns=data.drop(columns=['class']).columns)

# Scale numerical data using MinMaxScaler
minmax_scaler = MinMaxScaler()
data_scaled = minmax_scaler.fit_transform(data_imputed)
data_scaled = pd.DataFrame(data_scaled, columns=data_imputed.columns)

# Using chi2 to select the best 8 characteristics
selector = SelectKBest(chi2, k=8)
data_reduced = selector.fit_transform(data_scaled, target)
selected_columns = data_scaled.columns[selector.get_support()]
data_reduced = pd.DataFrame(data_reduced, columns=selected_columns)

# Reduce to 2D with PCA
pca = PCA(n_components=2)
data_reduced_2d = pca.fit_transform(data_reduced)
data_reduced_2d = pd.DataFrame(data_reduced_2d, columns=['PC1','PC2'])

# Normalize with 'l2'
norm = Normalizer(norm='l2')
data_normalized = norm.fit_transform(data_reduced_2d)
data_normalized = pd.DataFrame(data_normalized, columns=['PC1','PC2'])

# Adding the 'class' column
data_normalized['class'] = data['class'].values

# Saving to CSV file
data_normalized.to_csv('wine_final.csv', index=False)
