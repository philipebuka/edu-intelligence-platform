{{ config(materialized='table') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY session_id) AS session_key,
    session_id,
    academic_year,
    semester,
    start_date,
    end_date
FROM {{ ref('stg_academic_sessions') }}