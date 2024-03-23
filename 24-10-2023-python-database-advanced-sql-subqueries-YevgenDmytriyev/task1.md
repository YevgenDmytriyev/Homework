## Task 1
<pre>subqueries_db=# \i /home/dci-student/24-10-2023-python-database-advanced-sql-subqueries-Lightmaker777/src/data/task1.sql 
CREATE TABLE
CREATE TYPE
CREATE TABLE
INSERT 0 105
INSERT 0 303</pre>
<pre>
subqueries_db=# \x
Expanded display is on.
subqueries_db=# SELECT id, name
FROM item
WHERE item.id NOT IN (
  SELECT item_id
  FROM stock
  WHERE quantity > 0
)
ORDER BY name;
-[ RECORD 1 ]----------------
id   | 33
name | Cheap T-shirt
-[ RECORD 2 ]----------------
id   | 103
name | Cheap T-shirt
-[ RECORD 3 ]----------------
id   | 105
name | Refurbished Smartphone
-[ RECORD 4 ]----------------
id   | 93
name | Refurbished T-shirt
</pre>

