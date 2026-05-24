def train_model(model, X_train, y_train):
    history = model.fit(
        X_train,
        y_train,
        epochs=50,
        validation_split=0.2,
        verbose=1
    )
    return history