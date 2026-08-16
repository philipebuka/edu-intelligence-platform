SELECT
    department_id,
    department_code,
    department_name,
    faculty_id
FROM {{ source('education', 'departments') }}