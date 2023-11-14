import os
import pickle
import pandas as pd
from datetime import datetime
from flask import Flask, request, Response
from cardio.Cardio import Cardio

# Get model pkl
model = pickle.load(open("model/LGBM_.best_model.pkl", "rb"))

# Initiate API
app = Flask(__name__)


@app.route("/cardio", methods=["POST"])
def cardio():
    test_json = request.get_json()

    if test_json:  # there is data
        # Load data
        if isinstance(test_json, type(dict)):  # unique example
            raw_df = pd.DataFrame(test_json)
        else:  # multiple examples
            raw_df = pd.DataFrame(test_json)

        # Instantiate Cardio class
        pipeline = Cardio()

        # data cleaning
        df1 = pipeline.data_cleaning(raw_df)

        # feature engineering
        df2 = pipeline.feature_engineering(df1)

        # data preparation
        df3 = pipeline.data_preparation(df2)

        # Predictions
        predictions = pipeline.get_prediction(model, raw_df, df3)

        return predictions.to_json(orient="records", date_format="iso")

    else:
        return Response("{}", status=200, mimetype="application/json")


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
