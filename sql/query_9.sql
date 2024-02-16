-- Список курсів, які відвідує студент

SELECT DISTINCT 
		s.FirstName || ' ' || s.LastName AS 'Student''s Name',
		s2.SubjectName AS 'Subject'
FROM Students s 
	LEFT JOIN Grades g ON s.StudentId = g.StudentId 
	LEFT JOIN Subjects s2 ON g.SubjectId = s2.SubjectId 
WHERE s.StudentId = 1
ORDER BY s2.SubjectName
