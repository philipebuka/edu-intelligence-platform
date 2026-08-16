SELECT
    session_id,
    academic_year,
    semester,
    start_date,
    end_date
FROM {{ source('education', 'academic_sessions') }}