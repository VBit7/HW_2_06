-- Table: Group
CREATE TABLE IF NOT EXISTS Groups (
            GroupId 	INTEGER PRIMARY KEY AUTOINCREMENT,
            GroupName	VARCHAR(50)
        );

-- Table: Student
CREATE TABLE IF NOT EXISTS Students (
            StudentId	INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName 	VARCHAR(30),
            LastName	VARCHAR(30),
            GroupId		INTEGER,
            CONSTRAINT FK_GroupId FOREIGN KEY (GroupId) REFERENCES Groups (GroupId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );

-- Table: Teacher
CREATE TABLE IF NOT EXISTS Teachers (
            TeacherId 	INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName 	VARCHAR(30),
            LastName	VARCHAR(30)
        );

-- Table: Subject
CREATE TABLE IF NOT EXISTS Subjects (
            SubjectId	INTEGER PRIMARY KEY AUTOINCREMENT,
            SubjectName VARCHAR(50),
            TeacherId	INTEGER,
            CONSTRAINT FK_TeacherId FOREIGN KEY (TeacherId) REFERENCES Teachers (TeacherId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );

-- Table: Grade
CREATE TABLE IF NOT EXISTS Grades (
            GradeId		INTEGER PRIMARY KEY AUTOINCREMENT,
			StudentId	INTEGER,
            SubjectId	INTEGER,
            Score		INTEGER,
            ScoreDate	DATE,
            CONSTRAINT FK_StudentId FOREIGN KEY (StudentId) REFERENCES Students (StudentId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE,
            CONSTRAINT FK_SubjectId FOREIGN KEY (SubjectId) REFERENCES Subjects (SubjectId)
            	ON DELETE CASCADE
            	ON UPDATE CASCADE
        );
