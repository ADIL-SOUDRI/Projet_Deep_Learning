import numpy as np
from sklearn.preprocessing import MinMaxScaler


# =========================
# SCALE DATA
# =========================
def scale_data(data):
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    return data_scaled, scaler


# =========================
# CREATE SEQUENCES
# =========================
def create_sequences(data, time_steps=10):

    X = []
    y = []

    for i in range(len(data) - time_steps):

        X.append(data[i:i+time_steps])

        # dernière colonne = target
        y.append(data[i+time_steps, -1])

    return np.array(X), np.array(y)
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler

# def scale_data(data):
#     scaler = MinMaxScaler()
#     data_scaled = scaler.fit_transform(data)
#     return data_scaled, scaler