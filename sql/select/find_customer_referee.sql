/*

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.


Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
*/

WITH players_cte AS (
  SELECT 1 AS id, 'Will' AS name, NULL AS referee_id UNION ALL
  SELECT 2, 'Jane', NULL UNION ALL
  SELECT 3, 'Alex', 2 UNION ALL
  SELECT 4, 'Bill', NULL UNION ALL
  SELECT 5, 'Zack', 1 UNION ALL
  SELECT 6, 'Mark', 2
)

SELECT
  name
FROM
  players_cte
WHERE
  COALESCE(referee_id, 1) !=2;
