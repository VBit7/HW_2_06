-- Студент із найвищим середнім балом з певного предмета

SELECT	FirstName || ' ' || LastName AS 'Student''s name',
		s2.SubjectName AS 'Subject',		
		ROUND(AVG(Score), 2) AS 'MAX AVG Score'
FROM Students s 
	LEFT JOIN Grades g ON s.StudentId = g.StudentId
	LEFT JOIN Subjects s2 ON g.SubjectId = s2.SubjectId 
WHERE s2.SubjectId = 1
GROUP BY SubjectName, FirstName, LastName
ORDER BY AVG(Score) DESC 
LIMIT 1;
