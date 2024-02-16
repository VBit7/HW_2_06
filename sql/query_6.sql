-- Список студентів у певній групі

SELECT 
		s.FirstName || ' ' || s.LastName AS 'Student''s Name',
		g.GroupName AS 'Group'
FROM Groups g
	LEFT JOIN Students s ON g.GroupId = s.GroupId 
WHERE g.GroupId = 1
