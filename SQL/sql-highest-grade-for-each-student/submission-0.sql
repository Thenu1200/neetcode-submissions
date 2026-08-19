-- Write your query below
WITH RankedGrades AS (
    SELECT 
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rn
    FROM exam_results
)
SELECT 
    student_id,
    exam_id,
    score
FROM RankedGrades
WHERE rn = 1;