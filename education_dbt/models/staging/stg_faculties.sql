SELECT
    faculty_id,
    faculty_code,
    faculty_name
FROM {{ source('education', 'faculties') }}