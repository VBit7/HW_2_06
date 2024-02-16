-- Оцінки студентів у окремій групі з певного предмета
-- (обмежено вивід до 10 студентів для наглядності)

SELECT
		s.FirstName || ' ' || s.LastName AS 'Student''s Name',
		g.GroupName AS 'Group',
		s2.SubjectName AS 'Subject',
		g2.Score AS 'Score',
		ScoreDate AS 'Date of Score'
FROM Groups g
	JOIN Students s ON g.GroupId = s.GroupId 
	JOIN Grades g2 ON s.StudentId = g2.StudentId 
	JOIN Subjects s2 ON g2.SubjectId = s2.SubjectId 
WHERE g.GroupId = 1
	AND s2.SubjectId =1
LIMIT 10;
