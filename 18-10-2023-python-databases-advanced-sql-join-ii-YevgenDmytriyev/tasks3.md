## Task 3
<pre>mentors_db=# SELECT
  module.name AS topic,
  mentor.name AS mentor,
  student.name AS student
FROM module
FULL JOIN mentor ON module.teacher = mentor.id
FULL JOIN student ON mentor.id = student.mentor_id
ORDER BY module.name, student.name;
         topic          |      mentor      |      student       
------------------------+------------------+--------------------
 Advanced SQL           | Julius Maxim     | Alex Anjou
 Advanced SQL           | Julius Maxim     | Maria Highsmith
 Computer Basics        | Melinda O&apos;Connor | Christian Blanc
 Computer Basics        | Melinda O&apos;Connor | Itzi Elizabal
 Database Basics        | Ahmed Ali        | 
 Django Admin           | Rose Dupond      | 
 Django Basics          | Laura Wild       | Dolores Perez
 Django ORM             |                  | 
 Frontend               | Laura Wild       | Dolores Perez
 Python Algorithms      | Peter Smith      | Aimaar Abdul
 Python Basics          | Patricia Boulard | Gudrun Schmidt
 Python Data Structures | Julia Vila       | Gerald Hutticher
 Python Data Structures | Julia Vila       | John Goldwin
 Python Web Frameworks  | Laura Wild       | Dolores Perez
 SQL                    | Fabienne Martin  | Irmgard Seekircher
                        |                  | Emilio Ramiro
                        |                  | Wayne Green
(17 rows)
</pre>

