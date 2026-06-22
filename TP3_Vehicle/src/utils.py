from sklearn.metrics import mean_absolute_error

def evaluate_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    print("MAE:", mae)
    return mae