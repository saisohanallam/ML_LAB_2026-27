import os

import pandas as pd
from flask import Flask, flash, render_template, request

from src.segmentation import load_sample_data, run_analysis

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB upload limit


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            k = int(request.form.get("clusters", 4))
            if not 2 <= k <= 8:
                raise ValueError("Choose between 2 and 8 clusters.")

            upload = request.files.get("dataset")
            if upload and upload.filename:
                if not upload.filename.lower().endswith(".csv"):
                    raise ValueError("Please upload a .csv file.")
                df = pd.read_csv(upload)
                source = upload.filename
            else:
                df = load_sample_data()
                source = "Built-in synthetic demonstration dataset"

            result = run_analysis(df, k)
            result["source"] = source
        except Exception as exc:  # show any problem to the user instead of a 500
            flash(str(exc), "error")
    return render_template("index.html", result=result)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)), debug=False)
