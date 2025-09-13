from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load model & encoders
with open("model.pkl", "rb") as f:
    saved = pickle.load(f)
model = saved["model"]
encoders = saved["encoders"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect input values from form
    features = [x for x in request.form.values()]
    df = pd.DataFrame([features], columns=[
        "Latitude", "Longitude", "Rainfall (mm)", "Temperature (°C)",
        "Humidity (%)", "River Discharge (m³/s)", "Water Level (m)",
        "Elevation (m)", "Land Cover", "Soil Type", "Population Density",
        "Infrastructure", "Historical Floods"
    ])

    # --- Convert numeric columns only ---
    numeric_cols = ["Latitude","Longitude","Rainfall (mm)","Temperature (°C)",
                    "Humidity (%)","River Discharge (m³/s)","Water Level (m)",
                    "Elevation (m)","Population Density","Historical Floods"]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # safely convert numbers

    # --- Encode categorical columns only ---
    categorical_cols = ["Land Cover", "Soil Type", "Infrastructure"]

    for col in categorical_cols:
        # Standardize input to match training case
        df[col] = df[col].str.capitalize()
        # Handle unseen categories by mapping to first class as default
        df[col] = df[col].apply(lambda x: x if x in encoders[col].classes_ else encoders[col].classes_[0])
        # Transform using saved LabelEncoder
        df[col] = encoders[col].transform(df[col])

    # Predict
    output = model.predict(df)[0]

    return render_template("index.html", prediction_text=f"Flood Risk Prediction: {output}")

if __name__ == "__main__":
    app.run(debug=True)
