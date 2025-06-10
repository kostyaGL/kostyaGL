/*
Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.


Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
*/

WITH Products AS (
    SELECT 1 AS product_id, 20 AS new_price, '2019-08-14' AS change_date UNION ALL
    SELECT 2 AS product_id, 50 AS new_price, '2019-08-14' AS change_date UNION ALL
    SELECT 1 AS product_id, 30 AS new_price, '2019-08-15' AS change_date UNION ALL
    SELECT 1 AS product_id, 35 AS new_price, '2019-08-16' AS change_date UNION ALL
    SELECT 2 AS product_id, 65 AS new_price, '2019-08-17' AS change_date UNION ALL
    SELECT 3 AS product_id, 20 AS new_price, '2019-08-18' AS change_date
)

SELECT
    p2.product_id,
    COALESCE(p1.new_price, 10) AS price
FROM (
SELECT
    DISTINCT product_id,
    FIRST_VALUE(new_price) OVER (PARTITION BY product_id ORDER BY PARSE_DATE('%Y-%m-%d', change_date) DESC) as new_price
FROM
    Products
WHERE PARSE_DATE('%Y-%m-%d', change_date) <= DATE('2019-08-16')
 ) p1

RIGHT JOIN (
SELECT
    DISTINCT product_id
FROM
    Products) p2 ON p2.product_id=p1.product_id
