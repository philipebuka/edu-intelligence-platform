import random
from datetime import date, timedelta
from pathlib import Path
import pandas as pd

#reproducible data generation
random.seed(42)

OUTPUT_DIR = Path("/opt/airflow/data/sample")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_STUDENTS = 2000

# --------------------------
# Generate faculties

faculties = [
    {"faculty_id":1,"faculty_code":"SCI","faculty_name":"Faculty of Science"},
    {"faculty_id":2,"faculty_code":"ENG","faculty_name":"Faculty of Engineering"},
    {"faculty_id":3,"faculty_code":"BUS","faculty_name":"Faculty of Business"},
    #{"faculty_id":4,"faculty_code":"ART","faculty_name":"Faculty of Social Sciences"}
    ]

faculties_df = pd.DataFrame(faculties)

#------------------------------
# Generate departments

departments = [
    {"department_id":1,"department_code":"CS","department_name":"Computer Science","faculty_id":1},
    {"department_id":2,"department_code":"MTH","department_name":"Mathematics","faculty_id":1},
    {"department_id":3,"department_code":"STA","department_name":"Statistics","faculty_id":1},
    {"department_id":4,"department_code":"CPE","department_name":"Computer Engineering","faculty_id":2},
    {"department_id":5,"department_code":"ELE","department_name":"Electrical Engineering","faculty_id":2},
    {"department_id":6,"department_code":"MEE","department_name":"Mechanical Engineering","faculty_id":2},
    {"department_id":7,"department_code":"ACC","department_name":"Accounting","faculty_id":3},
    {"department_id":8,"department_code":"BUS","department_name":"Business Administration","faculty_id":3},
    {"department_id":9,"department_code":"ECO","department_name":"Economics","faculty_id":3}
    ]

departments_df = pd.DataFrame(departments)

