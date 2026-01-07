from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.ingest_bronze import ingest_to_bronze

default_args = {
    "owner": "Guylherme Lopes",
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="bronze_ingestion",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    ingest = PythonOperator(
        task_id="ingest_raw_data",
        python_callable=ingest_to_bronze
    )

    ingest
