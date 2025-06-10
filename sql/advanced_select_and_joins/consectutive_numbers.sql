/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.


Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/
WITH Logs AS (
    SELECT 1 AS id, 1 AS num UNION ALL
    SELECT 2 AS id, 1 AS num UNION ALL
    SELECT 3 AS id, 1 AS num UNION ALL
    SELECT 4 AS id, 2 AS num UNION ALL
    SELECT 5 AS id, 1 AS num UNION ALL
    SELECT 6 AS id, 2 AS num UNION ALL
    SELECT 7 AS id, 2 AS num
)
SELECT
    log1.num ConsecutiveNums
FROM
    Logs log1
JOIN Logs log2 ON log1.id=log2.id+1
JOIN Logs log3 ON log1.id=log3.id+2
WHERE log1.num=log2.num AND log2.num=log3.num

