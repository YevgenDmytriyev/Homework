## Task 4
<pre>mentors_db=# SELECT
  module.name AS topic,
  mentor.name AS mentor,
  student.name AS student
FROM module
FULL JOIN mentor ON module.teacher = mentor.id
FULL JOIN student ON mentor.id = student.mentor_id
WHERE mentor.city = &apos;Berlin&apos;
OR student.city = &apos;Berlin&apos;
ORDER BY module.name, student.name;
         topic          |      mentor      |      student       
------------------------+------------------+--------------------
 Advanced SQL           | Julius Maxim     | Alex Anjou
 Advanced SQL           | Julius Maxim     | Maria Highsmith
 Computer Basics        | Melinda O&apos;Connor | Christian Blanc
 Computer Basics        | Melinda O&apos;Connor | Itzi Elizabal
 Python Basics          | Patricia Boulard | Gudrun Schmidt
 Python Data Structures | Julia Vila       | Gerald Hutticher
 SQL                    | Fabienne Martin  | Irmgard Seekircher
(7 rows)
</pre>
