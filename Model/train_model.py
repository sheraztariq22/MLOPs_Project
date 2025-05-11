import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes
# Enable autologging
mlflow.sklearn.autolog()

def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=100, max_depth=4)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        mlflow.log_metric("mse_manual", mse)  # example of manual metric

if __name__ == "__main__":
    mlflow.set_tracking_uri("file:///home/sheraz/MLOps Project/mlruns")
    main()
