	SELECT AVER.Average,AVER.StudentID,AVER.StudentName
    FROM
    (
		SELECT AVG(Grade.Grade) AS Average,Student.StudentName,Student.StudentID
		FROM Student
		JOIN Grade
		ON Student.StudentName=Grade.StudentName
		GROUP BY Student.StudentID
	) AS AVER

   
   
    
    
