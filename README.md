# Flood Risk Prediction  

A Machine Learning and Flask based web application to predict the flood risk (Negative-0, Positive-1) from environmental parameters. 

# Project Structure  
FloodRiskPrediction/
├── app.py # Main Flask application
├── flood_risk_dataset_india.csv # Dataset used for training & testing
├── FloodRisk_EDA.ipynb # Exploratory Data Analysis notebook
│
├── templates/
│ └── index.html # Main HTML page for input form
│
├── static/
│ └── flood.jpg # Background image for UI
│
├── output_Screen.png # UI screenshot
├── output_FloodNegative.png # Prediction: No Flood
├── output_FloodPositive.png # Prediction: Flood
└── README.md # Project documentation

## Tech Stack:  

 **Python 3.x**  
- Flask (backend)  
- Pandas, NumPy (data preprocessing)  
- Scikit-learn (ML model)  
- HTML, CSS (frontend UI)  


## Installation & Setup:  

1. Clone the repository:  
   
   git clone https://github.com/Pruthvi-27/FloodRiskPrediction.git
   cd FloodRiskPrediction

2. Install dependencies:

   pip install flask pandas numpy scikit-learn

3. Run the application:

   python app.py

4. Open the app in your browser:

   http://127.0.0.1:5000/

   Inputs & Outputs

## Inputs:

Latitude
Longitude
Rainfall (mm)
Temperature
Humidity (%)
River Discharge
Water Level
Elevation
Land Cover
Soil Type
Population Density
Infrastructure
Historical Floods

## Outputs:

Flood Prediction (Positive Case):
 Flood Prediction: 1

Flood Prediction (Negative Case):
 Flood Prediction: 0

## Screenshots:

Uploaded:
 Web App UI
 Flood Prediction (Positive Case)
 Flood Prediction (Negative Case)

