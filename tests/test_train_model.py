def test_mlflow_runs():
    import os
    assert os.path.exists("mlruns"), "MLflow did not log correctly"
