{{ config(materialized='table') }}

SELECT
    a.academic_year,
    a.semester,

    COUNT(DISTINCT r.student_key) AS total_students,
    COUNT(DISTINCT c.course_key) AS total_courses,
    COUNT(DISTINCT d.department_key) AS total_departments,
    COUNT(DISTINCT f.faculty_key) AS total_faculties,

    COUNT(*) AS total_results,

    ROUND(AVG(r.score), 2) AS average_score,

    SUM(CASE WHEN r.is_passed THEN 1 ELSE 0 END) AS total_passed,
    SUM(CASE WHEN NOT r.is_passed THEN 1 ELSE 0 END) AS total_failed,

    ROUND(
        100.0 * SUM(CASE WHEN r.is_passed THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS overall_pass_rate

FROM {{ ref('fact_student_result') }} r

JOIN {{ ref('dim_student') }} s
    ON r.student_key = s.student_key

JOIN {{ ref('dim_course') }} c
    ON r.course_key = c.course_key

JOIN {{ ref('dim_department') }} d
    ON s.department_key = d.department_key

JOIN {{ ref('dim_faculty') }} f
    ON d.faculty_key = f.faculty_key

JOIN {{ ref('dim_academic_session') }} a
    ON r.session_key = a.session_key

GROUP BY
    a.academic_year,
    a.semester