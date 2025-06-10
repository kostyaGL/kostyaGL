/*
Table: Queries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
This table may have duplicate rows.
This table contains information collected from some queries on a database.
The position column has a value from 1 to 500.
The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.


We define query quality as:

The average of the ratio between query rating and its position.

We also define poor query percentage as:

The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Queries table:
+------------+-------------------+----------+--------+
| query_name | result            | position | rating |
+------------+-------------------+----------+--------+
| Dog        | Golden Retriever  | 1        | 5      |
| Dog        | German Shepherd   | 2        | 5      |
| Dog        | Mule              | 200      | 1      |
| Cat        | Shirazi           | 5        | 2      |
| Cat        | Siamese           | 3        | 3      |
| Cat        | Sphynx            | 7        | 4      |
+------------+-------------------+----------+--------+
Output:
+------------+---------+-----------------------+
| query_name | quality | poor_query_percentage |
+------------+---------+-----------------------+
| Dog        | 2.50    | 33.33                 |
| Cat        | 0.66    | 33.33                 |
+------------+---------+-----------------------+
Explanation:
Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33
*/

WITH Queries AS (
    SELECT 'Dog' AS query_name, 'Golden Retriever' AS result, 1 AS position, 5 AS rating UNION ALL
    SELECT 'Dog' AS query_name, 'German Shepherd' AS result, 2 AS position, 5 AS rating UNION ALL
    SELECT 'Dog' AS query_name, 'Mule' AS result, 200 AS position, 1 AS rating UNION ALL
    SELECT 'Cat' AS query_name, 'Shirazi' AS result, 5 AS position, 2 AS rating UNION ALL
    SELECT 'Cat' AS query_name, 'Siamese' AS result, 3 AS position, 3 AS rating UNION ALL
    SELECT 'Cat' AS query_name, 'Sphynx' AS result, 7 AS position, 4 AS rating
)
SELECT
 ROUND(SUM(rating / position) / COUNT(*), 2) quality,
 (COUNT(DISTINCT query_name) / COUNT(*)) * 100 poor_query_percentage
FROM
 Queries
GROUP BY query_name

