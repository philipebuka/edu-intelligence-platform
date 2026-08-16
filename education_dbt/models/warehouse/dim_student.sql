{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY s.student_id) AS student_key,
    s.student_id,
    s.student_number,
    s.first_name,
    s.last_name,
    s.gender,
    s.date_of_birth,
    d.department_key,
    s.programme,
    s.level,
    s.admission_year,
    CURRENT_DATE AS effective_date,
    NULL::DATE AS expiry_date,
    TRUE AS is_current
FROM {{ ref('stg_students') }} s
JOIN {{ ref('dim_department') }} d
    ON s.department_id = d.department_id