# -------------------------
# Courses
# -------------------------
courses = [

    # ============================================================
    # FACULTY OF SCIENCE
    # ============================================================

    # Department of Computer Science - department_id: 1
    {"course_id": 1, "course_code": "CSC101","course_name": "Introduction to Computer Science","credit_units": 3,"department_id": 1},
    {"course_id": 2,"course_code": "CSC201","course_name": "Data Structures and Algorithms","credit_units": 3,"department_id": 1},
    {"course_id": 3,"course_code": "CSC301","course_name": "Database Management Systems","credit_units": 3,"department_id": 1},
    {"course_id": 4,"course_code": "CSC401","course_name": "Software Engineering","credit_units": 3,"department_id": 1},
    {"course_id": 5,"course_code": "CSC501","course_name": "Artificial Intelligence","credit_units": 3,"department_id": 1},

    # Department of Mathematics - department_id: 2
    {"course_id": 6,"course_code": "MTH101","course_name": "Calculus I","credit_units": 3,"department_id": 2},
    {"course_id": 7,"course_code": "MTH201","course_name": "Linear Algebra","credit_units": 3,"department_id": 2},
    {"course_id": 8,"course_code": "MTH301","course_name": "Differential Equations","credit_units": 3,"department_id": 2},
    {"course_id": 9,"course_code": "MTH401","course_name": "Numerical Analysis","credit_units": 3,"department_id": 2},
    {"course_id": 10,"course_code": "MTH501","course_name": "Advanced Mathematical Methods","credit_units": 3,"department_id": 2},

    # Department of Statistics - department_id: 3
    {"course_id": 11,"course_code": "STA101","course_name": "Introduction to Statistics","credit_units": 3,"department_id": 3},
    {"course_id": 12,"course_code": "STA201","course_name": "Probability Theory","credit_units": 3,"department_id": 3},
    {"course_id": 13,"course_code": "STA301","course_name": "Statistical Inference","credit_units": 3,"department_id": 3},
    {"course_id": 14,"course_code": "STA401","course_name": "Regression Analysis","credit_units": 3,"department_id": 3},
    {"course_id": 15,"course_code": "STA501","course_name": "Applied Multivariate Statistics","credit_units": 3,"department_id": 3},

    # ============================================================
    # FACULTY OF ENGINEERING
    # ============================================================

    # Department of Computer Engineering - department_id: 4
    {"course_id": 16,"course_code": "CPE101","course_name": "Introduction to Computer Engineering","credit_units": 3,"department_id": 4},
    {"course_id": 17,"course_code": "CPE201","course_name": "Digital Logic Design","credit_units": 3,"department_id": 4},
    {"course_id": 18,"course_code": "CPE301","course_name": "Microprocessor Systems","credit_units": 3,"department_id": 4},
    {"course_id": 19,"course_code": "CPE401","course_name": "Computer Architecture","credit_units": 3,"department_id": 4},
    {"course_id": 20,"course_code": "CPE501","course_name": "Embedded Systems Design","credit_units": 3,"department_id": 4},

    # Department of Electrical/Electronics Engineering - department_id: 5
    {"course_id": 21,"course_code": "EEE101","course_name": "Basic Electrical Engineering","credit_units": 3,"department_id": 5},
    {"course_id": 22,"course_code": "EEE201","course_name": "Circuit Theory","credit_units": 3,"department_id": 5},
    {"course_id": 23,"course_code": "EEE301","course_name": "Electronic Devices and Circuits","credit_units": 3,"department_id": 5},
    {"course_id": 24,"course_code": "EEE401","course_name": "Power Systems Engineering","credit_units": 3,"department_id": 5},
    {"course_id": 25,"course_code": "EEE501","course_name": "Control Systems Engineering","credit_units": 3,"department_id": 5},

    # Department of Mechanical Engineering - department_id: 6
    {"course_id": 26,"course_code": "MEE101","course_name": "Introduction to Mechanical Engineering","credit_units": 3,"department_id": 6},
    {"course_id": 27,"course_code": "MEE201","course_name": "Engineering Mechanics","credit_units": 3,"department_id": 6},
    {"course_id": 28,"course_code": "MEE301","course_name": "Thermodynamics","credit_units": 3,"department_id": 6},
    {"course_id": 29,"course_code": "MEE401","course_name": "Fluid Mechanics","credit_units": 3,"department_id": 6},
    {"course_id": 30,"course_code": "MEE501","course_name": "Advanced Machine Design","credit_units": 3,"department_id": 6},

    # ============================================================
    # FACULTY OF BUSINESS
    # ============================================================

    # Department of Accounting - department_id: 7
    {"course_id": 31,"course_code": "ACC101","course_name": "Introduction to Accounting","credit_units": 3,"department_id": 7},
    {"course_id": 32,"course_code": "ACC201","course_name": "Financial Accounting","credit_units": 3,"department_id": 7},
    {"course_id": 33,"course_code": "ACC301","course_name": "Management Accounting","credit_units": 3,"department_id": 7},
    {"course_id": 34,"course_code": "ACC401","course_name": "Auditing and Assurance","credit_units": 3,"department_id": 7},
    {"course_id": 35,"course_code": "ACC501","course_name": "Advanced Financial Reporting","credit_units": 3,"department_id": 7},

    # Department of Business Administration - department_id: 8
    {"course_id": 36,"course_code": "BUS101","course_name": "Introduction to Business","credit_units": 3,"department_id": 8},
    {"course_id": 37,"course_code": "BUS201","course_name": "Principles of Management","credit_units": 3,"department_id": 8},
    {"course_id": 38,"course_code": "BUS301","course_name": "Organizational Behaviour","credit_units": 3,"department_id": 8},
    {"course_id": 39,"course_code": "BUS401","course_name": "Strategic Management","credit_units": 3,"department_id": 8},
    {"course_id": 40,"course_code": "BUS501","course_name": "Business Policy and Strategy","credit_units": 3,"department_id": 8},

    # Department of Economics - department_id: 9
    {"course_id": 41,"course_code": "ECO101","course_name": "Principles of Economics","credit_units": 3,"department_id": 9},
    {"course_id": 42,"course_code": "ECO201","course_name": "Microeconomic Theory","credit_units": 3,"department_id": 9},
    {"course_id": 43,"course_code": "ECO301","course_name": "Macroeconomic Theory","credit_units": 3,"department_id": 9},
    {"course_id": 44,"course_code": "ECO401","course_name": "Econometrics","credit_units": 3,"department_id": 9},
    {"course_id": 45,"course_code": "ECO501","course_name": "Advanced Economic Analysis","credit_units": 3,"department_id": 9},

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
    "Samuel", "Chioma", "Michael", "Joy", "Victor", 
    "Blessing", "Uche", "Ijeoma", "Chukwuemeka", "Nkechi",
    "Raymond", "Patience", "Obinna", "Chisom", "Kelechi",
    "Ifeoma", "Chijioke", "Ogechi", "Chukwudi", "Nnamdi",
    "Chinonso", "Ugochukwu", "Chibuzo", "Ngozika", "Chukwuma",
    "Chinwe", "Chukwuebuka", "Chidimma","tobi", "Tosin", "Bola", "Femi", "Sade", "Kemi", "Yemi",
    "Tunde", "Ayo", "Bamidele", "Segun", "Funke", "Titi", "Dayo", "Lola", "Seyi", "Bisi",
    "Abdul", "Aisha", "Hassan", "Fatima", "Ibrahim", "Zainab", "Musa", "Maryam", "Usman", "Aminu",
    "Aisha", "Hauwa", "Abubakar", "Rashida", "Sadiq", "Aminat", "Bashir", "Khadijah",
    "Umo", "Ekaette", "Iniobong", "Bassey", "Nkoyo", "Edidiong", "Uduak", "Ekemini", "Asuquo", "Inyang"
]

