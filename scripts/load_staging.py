import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()  # Load environment variables from .env file
# Database configuration
DB_USER = os.getenv("POSTGRES_USER", "edu_admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "education_dw")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

DATA_DIR = Path("data/sample")

tables = [
    "faculties",
    "departments",
    "students",
    "courses",
    "academic_sessions",
    "results",
]

for table in tables:
    file_path = DATA_DIR / f"{table}.csv"

    df = pd.read_csv(file_path)

    df.to_sql(
        table,
        engine,
        schema="staging",
        if_exists="replace",
        index=False,
    )

    print(f"Loaded {len(df):,} records into staging.{table}")

print("Staging load completed successfully.")