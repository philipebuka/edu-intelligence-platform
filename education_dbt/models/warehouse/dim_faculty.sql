{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY faculty_id) AS faculty_key,
    faculty_id,
    faculty_code,
    faculty_name,
    CURRENT_DATE AS effective_date,
    NULL::DATE AS expiry_date,
    TRUE AS is_current
FROM {{ ref('stg_faculties') }}