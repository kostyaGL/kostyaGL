/*
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.


Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.



Example 1:

Input:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation:
Note that if the number of students is odd, there is no need to change the last one's seat.
*/

WITH Seat AS (
    SELECT 1 AS id, 'Abbot' AS student
    UNION ALL
    SELECT 2, 'Doris'
    UNION ALL
    SELECT 3, 'Emerson'
    UNION ALL
    SELECT 4, 'Green'
    UNION ALL
    SELECT 5, 'Jeames'
)
SELECT
    ROW_NUMBER() OVER(order by IF(MOD(id, 2) = 0, id-1, id+1) ) as id,
    student
FROM
    Seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)
