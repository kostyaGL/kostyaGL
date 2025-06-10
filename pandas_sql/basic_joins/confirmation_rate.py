"""
+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
+----------------+----------+
user_id is the column of unique values for this table.
Each row contains information about the signup time for the user with ID user_id.


Table: Confirmations

+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| user_id        | int      |
| time_stamp     | datetime |
| action         | ENUM     |
+----------------+----------+
(user_id, time_stamp) is the primary key (combination of columns with unique values) for this table.
user_id is a foreign key (reference column) to the Signups table.
action is an ENUM (category) of the type ('confirmed', 'timeout')
Each row of this table indicates that the user with ID user_id requested a confirmation message at time_stamp and that confirmation message was either confirmed ('confirmed') or expired without confirming ('timeout').


The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Signups table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
+---------+---------------------+
Confirmations table:
+---------+---------------------+-----------+
| user_id | time_stamp          | action    |
+---------+---------------------+-----------+
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
| 2       | 2021-02-28 23:59:59 | timeout   |
+---------+---------------------+-----------+
Output:
+---------+-------------------+
| user_id | confirmation_rate |
+---------+-------------------+
| 6       | 0.00              |
| 3       | 0.00              |
| 7       | 1.00              |
| 2       | 0.50              |
+---------+-------------------+
Explanation:
User 6 did not request any confirmation messages. The confirmation rate is 0.
User 3 made 2 requests and both timed out. The confirmation rate is 0.
User 7 made 3 requests and all were confirmed. The confirmation rate is 1.
User 2 made 2 requests where one was confirmed and the other timed out. The confirmation rate is 1 / 2 = 0.5.
*/

WITH Signups AS (
    SELECT 3 AS user_id, TIMESTAMP '2020-03-21 10:16:13' AS time_stamp UNION ALL
    SELECT 7 AS user_id, TIMESTAMP '2020-01-04 13:57:59' AS time_stamp UNION ALL
    SELECT 2 AS user_id, TIMESTAMP '2020-07-29 23:09:44' AS time_stamp UNION ALL
    SELECT 6 AS user_id, TIMESTAMP '2020-12-09 10:39:37' AS time_stamp
),
Confirmations AS (
    SELECT 3 AS user_id, TIMESTAMP '2021-01-06 03:30:46' AS time_stamp, 'timeout' AS action UNION ALL
    SELECT 3 AS user_id, TIMESTAMP '2021-07-14 14:00:00' AS time_stamp, 'timeout' AS action UNION ALL
    SELECT 7 AS user_id, TIMESTAMP '2021-06-12 11:57:29' AS time_stamp, 'confirmed' AS action UNION ALL
    SELECT 7 AS user_id, TIMESTAMP '2021-06-13 12:58:28' AS time_stamp, 'confirmed' AS action UNION ALL
    SELECT 7 AS user_id, TIMESTAMP '2021-06-14 13:59:27' AS time_stamp, 'confirmed' AS action UNION ALL
    SELECT 2 AS user_id, TIMESTAMP '2021-01-22 00:00:00' AS time_stamp, 'confirmed' AS action UNION ALL
    SELECT 2 AS user_id, TIMESTAMP '2021-02-28 23:59:59' AS time_stamp, 'timeout' AS action
)

-- Example query to retrieve all data from both CTEs
# Write your MySQL query statement below
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;

"""
import pandas as pd
from io import StringIO

# Sample data for Signups and Confirmations tables as strings
signups_data = """user_id,time_stamp
3,2020-03-21 10:16:13
7,2020-01-04 13:57:59
2,2020-07-29 23:09:44
6,2020-12-09 10:39:37"""
confirmations_data = """user_id,time_stamp,action
3,2021-01-06 03:30:46,timeout
3,2021-07-14 14:00:00,timeout
7,2021-06-12 11:57:29,confirmed
7,2021-06-13 12:58:28,confirmed
7,2021-06-14 13:59:27,confirmed
2,2021-01-22 00:00:00,confirmed
2,2021-02-28 23:59:59,timeout"""

# Load data into pandas DataFrames
signups_df = pd.read_csv(StringIO(signups_data))
confirmations_df = pd.read_csv(StringIO(confirmations_data))

# Convert 'time_stamp' columns to datetime
signups_df['time_stamp'] = pd.to_datetime(signups_df['time_stamp'])
confirmations_df['time_stamp'] = pd.to_datetime(confirmations_df['time_stamp'])

# Calculate confirmation rate using pandas
merged_df = pd.merge(signups_df, confirmations_df, on='user_id', how='left')
merged_df['confirmed'] = merged_df['action'].apply(lambda x: 1 if x == 'confirmed' else 0)
confirmation_rate_df = merged_df.groupby('user_id')['confirmed'].mean().reset_index()
confirmation_rate_df.rename(columns={'confirmed': 'confirmation_rate'}, inplace=True)

# Handle users with no confirmations (left join result)
confirmation_rate_df['confirmation_rate'] = confirmation_rate_df['confirmation_rate'].fillna(0)

# Sort by user_id (optional, for clarity)
confirmation_rate_df = confirmation_rate_df.sort_values(by='user_id')

# Display the result
print(confirmation_rate_df)
