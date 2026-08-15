import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

query = """
SELECT *
FROM staging.results;
"""

df = pd.read_sql(query, engine)

errors = []

if df["result_id"].isnull().any():
    errors.append("result_id contains NULL values.")

if df["result_id"].duplicated().any():
    errors.append("result_id contains duplicates.")

if df["student_id"].isnull().any():
    errors.append("student_id contains NULL values.")

if not df["score"].between(0, 100).all():
    errors.append("score contains values outside 0-100.")

valid_grades = {"A", "B", "C", "D", "E", "F"}

if not df["grade"].isin(valid_grades).all():
    errors.append("grade contains invalid values.")

if (df["credit_units"] <= 0).any():
    errors.append("credit_units contains zero or negative values.")

if errors:
    print("DATA QUALITY CHECK FAILED")

    for error in errors:
        print(f"- {error}")

    raise SystemExit(1)

print("DATA QUALITY CHECK PASSED")
print(f"Records validated: {len(df):,}")