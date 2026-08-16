{{ config(materialized='table') }}

SELECT
    r.result_id,

    s.student_key,
    c.course_key,
    a.session_key,

    r.score,
    r.grade,
    r.grade_point,
    r.credit_units,

    CASE
        WHEN r.score >= 40 THEN TRUE
        ELSE FALSE
    END AS is_passed,

    CURRENT_TIMESTAMP AS created_at

FROM {{ ref('stg_results') }} r

JOIN {{ ref('dim_student') }} s
    ON r.student_id = s.student_id
    AND s.is_current = TRUE

JOIN {{ ref('dim_course') }} c
    ON r.course_id = c.course_id
    AND c.is_current = TRUE

JOIN {{ ref('dim_academic_session') }} a
    ON r.session_id = a.session_id