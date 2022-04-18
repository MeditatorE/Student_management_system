
		select AVER.Average,AVER.StudentName,AVER.StudentID
		FROM
        (
			SELECT AVG(Grade.Grade) AS Average,Student.StudentName,Student.StudentID,
            row_number()over(order by avg(Grade.Grade) desc) as r
			FROM Student
			JOIN Grade
			ON Student.StudentName=Grade.StudentName
			GROUP BY Student.StudentID
		) AS AVER
        WHERE r=1
    
    
    