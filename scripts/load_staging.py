import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text


# Database configuration
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

DATA_DIR = Path("/opt/airflow/data/sample")

tables = [
    "faculties",
    "departments",
    "students",
    "courses",
    "academic_sessions",
    "results",
]

with engine.begin() as conn:

    for table in tables:
        file_path = DATA_DIR / f"{table}.csv"

        df = pd.read_csv(file_path)

        # Remove existing records while keeping the table
        conn.execute(
            text(f"TRUNCATE TABLE staging.{table}")
        )

        # Insert the new records
        df.to_sql(
            table,
            conn,
            schema="staging",
            if_exists="append",
            index=False,
        )

        print(
            f"Loaded {len(df):,} records into staging.{table}"
        )

print("Staging load completed successfully.")