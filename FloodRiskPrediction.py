# FloodGuard Week 2 - EDA

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\Flood risk prediction\FloodRiskPrediction\Flood_dataset.csv")
print("Shape of dataset:", df.shape)

# First few rows
print(df.head())

# Info and missing values
print(df.info())
print(df.isnull().sum())

# Statistics
print(df.describe())

# Rainfall distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Rainfall'], kde=True, bins=30, color="blue")
plt.title("Rainfall Distribution")
plt.show()

# Temperature distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Temperature'], kde=True, bins=30, color="orange")
plt.title("Temperature Distribution")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Flood occurrence count
plt.figure(figsize=(6,4))
sns.countplot(x=df['Flood'], palette="Set2")
plt.title("Flood Occurrence Distribution")
plt.show()

# Correlation with target
correlations = df.corr()['Flood'].sort_values(ascending=False)
print("Correlation of features with target:\n", correlations)
