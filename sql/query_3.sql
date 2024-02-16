-- Середній бал у групах з певного предмета

SELECT g.GroupName AS 'Group', s2.SubjectName AS 'Subject', ROUND(AVG(g2.Score), 2) AS 'Score'
FROM Groups g 
	LEFT JOIN Students s ON g.GroupId =s.GroupId 
	LEFT JOIN Grades g2 ON s.StudentId = g2.StudentId 
	LEFT JOIN Subjects s2 ON g2.SubjectId = s2.SubjectId 
WHERE s2.SubjectId = 1
GROUP BY g.GroupName, s2.SubjectName
