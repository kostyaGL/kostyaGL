"""
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
"""

import pandas as pd

# Define the Transactions table data
data = {
    'id': [121, 122, 123, 124],
    'country': ['US', 'US', 'US', 'DE'],
    'state': ['approved', 'declined', 'approved', 'approved'],
    'amount': [1000, 2000, 2000, 2000],
    'trans_date': ['2018-12-18', '2018-12-19', '2019-01-01', '2019-01-07']
}

# Create a DataFrame
Transactions = pd.DataFrame(data)

# Convert trans_date to datetime
Transactions['trans_date'] = pd.to_datetime(Transactions['trans_date'])

# Extract month from trans_date
Transactions['month'] = Transactions['trans_date'].dt.strftime('%Y-%m')

# Create a function to calculate the aggregated values
def aggregate_transactions(group):
    return pd.Series({
        'trans_count': group['id'].count(),
        'approved_count': (group['state'] == 'approved').sum(),
        'trans_total_amount': group['amount'].sum(),
        'approved_total_amount': group[group['state'] == 'approved']['amount'].sum()
    })
# Transactions.groupby(['month', 'country']).agg(
#     {'id' : 'count'}
# )
# Group by month and country, then apply the aggregate function
result = Transactions.groupby(['month', 'country']).apply(aggregate_transactions).reset_index()

# Reorder columns to match the desired output
result = result[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]

# Print the result
print(result)
