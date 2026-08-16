SELECT
    course_id,
    course_code,
    course_name,
    credit_units,
    department_id
FROM {{ source('education', 'courses') }}