import random
from datetime import date, timedelta
from pathlib import Path
import pandas as pd

#reproducible data generation
random.seed(42)

OUTPUT_DIR = Path("/opt/airflow/data/sample")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_STUDENTS = 1000

# --------------------------
# Generate faculties

faculties = [
    {"faculty_id":1,"faculty_code":"SCI","faculty_name":"Faculty of Science"},
    {"faculty_id":2,"faculty_code":"ENG","faculty_name":"Faculty of Engineering"},
    {"faculty_id":3,"faculty_code":"BUS","faculty_name":"Faculty of Business"},
    {"faculty_id":4,"faculty_code":"ART","faculty_name":"Faculty of Social Sciences"}
    ]

faculties_df = pd.DataFrame(faculties)

#------------------------------
# Generate departments

departments = [
    {"department_id":1,"department_code":"CS","department_name":"Computer Science","faculty_id":1},
    {"department_id":2,"department_code":"MTH","department_name":"Mathematics","faculty_id":1},
    {"department_id":3,"department_code":"ACC","department_name":"Accounting","faculty_id":3},
    {"department_id":4,"department_code":"ECO","department_name":"Economics","faculty_id":3}
    ]

departments_df = pd.DataFrame(departments)

# -------------------------
# Courses
# -------------------------
courses = [
    {
        "course_id": 1,
        "course_code": "CSC101",
        "course_name": "Introduction to Computer Science",
        "credit_units": 3,
        "department_id": 1,
    },
    {
        "course_id": 2,
        "course_code": "CSC201",
        "course_name": "Data Structures",
        "credit_units": 3,
        "department_id": 1,
    },
    {
        "course_id": 3,
        "course_code": "CSC301",
        "course_name": "Database Systems",
        "credit_units": 3,
        "department_id": 1,
    },
    {
        "course_id": 4,
        "course_code": "MTH101",
        "course_name": "Calculus I",
        "credit_units": 3,
        "department_id": 2,
    },
    {
        "course_id": 5,
        "course_code": "MTH201",
        "course_name": "Statistics",
        "credit_units": 3,
        "department_id": 2,
    },
    {
        "course_id": 6,
        "course_code": "EEE101",
        "course_name": "Circuit Theory",
        "credit_units": 3,
        "department_id": 3,
    },
    {
        "course_id": 7,
        "course_code": "ACC101",
        "course_name": "Financial Accounting",
        "credit_units": 3,
        "department_id": 4,
    },
    {
        "course_id": 8,
        "course_code": "ECO101",
        "course_name": "Principles of Economics",
        "credit_units": 3,
        "department_id": 5,
    },
]

courses_df = pd.DataFrame(courses)

# -------------------------
# Academic Sessions
# -------------------------
academic_sessions = [
    {
        "session_id": 1,
        "academic_year": "2023/2024",
        "semester": "First",
        "start_date": "2023-10-01",
        "end_date": "2024-02-28",
    },
    {
        "session_id": 2,
        "academic_year": "2023/2024",
        "semester": "Second",
        "start_date": "2024-03-01",
        "end_date": "2024-07-31",
    },
    {
        "session_id": 3,
        "academic_year": "2024/2025",
        "semester": "First",
        "start_date": "2024-10-01",
        "end_date": "2025-02-28",
    },
    {
        "session_id": 4,
        "academic_year": "2024/2025",
        "semester": "Second",
        "start_date": "2025-03-01",
        "end_date": "2025-07-31",
    },
]

academic_sessions_df = pd.DataFrame(academic_sessions)

# -------------------------
# Students
# -------------------------
first_names = [
    "Chinedu", "Adaeze", "Emeka", "Ngozi", "Ifeanyi",
    "Amaka", "David", "Grace", "Daniel", "Esther",
    "Samuel", "Chioma", "Michael", "Joy", "Victor"
]

last_names = [
    "Okafor", "Eze", "Nwosu", "Obi", "Adebayo",
    "Okeke", "Ibrahim", "Uche", "Olawale", "Adeyemi"
]

students = []

for i in range(1, NUM_STUDENTS + 1):
    department_id = random.choice(departments_df["department_id"].tolist())

    students.append({
        "student_id": i,
        "student_number": f"STU{20230000 + i}",
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "gender": random.choice(["Male", "Female"]),
        "date_of_birth": date(
            random.randint(1998, 2006),
            random.randint(1, 12),
            random.randint(1, 28)
        ),
        "department_id": department_id,
        "programme": departments_df.loc[
            departments_df["department_id"] == department_id,
            "department_name"
        ].iloc[0],
        "level": random.choice([100, 200, 300, 400]),
        "admission_year": random.choice([2021, 2022, 2023, 2024])
    })

students_df = pd.DataFrame(students)

# -------------------------
# Results
# -------------------------
results = []

for student_id in students_df["student_id"]:
    student_department = students_df.loc[
        students_df["student_id"] == student_id,
        "department_id"
    ].iloc[0]

    # Get courses belonging to the student's department
    department_courses = courses_df[
        courses_df["department_id"] == student_department
    ]

    for session_id in academic_sessions_df["session_id"]:
        # Student takes all courses offered by their department
        for _, course in department_courses.iterrows():

            score = random.randint(35, 95)

            if score >= 70:
                grade = "A"
                grade_point = 5.0
            elif score >= 60:
                grade = "B"
                grade_point = 4.0
            elif score >= 50:
                grade = "C"
                grade_point = 3.0
            elif score >= 45:
                grade = "D"
                grade_point = 2.0
            elif score >= 40:
                grade = "E"
                grade_point = 1.0
            else:
                grade = "F"
                grade_point = 0.0

            results.append({
                "result_id": len(results) + 1,
                "student_id": student_id,
                "course_id": course["course_id"],
                "session_id": session_id,
                "score": score,
                "grade": grade,
                "grade_point": grade_point,
                "credit_units": course["credit_units"]
            })

results_df = pd.DataFrame(results)

# -------------------------
# Save datasets
# -------------------------
faculties_df.to_csv(OUTPUT_DIR / "faculties.csv", index=False)
departments_df.to_csv(OUTPUT_DIR / "departments.csv", index=False)
students_df.to_csv(OUTPUT_DIR / "students.csv", index=False)
courses_df.to_csv(OUTPUT_DIR / "courses.csv", index=False)
academic_sessions_df.to_csv(
    OUTPUT_DIR / "academic_sessions.csv",
    index=False
)
results_df.to_csv(OUTPUT_DIR / "results.csv", index=False)

print("Synthetic data generated successfully.")
print(f"Students: {len(students_df):,}")
print(f"Results: {len(results_df):,}")