{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY c.course_id) AS course_key,
    c.course_id,
    c.course_code,
    c.course_name,
    c.credit_units,
    d.department_key,
    CURRENT_DATE AS effective_date,
    NULL::DATE AS expiry_date,
    TRUE AS is_current
FROM {{ ref('stg_courses') }} c
JOIN {{ ref('dim_department') }} d
    ON c.department_id = d.department_id