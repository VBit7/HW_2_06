-- 5 студентів із найбільшим середнім балом з усіх предметів

SELECT FirstName || ' ' || LastName AS 'Student''s name', ROUND(AvgScore, 2) AS 'Average score'
FROM Students s
	LEFT JOIN (
		SELECT StudentId, AVG(Score) AS AvgScore
		FROM Grades g
		GROUP BY StudentId) a ON s.StudentId = a.StudentId
ORDER BY AvgScore DESC
LIMIT 5;
