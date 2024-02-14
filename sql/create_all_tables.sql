-- Table: Group
CREATE TABLE IF NOT EXISTS Groups (
            GroupId 	INT PRIMARY KEY,
            GroupName	VARCHAR(50)
        );

-- Table: Student
CREATE TABLE IF NOT EXISTS Students (
            StudentId	INT PRIMARY KEY,
            FirstName 	VARCHAR(30),
            SecondName	VARCHAR(30),
            GroupId		INT,
            CONSTRAINT FK_GroupId FOREIGN KEY (GroupId) REFERENCES Groups (GroupId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );

-- Table: Teacher
CREATE TABLE IF NOT EXISTS Teachers (
            TeacherId 	INT PRIMARY KEY,
            FirstName 	VARCHAR(30),
            SecondName	VARCHAR(30)
        );

-- Table: Subject
CREATE TABLE IF NOT EXISTS Subjects (
            SubjectId	INT PRIMARY KEY,
            SubjectName VARCHAR(50),
            TeacherId	INT,
            CONSTRAINT FK_TeacherId FOREIGN KEY (TeacherId) REFERENCES Teachers (TeacherId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );

-- Table: Grade
CREATE TABLE IF NOT EXISTS Grades (
            GradeId		INT PRIMARY KEY,
			StudentId	INT,
            SubjectId	INT,
            Score		INT,
            ScoreDate	DATE,
            CONSTRAINT FK_StudentId FOREIGN KEY (StudentId) REFERENCES Students (StudentId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE,
            CONSTRAINT SubjectId FOREIGN KEY (SubjectId) REFERENCES Subject (SubjectId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );
