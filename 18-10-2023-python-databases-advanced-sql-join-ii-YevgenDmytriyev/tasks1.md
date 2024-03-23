### Task 1
<pre>mentors_db=# SELECT
  student.name AS student,
  mentor.name AS mentor,
  local_mentor.name AS local_mentor
FROM student
LEFT JOIN mentor AS mentor ON student.mentor_id = mentor.id
LEFT JOIN mentor AS local_mentor ON student.local_mentor = local_mentor.id
ORDER BY student.name;
      student       |      mentor      |  local_mentor   
--------------------+------------------+-----------------
 Aimaar Abdul       | Peter Smith      | Laura Wild
 Alex Anjou         | Julius Maxim     | Fabienne Martin
 Christian Blanc    | Melinda O&apos;Connor | Fabienne Martin
 Dolores Perez      | Laura Wild       | Julia Vila
 Emilio Ramiro      |                  | Julia Vila
 Gerald Hutticher   | Julia Vila       | Julius Maxim
 Gudrun Schmidt     | Patricia Boulard | Julius Maxim
 Irmgard Seekircher | Fabienne Martin  | Julius Maxim
 Itzi Elizabal      | Melinda O&apos;Connor | Julia Vila
 John Goldwin       | Julia Vila       | Laura Wild
 Maria Highsmith    | Julius Maxim     | Peter Smith
 Wayne Green        |                  | Peter Smith
(12 rows)
</pre>

