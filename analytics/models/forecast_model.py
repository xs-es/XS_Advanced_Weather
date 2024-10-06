# forecast_model.py
import numpy as np
from sklearn.linear_model import LinearRegression

def train_forecast_model(X, y):
    """Train a forecasting model based on input features and target values."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_temperature(model, future_periods):
    """Predict temperature using the trained model for given periods."""
    predictions = model.predict(np.array(future_periods).reshape(-1, 1))
    return predictions

if __name__ == "__main__":
    # Sample data to demonstrate functionality
    X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
    y = np.array([20, 21, 19, 22, 23, 24]).reshape(-1, 1)

    model = train_forecast_model(X, y)
    future_periods = [7, 8, 9]
    predictions = predict_temperature(model, future_periods)
    print("Temperature predictions:", predictions)
