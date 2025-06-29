"""
Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.


Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.


Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

The result format is in the following example.



Example 1:

Input:
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
Output:
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
Explanation:
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.
*/

WITH
-- Define the Visits table CTE
Visits AS (
  SELECT
    1 AS visit_id,
    23 AS customer_id
  UNION ALL
  SELECT
    2 AS visit_id,
    9 AS customer_id
  UNION ALL
  SELECT
    4 AS visit_id,
    30 AS customer_id
  UNION ALL
  SELECT
    5 AS visit_id,
    54 AS customer_id
  UNION ALL
  SELECT
    6 AS visit_id,
    96 AS customer_id
  UNION ALL
  SELECT
    7 AS visit_id,
    54 AS customer_id
  UNION ALL
  SELECT
    8 AS visit_id,
    54 AS customer_id
),

-- Define the Transactions table CTE
Transactions AS (
  SELECT
    2 AS transaction_id,
    5 AS visit_id,
    310 AS amount
  UNION ALL
  SELECT
    3 AS transaction_id,
    5 AS visit_id,
    300 AS amount
  UNION ALL
  SELECT
    9 AS transaction_id,
    5 AS visit_id,
    200 AS amount
  UNION ALL
  SELECT
    12 AS transaction_id,
    1 AS visit_id,
    910 AS amount
  UNION ALL
  SELECT
    13 AS transaction_id,
    2 AS visit_id,
    970 AS amount
)

SELECT
  v.customer_id,
  count(*) count_no_trans
FROM
  Visits v
LEFT JOIN
  Transactions t
ON
  v.visit_id = t.visit_id
WHERE
  t.amount is null
GROUP BY
  v.customer_id
"""

import pandas as pd

# Define the Visits and Transactions data
visits_data = {
    'visit_id': [1, 2, 4, 5, 6, 7, 8],
    'customer_id': [23, 9, 30, 54, 96, 54, 54]
}

transactions_data = {
    'transaction_id': [2, 3, 9, 12, 13],
    'visit_id': [5, 5, 5, 1, 2],
    'amount': [310, 300, 200, 910, 970]
}

# Convert data to pandas DataFrames
visits_df = pd.DataFrame(visits_data)
transactions_df = pd.DataFrame(transactions_data)

# Merge Visits and Transactions on visit_id using left join
merged_df = pd.merge(visits_df, transactions_df, on='visit_id', how='left')

# Filter rows where there is no transaction (amount is null)
no_transaction_df = merged_df[merged_df['amount'].isnull()]

# Count occurrences of no transactions per customer_id
result_df = no_transaction_df.groupby('customer_id').size().reset_index(name='count_no_trans')

# Display the result
print(result_df)
