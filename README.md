# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts residential house prices using Machine Learning. The model is built using **Linear Regression** and trained on the Kaggle House Prices dataset. The workflow includes data preprocessing, feature engineering, exploratory data analysis (EDA), model training, evaluation, and prediction on unseen data.

---

## 🎯 Objective

The objective of this project is to build a regression model that accurately predicts the selling price of a house based on its key characteristics.

---

## 📂 Dataset

The dataset consists of two files:

* **train.csv** – Contains the training data along with the target variable (`SalePrice`).
* **test.csv** – Contains unseen data used for generating predictions.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Checked missing values
* Correlation analysis
* Distribution of the target variable (`SalePrice`)
* Outlier detection using boxplots
* Feature selection based on correlation and domain knowledge

---

## ⚙️ Feature Engineering

A new feature, **Total_Bathrooms**, was created to improve the predictive performance of the model.

Selected features used for training:

* OverallQual
* GrLivArea
* TotalBsmtSF
* GarageCars
* GarageArea
* Total_Bathrooms
* 1stFlrSF

---

## 🤖 Machine Learning Model

**Algorithm Used**

* Linear Regression

### Workflow

1. Load the dataset
2. Data preprocessing
3. Handle missing values
4. Feature engineering
5. Feature selection
6. Train the Linear Regression model
7. Evaluate model performance
8. Predict house prices for the test dataset
9. Generate Kaggle submission file

---

## 📈 Model Evaluation

The model was evaluated using standard regression metrics such as:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

The evaluation results indicate that the model performs well in predicting house prices using the selected features.

---

## 📁 Project Structure

```text
House-Price-Prediction/
│── train.csv
│── test.csv
│── House_Price_Prediction.ipynb
│── submission.csv
│── requirements.txt
│── README.md
```

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone <repository-link>
```

2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook.

```bash
jupyter notebook
```

4. Run all the cells to train the model and generate predictions.

---

## 📌 Results

The trained model successfully predicts house prices for unseen data and generates a Kaggle-compatible `submission.csv` file. The project demonstrates the complete machine learning workflow, including preprocessing, feature engineering, model development, evaluation, and prediction.

---

## 🔮 Future Improvements

* Compare multiple regression models such as Random Forest and XGBoost.
* Perform hyperparameter tuning.
* Build a web application using Streamlit or Flask for real-time predictions.
* Deploy the model on a cloud platform.

---

## 👩‍💻 Author

**Shraddha Sharma**

If you found this project helpful, feel free to ⭐ the repository.
