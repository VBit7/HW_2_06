-- Середній бал на потоці (по всій таблиці оцінок)

SELECT ROUND(AVG(Score), 2) AS 'AVG Score'
FROM Grades g 
