## Task 4
<pre>site_user_db=# SELECT name
FROM site_user
WHERE extract(YEAR FROM birthdate) &lt; 2000;
-[ RECORD 1 ]-------
name | Miriam Valira
-[ RECORD 2 ]-------
name | Louise Clark</pre>

<pre>site_user_db=# SELECT name
FROM site_user
WHERE siblings IS NOT NULL;
-[ RECORD 1 ]-------
name | Miriam Valira
-[ RECORD 2 ]-------
name | Johann Müller
-[ RECORD 3 ]-------
name | Louise Clark</pre>

<pre>site_user_db=# SELECT name
FROM site_user
WHERE site_settings-&gt;&gt;&apos;notifications&apos; = &apos;true&apos;;
-[ RECORD 1 ]-------
name | Johann Müller
-[ RECORD 2 ]-------
name | Louise Clark</pre>

<pre>site_user_db=# SELECT name
FROM site_user
WHERE array_length(availability, 1) &gt; 1;
-[ RECORD 1 ]-------
name | Johann Müller
-[ RECORD 2 ]-------
name | Louise Clark</pre>
