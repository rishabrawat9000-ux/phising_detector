# Phishing URL Detection Using Machine Learning

A machine learning-based cybersecurity project that detects whether a given URL is **legitimate or potentially phishing**. The system analyzes the structural and lexical characteristics of URLs and uses a trained machine learning model to classify them.

## 📌 Project Overview

Phishing attacks commonly use malicious URLs to trick users into visiting fake websites and revealing sensitive information. This project aims to provide an automated method for identifying suspicious URLs based on their characteristics.

Instead of opening or crawling the website, the system analyzes the URL itself. This makes the prediction process lightweight and fast.

The project includes both a **machine learning pipeline** and a **Flask web application**, allowing users to enter a URL and receive a prediction through a web interface.

## 🔄 How It Works

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
        Trained ML Classification Model
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
    Legitimate                Phishing


## 🔍 Features Extracted

The system extracts lexical features from URLs, including:

* URL length
* Number of dots (`.`)
* Number of hyphens (`-`)
* Number of digits
* Number of slashes (`/`)
* Number of question marks (`?`)
* Number of equal signs (`=`)
* Number of `@` symbols
* Other URL-based characteristics

These features are used to identify patterns that may distinguish phishing URLs from legitimate URLs.

## 🧠 Machine Learning Pipeline

The project follows a complete machine learning workflow:

1. Dataset loading and analysis
2. Data cleaning and preprocessing
3. URL feature extraction
4. Feature analysis
5. Feature scaling
6. PCA-based dimensionality reduction
7. Model training
8. Model evaluation
9. Saving the trained model
10. Integrating the model with Flask
11. Real-time URL prediction

The trained preprocessing objects and model are saved using **Joblib** so they can be reused when making predictions.

## 🌐 Web Application

The Flask application provides a simple interface where users can:

1. Enter a URL.
2. Submit the URL for analysis.
3. Extract its features automatically.
4. Process the features using the trained pipeline.
5. Receive a classification result.

Example:

```text
Input:
https://example.com

Output:
Legitimate URL
```

or

```text
Input:
http://suspicious-example.com/...

Output:
Potentially Phishing URL
```

## 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Main programming language |
| Pandas       | Data processing           |
| NumPy        | Numerical operations      |
| Scikit-learn | Machine learning          |
| PCA          | Dimensionality reduction  |
| Joblib       | Saving/loading ML objects |
| Flask        | Web application backend   |
| HTML         | Web interface             |
| CSS          | Frontend styling          |
| Gunicorn     | Production server         |

## 📁 Project Structure

```text
phisingdetector/
│
├── app.py
├── predict.py
├── requirements.txt
│
├── model.pkl
├── scaler.pkl
├── pca.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
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

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open the address in your browser and enter a URL to test the system.

## ☁️ Deployment

The application can be deployed using platforms such as **Render** or other services that support Python/Flask applications.

For production deployment with Gunicorn:

```bash
gunicorn app:app
```

## 🎯 Future Improvements

Possible improvements include:

* Adding more URL and domain-based features
* Using larger and more diverse datasets
* Comparing multiple machine learning algorithms
* Improving model accuracy and recall
* Adding confidence scores
* Integrating threat-intelligence APIs
* Adding a browser extension
* Implementing real-time URL scanning
* Improving the user interface

## ⚠️ Disclaimer

This project is intended for **educational and research purposes**. A machine learning prediction cannot guarantee that a URL is completely safe or malicious. Users should always exercise caution when accessing unfamiliar links.
