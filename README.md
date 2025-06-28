# 💻 Laptop Price Prediction with SVR

A machine learning project that predicts laptop prices based on key specifications, using a **Support Vector Regression (SVR)** model with hyperparameter tuning and **GridSearchCV**.

---

## 📌 Project Objective

> **Goal:** Predict accurate laptop prices based on features like processor, RAM, storage, display, and other specs — helping buyers and sellers estimate fair market value.

---

## 📂 Dataset

- 📥 **Source:** [Kaggle](https://www.kaggle.com/) or other online laptop spec datasets.
- Includes columns such as:
  - **Brand**
  - **Processor**
  - **RAM**
  - **Storage**
  - **Display Size**
  - **Graphics Card**
  - **Operating System**
  - **Price** (Target)

---

## 🧩 Model

- 📊 **Model Used:** Support Vector Regression (**SVR**)
- 🧪 **Tuning:** Hyperparameter tuning with **GridSearchCV**
- 🎯 **Accuracy Achieved:** ~87% on test data

---

## ⚙️ Highlights

- 📌 **Preprocessing:** 
  - Handled categorical & numerical features
  - Feature engineering (e.g., combining storage types)
  - Used **Pipeline** and **ColumnTransformer** for clean workflow
- 🔍 **Hyperparameter Tuning:** Optimized `C`, `kernel`, `gamma` for best performance
- 🧩 Modular, reusable code for quick re-training

---

## 🚀 How to Run Locally

1️⃣ **Clone the repo**
```bash
git clone https://github.com/yourusername/laptop-price-prediction.git
cd laptop-price-prediction
