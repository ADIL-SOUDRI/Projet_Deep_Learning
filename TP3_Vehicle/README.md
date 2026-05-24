# 🚗 TP3 — LSTM Vehicle Fuel Consumption Prediction

## 📌 Description

Ce projet consiste à développer un modèle de Deep Learning basé sur les réseaux LSTM pour prédire la consommation de carburant des véhicules à partir de leurs caractéristiques techniques.

Le projet inclut :
- Analyse exploratoire des données (EDA)
- Prétraitement et normalisation
- Modèle LSTM pour régression
- Évaluation des performances
- Visualisation des résultats
- Export du modèle en format TinyML

---

## 📂 Dataset

Dataset utilisé :
- FuelConsumption.csv

Variables principales :
- ENGINESIZE
- CYLINDERS
- CO2EMISSIONS
- FUELCONSUMPTION_COMB

Source :
Kaggle — Vehicle Fuel Consumption Dataset

---

## 🧠 Modèle utilisé

Architecture :
- LSTM (64 unités)
- LSTM (32 unités)
- Dense (32 ReLU)
- Dense (1)

Loss :
- MAE (Mean Absolute Error)

Optimizer :
- Adam

---

## 📊 Résultats

Le modèle est évalué avec :
- MAE
- MSE
- RMSE
- R² Score

Visualisations générées :
- Pairplot
- Heatmap
- Training history
- Predictions vs Real
- Residuals plot

---

## 📁 Structure du projet
TP3_Vehicle/
│
├── data/
├── figures/
├── models/
├── tinyml/
├── notebooks/
└── src/
---

## ⚙️ Installation

```bash
pip install -r requirements.txt
tebooks
jupyter notebook main1.ipynb
