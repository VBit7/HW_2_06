-- Середній бал, який певний викладач ставить певному студентові

SELECT
		t.FirstName || ' ' || t.LastName AS 'Teacher''s Name',
		ROUND(AVG(Score), 2) AS 'AVG Score',
		s.FirstName || ' ' || s.LastName AS 'Student''s Name'
FROM Students s 
	JOIN Grades g ON s.StudentId = g.StudentId 
	JOIN Subjects s2 ON g.SubjectId = s2.SubjectId 
	JOIN Teachers t ON s2.TeacherId = t.TeacherId 
WHERE s.StudentId = 1 
	AND t.TeacherId = 1
GROUP BY t.FirstName, t.LastName, s.FirstName, s.LastName  
ORDER BY AVG(Score)
