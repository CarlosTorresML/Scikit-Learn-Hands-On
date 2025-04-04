# 🔧 Data Preprocessing: Imputation & One-Hot Encoding

This project is a small but practical example of how to preprocess a mixed dataset in Python using `pandas` and `scikit-learn`.

## 🧠 Goal

Prepare a dataset for machine learning training by handling:
- Missing values in both numerical and categorical features
- One-hot encoding for categorical variables

## 💡 What you'll find inside

- Usage of `SimpleImputer` to fill in missing values
- Usage of `OneHotEncoder` to transform text into numbers
- Clean and ready-to-use DataFrame for machine learning models

## 📂 Files

- `preprocessing_task.py`: The complete Python script
- `README.md`: This file with explanations

## 🛠️ Tools used

- Python 3
- pandas
- scikit-learn

## 📊 Dataset structure

The original dataset includes 5 rows with missing values in both numerical and categorical columns:

| age | income | city       | gender |
|-----|--------|------------|--------|
| 25  | 30000  | Oslo       | M      |
| NaN | 50000  | Bergen     | F      |
| 35  | NaN    | Oslo       | NaN    |
| 42  | 80000  | Stavanger  | M      |
| NaN | NaN    | Bergen     | F      |

## ✅ Result

A fully numerical DataFrame with no missing values, ready to be used in ML models.

---
