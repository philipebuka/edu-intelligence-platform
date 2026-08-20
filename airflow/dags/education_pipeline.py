from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="education_pipeline",
    description="Education intelligence data pipeline",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["education", "etl", "dbt"],
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python /opt/airflow/scripts/generate_data.py",
    )

    load_staging = BashOperator(
        task_id="load_staging",
        bash_command="python /opt/airflow/scripts/load_staging.py",
    )

    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="python /opt/airflow/scripts/validate_results.py",
    )

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command=(
            "dbt run "
            "--project-dir /opt/airflow/education_dbt "
            "--select staging"
        ),
    )

    dbt_warehouse = BashOperator(
        task_id="dbt_warehouse",
        bash_command=(
            "dbt run "
            "--project-dir /opt/airflow/education_dbt "
            "--select warehouse"
        ),
    )

    dbt_reporting = BashOperator(
        task_id="dbt_reporting",
        bash_command=(
            "dbt run "
            "--project-dir /opt/airflow/education_dbt "
            "--select reporting"
        ),
    )

    generate_data >> load_staging >> validate_data
    validate_data >> dbt_staging >> dbt_warehouse >> dbt_reporting