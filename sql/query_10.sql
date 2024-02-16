-- Список курсів, які певному студенту читає певний викладач

SELECT DISTINCT
		s.FirstName || ' ' || s.LastName AS 'Student''s Name',
		s2.SubjectName AS 'Subject',
		t.FirstName || ' ' || t.LastName AS 'Teacher''s Name'
FROM Students s 
	JOIN Grades g ON s.StudentId = g.StudentId 
	JOIN Subjects s2 ON g.SubjectId = s2.SubjectId 
	JOIN Teachers t ON s2.TeacherId = t.TeacherId 
WHERE s.StudentId = 1 
	AND t.TeacherId = 1
ORDER BY s2.SubjectName
