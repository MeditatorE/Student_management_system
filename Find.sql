SELECT Grade.StudentID,Grade.StudentName,Grade.CourseName,Grade.Grade
From Grade,Student
Where Student.StudentID=Grade.StudentID