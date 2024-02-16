-- Оцінки студентів у певній групі з певного предмета на останньому занятті

SELECT
		s.FirstName || ' ' || s.LastName AS 'Student''s Name',
		g.GroupName AS 'Group',
		g2.Score AS 'Score',
		g2.ScoreDate AS 'Date of Score'
FROM Groups g 
	JOIN Students s ON g.GroupId = s.GroupId
	JOIN Grades g2 ON s.StudentId = g2.StudentId 
	JOIN Subjects s2 ON g2.SubjectId = s2.SubjectId 
WHERE g.GroupId = 1
	AND s2.SubjectId = 1
	AND g2.ScoreDate = (
		SELECT MAX(g3.ScoreDate)
		FROM Grades g3 JOIN Students s3 ON g3.StudentId = s3.StudentId
		WHERE g3.SubjectId = s2.SubjectId  
			AND s3.GroupId = g.GroupId 
	) 
