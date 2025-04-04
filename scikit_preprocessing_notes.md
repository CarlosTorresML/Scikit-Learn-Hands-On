# Scikit-learn Preprocessing Summary (🇬🇧 English, check below ⬇️ for Spanish 🇪🇸)

This document summarizes the full preprocessing pipeline using scikit-learn, explained in simple and practical terms. Ideal for quick review and reference.

---

## 🧹 1. Missing Values  
**What:** Fill or remove empty cells (NaN)  
**Tool:** `SimpleImputer()`

---

## 🏷️ 2. Transform Categorical Data  
**What:** Convert text/labels into numbers  
- `OrdinalEncoder()` → for ordered categories  
- `OneHotEncoder()` → for unordered categories  
- `LabelEncoder()` → for simple cases (⚠️ not recommended for features)

---

## 🧮 3. Transform Numerical Data  
**What:** Group or modify numeric values  
- `KBinsDiscretizer()` → splits into bins  
- `Binarizer()` → turns values into 0/1  
- `FunctionTransformer()` → apply custom logic

---

## ✂️ 4. Split the Dataset  
**What:** Divide into training and test sets  
**Tool:** `train_test_split()`

---

## 📏 5. Scale Data  
**What:** Make numeric features use similar ranges  
- `StandardScaler()` → mean = 0, std = 1  
- `MinMaxScaler()` → scaled between 0 and 1  
- `MaxAbsScaler()` → scaled between -1 and 1 (preserves sign)

---

## 🧼 6. Normalize Data (per row)  
**What:** Make each row have similar magnitude  
- `Normalizer(norm='l1')` → sum of values = 1  
- `Normalizer(norm='l2')` → Euclidean norm = 1  
- `Normalizer(norm='max')` → largest value = 1

---

## 🎯 7. Feature Selection  
**What:** Keep only the most useful columns  
**Tool:** `SelectKBest(score_func=chi2)`

---

## 🔻 8. Dimensionality Reduction  
**What:** Combine features into fewer new ones  
**Tool:** `PCA(n_components=...)`

---

## 📊 (Optional) Model Evaluation  
**What:** Check predictions  
- `confusion_matrix()`  
- `classification_report()`

---

## ✅ Recommended Order

1. Imputation  
2. Categorical/Numerical transformation  
3. `train_test_split()`  
4. Scaling  
5. Feature selection  
6. PCA  
7. Normalization  
8. Add class and export  

----------------------------------------------

# Resumen del Preprocesamiento con Scikit-learn (🇪🇸)

Este documento resume todo el flujo de preprocesamiento usando scikit-learn, explicado de forma clara y sencilla. Ideal para repasar o consultar rápidamente.

---

## 🧹 1. Valores Faltantes  
**Qué hace:** Rellena o elimina celdas vacías (`NaN`)  
**Función:** `SimpleImputer()`

---

## 🏷️ 2. Transformar Datos Categóricos  
**Qué hace:** Convierte texto o etiquetas en números  
- `OrdinalEncoder()` → para categorías con orden  
- `OneHotEncoder()` → para categorías sin orden  
- `LabelEncoder()` → para casos simples (⚠️ no recomendado para variables independientes)

---

## 🧮 3. Transformar Datos Numéricos  
**Qué hace:** Agrupa o modifica valores numéricos  
- `KBinsDiscretizer()` → agrupa en intervalos (bins)  
- `Binarizer()` → convierte en 0 o 1 según un umbral  
- `FunctionTransformer()` → aplica una función personalizada

---

## ✂️ 4. Dividir el Dataset  
**Qué hace:** Separa en conjuntos de entrenamiento y prueba  
**Función:** `train_test_split()`

---

## 📏 5. Escalar Datos  
**Qué hace:** Ajusta las escalas de las columnas numéricas  
- `StandardScaler()` → media 0, desviación estándar 1  
- `MinMaxScaler()` → valores entre 0 y 1  
- `MaxAbsScaler()` → valores entre -1 y 1 (mantiene el signo)

---

## 🧼 6. Normalizar Datos (por fila)  
**Qué hace:** Ajusta la magnitud de cada fila para que sea similar  
- `Normalizer(norm='l1')` → suma de la fila = 1  
- `Normalizer(norm='l2')` → norma euclidiana = 1  
- `Normalizer(norm='max')` → valor máximo = 1

---

## 🎯 7. Selección de Características  
**Qué hace:** Elige solo las columnas más útiles  
**Función:** `SelectKBest(score_func=chi2)`

---

## 🔻 8. Reducción de Dimensiones  
**Qué hace:** Crea nuevas columnas combinando las originales para simplificar  
**Función:** `PCA(n_components=...)`

---

## 📊 (Opcional) Evaluación del Modelo  
**Qué hace:** Mide si el modelo acierta o se equivoca  
- `confusion_matrix()`  
- `classification_report()`

---

## ✅ Orden Recomendado

1. Imputación de valores faltantes  
2. Transformación de datos categóricos y numéricos  
3. División con `train_test_split()`  
4. Escalado  
5. Selección de características  
6. Reducción de dimensiones con PCA  
7. Normalización  
8. Añadir columna 'class' y guardar/exportar

