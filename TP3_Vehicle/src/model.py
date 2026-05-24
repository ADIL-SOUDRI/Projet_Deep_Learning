import tensorflow as tf
from tensorflow.keras import layers

def build_lstm_model(input_shape):
    model = tf.keras.Sequential([
        layers.Input(shape=input_shape),
        layers.LSTM(64, return_sequences=True),
        layers.LSTM(32),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(
        optimizer='adam',
        loss='mae',
        metrics=['mae']
    )

    return model