# Wine Preprocessing Pipeline

This project demonstrates a complete data preprocessing workflow using scikit-learn and the Wine dataset. It includes imputation, scaling, feature selection, dimensionality reduction, normalization, and data export.

## Dataset

The [Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html) is a classic multi-class classification dataset included in scikit-learn. It contains 13 numeric features representing chemical analysis results of wines grown in the same region in Italy, with the target indicating wine type (3 classes).

## Steps Performed

1. **Loading the dataset**  
   The dataset is loaded from `sklearn.datasets` and converted to a pandas DataFrame.

2. **Imputation**  
   Missing values (simulated) are filled using the mean strategy with `SimpleImputer`.

3. **Standardization**  
   All numeric features are standardized using `StandardScaler`.

4. **Feature Selection**  
   The 8 most relevant features are selected using `SelectKBest` with the `chi2` scoring function.

5. **Dimensionality Reduction**  
   Principal Component Analysis (PCA) is applied to reduce the features to 2 dimensions.

6. **Normalization**  
   The 2D PCA output is normalized using L2 norm via `Normalizer`.

7. **Final Output**  
   The class label is added back to the processed dataset and saved as `wine_final.csv`.

## File

- `wine_final.csv`: Contains the final processed dataset with 2 PCA features (`PC1`, `PC2`) and the class label.

## Softw/Tools Used

- Python 3
- pandas
- NumPy
- scikit-learn


