# 🧠 Human Stress Detection Using Machine Learning

A machine learning–powered web application that predicts a person’s **stress level** using their **sleeping habits**, **lifestyle factors**, and **health indicators**. The app provides real-time predictions through a simple web interface built with Flask.

---

## 📌 Problem Statement

Stress is a growing global concern, often linked to poor sleep, inactivity, and unhealthy routines. Early stress detection can help individuals take preventive actions and improve mental health. This project aims to:

> 🧪 Predict an individual's **stress level** using features like sleep duration, physical activity, and heart rate using supervised machine learning.

---

## 🎯 Objectives

- Analyze the correlation between sleep habits, lifestyle, and stress.
- Build an ML model to classify stress levels based on numeric and categorical inputs.
- Deploy a lightweight and user-friendly **Flask-based web app** for real-time predictions.

---

## 🗃️ Dataset Details

- **Name**: Sleep Health and Lifestyle Dataset  
- **Format**: CSV  
- **Rows**: ~370 entries  
- **Label**: `Stress Level` (values from 3 to 8)

### 🔑 Features Used:
| Feature              | Description                                   |
|----------------------|-----------------------------------------------|
| Gender               | Male/Female                                   |
| Age                  | Integer (years)                               |
| Occupation           | Student, Engineer, Nurse, etc.                |
| Sleep Duration       | Hours slept per day (float)                   |
| Quality of Sleep     | Rating from 1–10                              |
| Physical Activity    | Rating from 1–10                              |
| BMI Category         | Normal, Overweight, Obese                     |
| Heart Rate           | Average BPM                                   |
| Daily Steps          | Number of steps walked daily                  |
| Sleep Disorder       | None, Insomnia, Sleep Apnea                   |

---

## 🧠 Machine Learning Approach

### ✅ Data Preprocessing
- **Label Encoding** for categorical columns using `LabelEncoder`.
- **Splitting** into training (80%) and testing (20%) sets.
- No missing values; hence, no imputation needed.

### 🤖 Algorithms Tested
| Model                 | Accuracy  |
|----------------------|-----------|
| ✅ Random Forest      | 98.67%    |
| Naive Bayes          | 89.33%    |
| SVM (RBF Kernel)     | 41.33%    |
| Logistic Regression  | 88.00%    |
| Decision Tree        | 97.33%    |
| K-Nearest Neighbors  | 93.33%    |

- **Best model**: `RandomForestClassifier` (saved using `joblib`)
- Evaluation metrics include **Accuracy**, **Precision**, **Recall**, **F1-Score**, and **Confusion Matrix**.

---

## 💡 Project Workflow

```

1. Collect and load data → CSV file
2. Preprocess data → Label encode + split train/test
3. Train ML models → Multiple classifiers
4. Evaluate → Accuracy, F1, Confusion Matrix
5. Save best model → joblib
6. Build Flask app → HTML frontend + Python backend
7. Make real-time predictions through form input

````

---

## 💻 Web App Features

- Form-based UI with input fields for:
  - Gender, Age, Occupation
  - Sleep Duration, Quality of Sleep
  - BMI, Heart Rate, Steps
  - Sleep Disorder
- Results displayed on same page (stress level prediction)
- Backend: Flask
- Frontend: HTML & CSS
- Model loading: Random Forest model with encoded inputs

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/frijo12/stress-detection-ml.git
cd stress-detection-ml
````

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Start the Flask Server

```bash
python app.py
```

### 4. Open in Browser

Visit: [http://localhost:5000](http://localhost:5000)

---

## 📈 Model Evaluation Details

### 🔍 Random Forest

* Accuracy: **98.67%**
* F1 Score: 98.67%
* Precision: 98.79%
* Recall: 98.67%

### Confusion Matrix:

```
[[12  0  0  0  0  0]
 [ 0 10  0  0  0  0]
 [ 0  0 13  1  0  0]
 [ 0  0  0 10  0  0]
 [ 0  0  0  0 12  0]
 [ 0  0  0  0  0 17]]
```

(See full metrics in the “Model Evaluation Details” section of this repo.)

---

## 📁 Project Structure

```
stress-detection-ml/
├── app.py                      # Flask backend
├── app/                        # Encoders
│   ├── encoder_Gender.pkl
│   └── ...
├── models/                     # Trained model
│   └── model_random_forest.pkl
├── templates/
│   └── index.html              # Frontend UI
├── dataset/
│   └── Sleep_health_and_lifestyle_dataset.csv
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```txt
Flask==3.0.0
pandas==2.2.0
numpy==1.26.0
scikit-learn==1.4.2
joblib==1.3.2
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📌 Future Improvements

* Add user authentication (login system)
* Graph-based visualization of results
* Deploy on Render / Heroku / Railway
* Collect live user data and re-train model

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Author

**Frijo Antony CF**
Final Year B.Tech CSE Student
Passionate about AI, ML, and building intelligent web applications
📫 Contact: [LinkedIn](www.linkedin.com/in/frijoantonycf)

---

## 🙌 Acknowledgments

* [Kaggle Datasets](https://www.kaggle.com/)
* Scikit-learn Documentation
* Flask Documentation