last_names = [
    "Okafor", "Eze", "Nwosu", "Obi", "Adebayo",
    "Okeke", "Ibrahim", "Uche", "Olawale", "Adeyemi","Eze", 
    "Chukwu", "Ogunleye", "Afolabi", "Balogun", "Ogunbiyi", 
    "Akinwale", "Oluwaseun", "Adebisi", "Oluwafemi","Ezenwa","Nwachukwu", "Oluwatosin", "Akinyemi", "Oluwadamilola",
    "Iloelunachi","Faiza","labake","Oluwadamilola","Adebimpe","Oluwaseyi","Adebukola","Oluwatobiloba","Adewale","Oluwafunmilayo"
    "Mmesoma","Ali","Adams","Johnson","Smith","Williams","Brown","Jones","Miller","Fernandez","Garcia","Martinez","Rodriguez","Hernandez","Lopez","Gonzalez","Wilson",
    "Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker",
    "Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera"
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

# # -------------------------
# # Results
# # -------------------------
# results = []

# for student_id in students_df["student_id"]:
#     student_department = students_df.loc[
#         students_df["student_id"] == student_id,
#         "department_id"
#     ].iloc[0]

#     # Get courses belonging to the student's department
#     department_courses = courses_df[
#         courses_df["department_id"] == student_department
#     ]

#     for session_id in academic_sessions_df["session_id"]:
#         # Student takes all courses offered by their department
#         for _, course in department_courses.iterrows():

#             score = random.randint(35, 95)

#             if score >= 70:
#                 grade = "A"
#                 grade_point = 5.0
#             elif score >= 60:
#                 grade = "B"
#                 grade_point = 4.0
#             elif score >= 50:
#                 grade = "C"
#                 grade_point = 3.0
#             elif score >= 45:
#                 grade = "D"
#                 grade_point = 2.0
#             elif score >= 40:
#                 grade = "E"
#                 grade_point = 1.0
#             else:
#                 grade = "F"
#                 grade_point = 0.0

#             results.append({
#                 "result_id": len(results) + 1,
#                 "student_id": student_id,
#                 "course_id": course["course_id"],
#                 "session_id": session_id,
#                 "score": score,
#                 "grade": grade,
#                 "grade_point": grade_point,
#                 "credit_units": course["credit_units"]
#             })

# results_df = pd.DataFrame(results)

# -------------------------
# Results
# -------------------------

results = []

# Target distribution
TARGET_MEAN = 54
TARGET_STD = 18
FAILURE_RATE = 0.12
PASS_MARK = 40

# Total number of result records
total_results = (
    len(students_df)
    * len(academic_sessions_df)
    * len(courses_df)
)

# Approximately 12% of records should be failures
num_failures = round(total_results * FAILURE_RATE)

# Create a list of result positions that will be failures
failure_indices = set(
    random.sample(
        range(total_results),
        num_failures
    )
)

score_index = 0

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

            # -----------------------------------
            # Generate score
            # -----------------------------------

            if score_index in failure_indices:

                # Generate a realistic failing score
                # between 0 and 39
                score = random.gauss(30, 6)

                # Keep within valid failure range
                score = max(0, min(39, score))

            else:

                # Generate score around mean 54
                # with standard deviation of 18
                score = random.gauss(
                    TARGET_MEAN,
                    TARGET_STD
                )

                # Keep score within valid range
                score = max(40, min(100, score))

            # Round to 2 decimal places
            score = round(score, 2)

            # -----------------------------------
            # Grade assignment
            # -----------------------------------

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

            score_index += 1


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