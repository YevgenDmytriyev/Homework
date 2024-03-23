### Task 2
<pre>mentors_db=# SELECT
  student.name AS student,
  module.name AS topic,
  mentor.name AS mentor
FROM student
LEFT JOIN mentor ON student.mentor_id = mentor.id
LEFT JOIN module ON mentor.id = module.teacher
ORDER BY student.name, module.name;
      student       |         topic          |      mentor      
--------------------+------------------------+------------------
 Aimaar Abdul       | Python Algorithms      | Peter Smith
 Alex Anjou         | Advanced SQL           | Julius Maxim
 Christian Blanc    | Computer Basics        | Melinda O&apos;Connor
 Dolores Perez      | Django Basics          | Laura Wild
 Dolores Perez      | Frontend               | Laura Wild
 Dolores Perez      | Python Web Frameworks  | Laura Wild
 Emilio Ramiro      |                        | 
 Gerald Hutticher   | Python Data Structures | Julia Vila
 Gudrun Schmidt     | Python Basics          | Patricia Boulard
 Irmgard Seekircher | SQL                    | Fabienne Martin
 Itzi Elizabal      | Computer Basics        | Melinda O&apos;Connor
 John Goldwin       | Python Data Structures | Julia Vila
 Maria Highsmith    | Advanced SQL           | Julius Maxim
 Wayne Green        |                        | 
(14 rows)
</pre>

