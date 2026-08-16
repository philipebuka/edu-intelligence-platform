{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY d.department_id) AS department_key,
    d.department_id,
    d.department_code,
    d.department_name,
    f.faculty_key,
    CURRENT_DATE AS effective_date,
    NULL::DATE AS expiry_date,
    TRUE AS is_current
FROM {{ ref('stg_departments') }} d
JOIN {{ ref('dim_faculty') }} f
    ON d.faculty_id = f.faculty_id