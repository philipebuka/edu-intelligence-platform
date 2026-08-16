{{ config(materialized='table') }}

SELECT
    d.department_key,
    d.department_code,
    d.department_name,
    f.faculty_name,

    a.academic_year,
    a.semester,

    COUNT(DISTINCT r.student_key) AS students,
    COUNT(DISTINCT r.course_key) AS courses,

    COUNT(*) AS total_results,

    ROUND(AVG(r.score), 2) AS average_score,

    SUM(CASE WHEN r.is_passed THEN 1 ELSE 0 END) AS total_passed,
    SUM(CASE WHEN NOT r.is_passed THEN 1 ELSE 0 END) AS total_failed,

    ROUND(
        100.0 * SUM(CASE WHEN r.is_passed THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS pass_rate

FROM {{ ref('fact_student_result') }} r

JOIN {{ ref('dim_student') }} s
    ON r.student_key = s.student_key

JOIN {{ ref('dim_department') }} d
    ON s.department_key = d.department_key

JOIN {{ ref('dim_faculty') }} f
    ON d.faculty_key = f.faculty_key

JOIN {{ ref('dim_academic_session') }} a
    ON r.session_key = a.session_key

GROUP BY
    d.department_key,
    d.department_code,
    d.department_name,
    f.faculty_name,
    a.academic_year,
    a.semester