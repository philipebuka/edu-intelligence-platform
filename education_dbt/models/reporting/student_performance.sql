{{ config(materialized='table') }}

SELECT
    s.student_key,
    s.student_number,
    s.first_name,
    s.last_name,
    s.gender,
    s.programme,
    s.level,
    d.department_name,
    f.faculty_name,

    a.academic_year,
    a.semester,

    COUNT(DISTINCT r.course_key) AS courses_taken,
    ROUND(AVG(r.score::numeric), 2) AS average_score,
    ROUND(AVG(r.grade_point::numeric), 2) AS average_grade_point,
    SUM(r.credit_units) AS total_credit_units,
    SUM(CASE WHEN r.is_passed THEN 1 ELSE 0 END) AS courses_passed,
    SUM(CASE WHEN NOT r.is_passed THEN 1 ELSE 0 END) AS courses_failed

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
    s.student_key,
    s.student_number,
    s.first_name,
    s.last_name,
    s.gender,
    s.programme,
    s.level,
    d.department_name,
    f.faculty_name,
    a.academic_year,
    a.semester