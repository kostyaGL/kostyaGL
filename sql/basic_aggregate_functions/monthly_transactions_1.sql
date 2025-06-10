/*
Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].


Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
*/

WITH Transactions AS (
    SELECT 121 AS id, 'US' AS country, 'approved' AS state, 1000 AS amount, '2018-12-18' AS trans_date UNION ALL
    SELECT 122 AS id, 'US' AS country, 'declined' AS state, 2000 AS amount, '2018-12-19' AS trans_date UNION ALL
    SELECT 123 AS id, 'US' AS country, 'approved' AS state, 2000 AS amount, '2019-01-01' AS trans_date UNION ALL
    SELECT 124 AS id, 'DE' AS country, 'approved' AS state, 2000 AS amount, '2019-01-07' AS trans_date
)
SELECT
 DATE_TRUNC(PARSE_DATE('%Y-%m-%d', trans_date), MONTH),
 country,
 COUNT(*) trans_count,
 SUM(if(state='approved', 1, 0)) approved_count,
 SUM(amount) trans_total_amount,
 SUM(if(state='approved', amount, 0)) approved_total_amount,
FROM
 Transactions
GROUP BY DATE_TRUNC(PARSE_DATE('%Y-%m-%d', trans_date), MONTH), country
