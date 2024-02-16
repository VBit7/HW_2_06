-- Курси, які читає певний викладач

SELECT
		t.FirstName || ' ' || t.LastName AS 'Teacher''s Name',
		s.SubjectName AS 'Subject'
FROM Teachers t 
	LEFT JOIN Subjects s ON t.TeacherId = s.TeacherId 
WHERE t.TeacherId = 1
