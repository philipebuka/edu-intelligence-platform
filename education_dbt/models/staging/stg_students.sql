SELECT
    student_id,
    student_number,
    first_name,
    last_name,
    gender,
    date_of_birth,
    department_id,
    programme,
    level,
    admission_year
FROM {{ source('education', 'students') }}