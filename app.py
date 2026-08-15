# pyright: reportMissingImports=false
from flask import Flask, render_template, request  # Import Flask and related modules
from src.predict import predict_url

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    url = ""
    error = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if not url:
            error = "Please enter a URL."

        else:
            try:
                result, confidence, _ = predict_url(url)

            except Exception as e:
                error = str(e)

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        url=url,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)