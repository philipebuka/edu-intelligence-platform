-- ============================================================
-- EDUCATION INTELLIGENCE PLATFORM
-- Warehouse Star Schema
-- ============================================================

-- ------------------------------------------------------------
-- Dimension: Faculty
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_faculty (
    faculty_key SERIAL PRIMARY KEY,
    faculty_id INTEGER NOT NULL,
    faculty_code VARCHAR(20) NOT NULL,
    faculty_name VARCHAR(150) NOT NULL,
    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expiry_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE
);


-- ------------------------------------------------------------
-- Dimension: Department
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_department (
    department_key SERIAL PRIMARY KEY,
    department_id INTEGER NOT NULL,
    department_code VARCHAR(20) NOT NULL,
    department_name VARCHAR(150) NOT NULL,

    faculty_key INTEGER NOT NULL,

    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expiry_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT fk_department_faculty
        FOREIGN KEY (faculty_key)
        REFERENCES warehouse.dim_faculty(faculty_key)
);


-- ------------------------------------------------------------
-- Dimension: Student
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_student (
    student_key SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    student_number VARCHAR(30) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    date_of_birth DATE,

    department_key INTEGER NOT NULL,

    programme VARCHAR(150),
    level INTEGER,
    admission_year INTEGER,

    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expiry_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT fk_student_department
        FOREIGN KEY (department_key)
        REFERENCES warehouse.dim_department(department_key)
);


-- ------------------------------------------------------------
-- Dimension: Course
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_course (
    course_key SERIAL PRIMARY KEY,
    course_id INTEGER NOT NULL,
    course_code VARCHAR(30) NOT NULL,
    course_name VARCHAR(200) NOT NULL,
    credit_units INTEGER NOT NULL,

    department_key INTEGER NOT NULL,

    effective_date DATE NOT NULL DEFAULT CURRENT_DATE,
    expiry_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT TRUE,

    CONSTRAINT fk_course_department
        FOREIGN KEY (department_key)
        REFERENCES warehouse.dim_department(department_key)
);


-- ------------------------------------------------------------
-- Dimension: Academic Session
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_academic_session (
    session_key SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);


-- ------------------------------------------------------------
-- Dimension: Assessment Type
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.dim_assessment_type (
    assessment_type_key SERIAL PRIMARY KEY,
    assessment_type_code VARCHAR(20) NOT NULL,
    assessment_type_name VARCHAR(100) NOT NULL
);


-- ------------------------------------------------------------
-- Fact: Student Result
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS warehouse.fact_student_result (
    result_key BIGSERIAL PRIMARY KEY,

    result_id INTEGER NOT NULL,

    student_key INTEGER NOT NULL,
    course_key INTEGER NOT NULL,
    session_key INTEGER NOT NULL,
    assessment_type_key INTEGER,

    score NUMERIC(5,2),
    grade VARCHAR(5),
    grade_point NUMERIC(3,2),
    credit_units INTEGER,

    is_passed BOOLEAN,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_result_student
        FOREIGN KEY (student_key)
        REFERENCES warehouse.dim_student(student_key),

    CONSTRAINT fk_result_course
        FOREIGN KEY (course_key)
        REFERENCES warehouse.dim_course(course_key),

    CONSTRAINT fk_result_session
        FOREIGN KEY (session_key)
        REFERENCES warehouse.dim_academic_session(session_key),

    CONSTRAINT fk_result_assessment
        FOREIGN KEY (assessment_type_key)
        REFERENCES warehouse.dim_assessment_type(assessment_type_key)
);


-- ============================================================
-- Indexes
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_department_faculty
    ON warehouse.dim_department(faculty_key);

CREATE INDEX IF NOT EXISTS idx_student_department
    ON warehouse.dim_student(department_key);

CREATE INDEX IF NOT EXISTS idx_course_department
    ON warehouse.dim_course(department_key);

CREATE INDEX IF NOT EXISTS idx_result_student
    ON warehouse.fact_student_result(student_key);

CREATE INDEX IF NOT EXISTS idx_result_course
    ON warehouse.fact_student_result(course_key);

CREATE INDEX IF NOT EXISTS idx_result_session
    ON warehouse.fact_student_result(session_key);