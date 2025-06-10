"""
Table: Users

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.


Table: Register

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.


Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The result format is in the following example.



Example 1:

Input:
Users table:
+---------+-----------+
| user_id | user_name |
+---------+-----------+
| 6       | Alice     |
| 2       | Bob       |
| 7       | Alex      |
+---------+-----------+
Register table:
+------------+---------+
| contest_id | user_id |
+------------+---------+
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 7       |
| 209        | 6       |
| 215        | 7       |
| 208        | 7       |
| 210        | 2       |
| 207        | 2       |
| 210        | 7       |
+------------+---------+
Output:
+------------+------------+
| contest_id | percentage |
+------------+------------+
| 208        | 100.0      |
| 209        | 100.0      |
| 210        | 100.0      |
| 215        | 66.67      |
| 207        | 33.33      |
+------------+------------+
Explanation:
All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%


WITH Users AS (
    SELECT 6 AS user_id, 'Alice' AS user_name UNION ALL
    SELECT 2 AS user_id, 'Bob' AS user_name UNION ALL
    SELECT 7 AS user_id, 'Alex' AS user_name
),
Register AS (
    SELECT 215 AS contest_id, 6 AS user_id UNION ALL
    SELECT 209 AS contest_id, 2 AS user_id UNION ALL
    SELECT 208 AS contest_id, 2 AS user_id UNION ALL
    SELECT 210 AS contest_id, 6 AS user_id UNION ALL
    SELECT 208 AS contest_id, 6 AS user_id UNION ALL
    SELECT 209 AS contest_id, 7 AS user_id UNION ALL
    SELECT 209 AS contest_id, 6 AS user_id UNION ALL
    SELECT 215 AS contest_id, 7 AS user_id UNION ALL
    SELECT 208 AS contest_id, 7 AS user_id UNION ALL
    SELECT 210 AS contest_id, 2 AS user_id UNION ALL
    SELECT 207 AS contest_id, 2 AS user_id UNION ALL
    SELECT 210 AS contest_id, 7 AS user_id
)
SELECT
    r.contest_id,
    round(count(distinct u.user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
FROM Users u
LEFT JOIN Register r ON u.user_id = r.user_id
GROUP BY r.contest_id

"""
import pandas as pd

# Define the Users and Register data
users_data = {
    'user_id': [6, 2, 7],
    'user_name': ['Alice', 'Bob', 'Alex']
}

register_data = {
    'contest_id': [215, 209, 208, 210, 208, 209, 209, 215, 208, 210, 207, 210],
    'user_id': [6, 2, 2, 6, 6, 7, 6, 7, 7, 2, 2, 7]
}

# Create pandas DataFrames from the data
users_df = pd.DataFrame(users_data)
register_df = pd.DataFrame(register_data)

# Perform the SQL-like query
result_df = (
    register_df.merge(users_df, on='user_id', how='left')
              .groupby('contest_id')
              .agg({'user_id': 'nunique'})
              .reset_index()
)

# Calculate the percentage
total_users = len(users_df)
result_df['percentage'] = (result_df['user_id'] / total_users) * 100
result_df['percentage'] = result_df['percentage'].round(2)

# Sort by contest_id in ascending order
result_df = result_df.sort_values(by='contest_id')

# Rename columns to match the output format
result_df = result_df.rename(columns={'contest_id': 'contest_id', 'percentage': 'percentage'})

# Display the result
print(result_df)
