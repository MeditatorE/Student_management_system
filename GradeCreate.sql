

CREATE TABLE Student
(
	StudentID char(20)PRIMARY KEY,
    StudentName char(20)
);

CREATE TABLE Grade
(
    StudentID char(20),
    StudentName char(20),
    CourseName char(20),
    Grade int
);