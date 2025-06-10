/*
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the column of unique values of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).


If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

The result format is in the following example.



Example 1:

Input:
Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+
Output:
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
Explanation:
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.
*/

WITH Delivery AS (
    SELECT 1 AS delivery_id, 1 AS customer_id, '2019-08-01' AS order_date, '2019-08-02' AS customer_pref_delivery_date UNION ALL
    SELECT 2 AS delivery_id, 2 AS customer_id, '2019-08-02' AS order_date, '2019-08-02' AS customer_pref_delivery_date UNION ALL
    SELECT 3 AS delivery_id, 1 AS customer_id, '2019-08-11' AS order_date, '2019-08-12' AS customer_pref_delivery_date UNION ALL
    SELECT 4 AS delivery_id, 3 AS customer_id, '2019-08-24' AS order_date, '2019-08-24' AS customer_pref_delivery_date UNION ALL
    SELECT 5 AS delivery_id, 3 AS customer_id, '2019-08-21' AS order_date, '2019-08-22' AS customer_pref_delivery_date UNION ALL
    SELECT 6 AS delivery_id, 2 AS customer_id, '2019-08-11' AS order_date, '2019-08-13' AS customer_pref_delivery_date UNION ALL
    SELECT 7 AS delivery_id, 4 AS customer_id, '2019-08-09' AS order_date, '2019-08-09' AS customer_pref_delivery_date
)

SELECT
    round(avg(IF(order_date = customer_pref_delivery_date, 1, 0))*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
  SELECT (customer_id, min(order_date))
  from Delivery
  group by customer_id
);