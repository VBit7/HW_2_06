-- Середній бал, який ставить певний викладач зі своїх предметів

SELECT
		t.FirstName || ' ' || t.LastName AS 'Teacher''s Name',
		s.SubjectName AS 'Subject',
		ROUND(AVG(Score), 2) AS 'AVG Score'
FROM Teachers t 
	JOIN Subjects s ON t.TeacherId = s.TeacherId
	JOIN Grades g ON s.SubjectId = g.SubjectId
WHERE t.TeacherId = 1
GROUP BY t.FirstName, t.LastName, s.SubjectName
ORDER BY s.SubjectName
