# 🛡️ Phishing URL Detection Using Machine Learning

A machine learning-based cybersecurity project that detects whether a given URL is **legitimate or potentially phishing**.

The system analyzes the structural and lexical characteristics of URLs and uses a trained **Random Forest classifier** to classify them.

The project includes a complete machine learning pipeline and a **Flask web application** that allows users to enter a URL and receive a real-time prediction.

## 📌 Project Overview

Phishing attacks commonly use malicious URLs to trick users into visiting fake websites and revealing sensitive information.

This project provides an automated approach for identifying suspicious URLs based on their characteristics.

Instead of opening, crawling, or interacting with the target website, the system analyzes the URL itself. This makes the prediction process lightweight and fast.

The system performs:

* URL feature extraction
* Feature preprocessing
* Feature scaling
* PCA dimensionality reduction
* Machine learning classification
* Real-time prediction through a Flask web application

> **Note:** The classifier analyzes URL characteristics and does not guarantee that a website is safe or malicious.

## 🌐 Live Demo

Try the deployed application:

### 🔗 [Phishing URL Detector](https://phising-detector-bca3.onrender.com/)

The application is hosted on **Render** using Flask and Gunicorn.

## 🔄 How It Works

```text
                    User enters URL
                           ↓
                  URL Feature Extraction
                           ↓
                   Feature Preprocessing
                           ↓
                     Feature Scaling
                           ↓
                          PCA
                           ↓
                Random Forest Classifier
                           ↓
              ┌────────────┴────────────┐
              ↓                         ↓
         Legitimate                  Phishing
```

## 🔍 Features Extracted

The system extracts lexical and structural features from URLs, including:

* URL length
* Number of dots (`.`)
* Number of hyphens (`-`)
* Number of digits
* Number of slashes (`/`)
* Number of question marks (`?`)
* Number of equal signs (`=`)
* Number of `@` symbols
* Other URL-based characteristics

These features are used to identify patterns that may help distinguish phishing URLs from legitimate URLs.

## 🧠 Machine Learning Pipeline

The project follows a complete machine learning workflow:

1. Dataset loading and analysis
2. Data cleaning and preprocessing
3. URL feature extraction
4. Exploratory feature analysis
5. Feature scaling
6. PCA-based dimensionality reduction
7. Machine learning model training
8. Model evaluation
9. Saving trained preprocessing objects and model
10. Flask integration
11. Real-time URL prediction

The trained model and preprocessing objects are saved using **Joblib** and loaded by the prediction pipeline.

### Prediction Pipeline

```text
Raw URL
   ↓
Feature Extraction
   ↓
Feature Vector
   ↓
Scaler
   ↓
PCA
   ↓
Random Forest
   ↓
Prediction + Confidence
```

## 🤖 Machine Learning Model

The deployed application uses a **Random Forest Classifier**.

The project also includes trained models for experimentation and comparison, including:

* Random Forest
* Decision Tree
* Logistic Regression
* Support Vector Machine (SVM)

The Random Forest model is used by the deployed application.

## 🌐 Web Application

The Flask web application provides a simple interface where users can:

1. Enter a URL.
2. Submit the URL for analysis.
3. Automatically extract URL features.
4. Apply the trained preprocessing pipeline.
5. Generate a machine learning prediction.
6. Display the classification result and confidence.

Example:

```text
Input:
https://example.com

Output:
Legitimate URL
```

Potentially suspicious URLs may produce:

```text
Input:
http://suspicious-example.com/...

Output:
Potentially Phishing URL
```

## 🛠️ Technologies Used

| Technology   | Purpose                       |
| ------------ | ----------------------------- |
| Python       | Main programming language     |
| Pandas       | Data processing               |
| NumPy        | Numerical operations          |
| Scikit-learn | Machine learning              |
| PCA          | Dimensionality reduction      |
| Joblib       | Saving and loading ML objects |
| Flask        | Web application backend       |
| HTML         | Web interface                 |
| CSS          | Frontend styling              |
| Gunicorn     | Production WSGI server        |
| Render       | Cloud deployment              |

## 📁 Project Structure

```text
phisingdetector/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── decision_tree_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   ├── svm_model.pkl
│   ├── scaler.pkl
│   └── pca.pkl
│
├── src/
│   ├── feature_extraction.py
│   └── predict.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── data/
│   └── ...
│
└── notebooks/
    └── ...
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/rishabrawat9000-ux/phising_detector.git
cd phising_detector
```

Create a virtual environment:

```bash
python3 -m venv venv313
```

Activate it on Linux:

```bash
source venv313/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running Locally

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

### Running with Gunicorn

For production-style local testing:

```bash
gunicorn app:app
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## ☁️ Deployment

The application is deployed using **Render**.

### Render Configuration

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

### 🌐 Live Application

**https://phising-detector-bca3.onrender.com/**

The deployment uses Gunicorn as the production WSGI server.

## 🎯 Future Improvements

Possible improvements include:

* Adding more URL and domain-based features
* Using larger and more diverse datasets
* Performing additional model comparisons
* Improving precision, recall, and overall model performance
* Improving confidence estimation
* Integrating threat-intelligence APIs
* Adding a browser extension
* Implementing real-time URL reputation checks
* Improving the user interface
* Adding model explainability
* Deploying the model through an API

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**.

A machine learning prediction cannot guarantee that a URL is completely safe or malicious. The system analyzes URL characteristics and should not be considered a replacement for professional security tools or threat-intelligence services.

Users should always exercise caution when accessing unfamiliar links.
