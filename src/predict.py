import os
import sys

import joblib
import pandas as pd


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)


from src.feature_extraction import extract_features



MODEL_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "random_forest_model.pkl"
)

SCALER_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "scaler.pkl"
)

PCA_PATH = os.path.join(
    PROJECT_DIR,
    "models",
    "pca.pkl"
)



model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
pca = joblib.load(PCA_PATH)



def predict_url(url):
    features = extract_features(url)

    X = pd.DataFrame([features])

    X_scaled = scaler.transform(X)

    X_pca = pca.transform(X_scaled)

    prediction = model.predict(X_pca)[0]

    probabilities = model.predict_proba(X_pca)[0]

    confidence = max(probabilities) * 100


    if prediction == 1:
        result = "legitimate"
    else:
        result = "phishing"

    return result, confidence, probabilities


if __name__ == "__main__":

    url = input("Enter URL: ").strip()

    if not url:
        print("Please enter a URL.")
        sys.exit(1)

    try:

        result, confidence, probabilities = predict_url(url)

        print("\nURL:", url)
        print("Prediction:", result)
        print(f"Confidence: {confidence:.2f}%")

        print("\nClass probabilities:")

        for class_label, probability in zip(
            model.classes_,
            probabilities
        ):
            print(
                f"Class {class_label}: "
                f"{probability * 100:.2f}%"
            )

    except Exception as e:

        print("\nPrediction error:")
        print(e)