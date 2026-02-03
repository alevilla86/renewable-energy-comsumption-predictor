import numpy as np
from sklearn.linear_model import LinearRegression


def train_model(X: np.ndarray, y: np.ndarray) -> LinearRegression:
    """Train a linear regression model on TIME -> Value."""
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    return model


def predict(model: LinearRegression, years: np.ndarray) -> np.ndarray:
    """Predict values for given years."""
    return model.predict(years.reshape(-1, 1))
