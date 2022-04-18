Set @ID=
(Select ave1.ID
from
(
	select AVER.Average,AVER.StudentName,AVER.StudentID as ID
	FROM
	(
		SELECT AVG(Grade.Grade) AS Average,Student.StudentName,Student.StudentID,
		row_number()over(order by avg(Grade.Grade) asc) as r
		FROM Student
		JOIN Grade
		ON Student.StudentName=Grade.StudentName
		GROUP BY Student.StudentID
	) AS AVER
	WHERE r=1
)as ave1);

DELETE from Student where Student.StudentID=@ID;



