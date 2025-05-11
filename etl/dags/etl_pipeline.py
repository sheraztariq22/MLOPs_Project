from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    df = pd.read_csv("data/raw/diabetes.csv")
    df.to_csv("data/processed/loaded.csv", index=False)

def preprocess_data():
    df = pd.read_csv("data/processed/loaded.csv")
    df = df.dropna()  # Basic cleaning
    df.to_csv("data/processed/cleaned.csv", index=False)

def split_data():
    df = pd.read_csv("data/processed/cleaned.csv")
    train, test = train_test_split(df, test_size=0.2)
    train.to_csv("data/processed/train.csv", index=False)
    test.to_csv("data/processed/test.csv", index=False)

with DAG("etl_pipeline", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="load", python_callable=load_data)
    t2 = PythonOperator(task_id="clean", python_callable=preprocess_data)
    t3 = PythonOperator(task_id="split", python_callable=split_data)

    t1 >> t2 >> t3
