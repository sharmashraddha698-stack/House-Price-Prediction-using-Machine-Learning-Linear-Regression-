# House-Price-Prediction-using-Machine-Learning-Linear-Regression-
A machine learning project that predicts house prices using Linear Regression based on important features like area, quality, and garage capacity.
# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project aims to predict house prices using a Machine Learning model.
The model is trained using important features such as overall quality, living area, basement size, and garage capacity.

---

## 📂 Dataset

* Source: Kaggle House Prices Dataset
* Files used:

  * `train.csv` → used for training the model
  * `test.csv` → used for prediction

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🧠 Model Used

* Linear Regression

---

## 🔍 Feature Selection

Important features were selected using **correlation analysis** with the target variable (`Saleprice`).

### Selected Features:

* OverallQual
* GrLivArea
* TotalBsmtSF
* GarageCars
* GarageArea
* Total_Bathrooms
* 1stFlrSF

---

## 🚀 Workflow

1. Load dataset
2. Perform data cleaning
3. Select important features
4. Train model using Linear Regression
5. Predict house prices on test data
6. Save predictions

---

## 📊 Model Prediction

```python
pred = model.predict(test_x)
```

##

---

## 💾 Output

Predicted results are saved as:

```
submission.csv
```

---

## 📌 Conclusion

The model successfully predicts house prices based on selected features.
Feature selection and data preprocessing significantly improve model performance.

---

## ⭐ Future Improvements

* Use advanced models like Random Forest
* Hyperparameter tuning
* Feature engineering

---

## 🙌 Author

Shraddha Sharma

