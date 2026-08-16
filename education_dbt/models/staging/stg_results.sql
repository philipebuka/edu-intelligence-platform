SELECT
    result_id,
    student_id,
    course_id,
    session_id,
    score,
    grade,
    grade_point,
    credit_units
FROM {{ source('education', 'results') }}