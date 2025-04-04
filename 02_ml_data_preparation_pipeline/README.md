# 🧪 Exercise 0303 – Scaling and Normalisation

This exercise is part of the *Programming for Machine Learning* course at Noroff.

The goal is to split a dataset, apply different scaling and normalisation techniques, compare the results, and save the final preprocessed data for future use in a machine learning model.

---

## ✅ Steps completed:

1. **Load the dataset** from `data0303.csv`.
2. **Split the data** into training and test sets using an 80/20 ratio.
3. **Apply and compare three scaling methods** to the training features:
   - StandardScaler
   - MinMaxScaler
   - MaxAbsScaler
4. **Select one scaler** (`MinMaxScaler`) to use for the next step.
5. **Apply and compare three normalisation methods** on the scaled data:
   - L1 normalisation
   - L2 normalisation
   - Max normalisation
6. **Select one normalisation** (`Max norm`) as the final preprocessing step.
7. **Recombine the final `X_train` data** with the corresponding `y_train` class labels.
8. **Export the final dataset** as `0303_updated.csv`.

---

## 🛠️ Technologies used

- Python 3
- pandas
- numpy
- scikit-learn (StandardScaler, MinMaxScaler, MaxAbsScaler, Normalizer)

---

## 📁 Output

A fully scaled and normalised training dataset saved as:
```bash
0303_updated.csv
