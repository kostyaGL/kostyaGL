"""/*
Table: Followers

+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.


Write a solution that will, for each user, return the number of followers.

Return the result table ordered by user_id in ascending order.

The result format is in the following example.



Example 1:

Input:
Followers table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
Output:
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
Explanation:
The followers of 0 are {1}
The followers of 1 are {0}
The followers of 2 are {0,1}
*/

WITH Followers AS (
    SELECT 0 AS user_id, 1 AS follower_id UNION ALL
    SELECT 1 AS user_id, 0 AS follower_id UNION ALL
    SELECT 2 AS user_id, 0 AS follower_id UNION ALL
    SELECT 2 AS user_id, 1 AS follower_id
)
SELECT
    user_id,
    COUNT(follower_id) followers_count
FROM
    Followers
GROUP BY user_id
ORDER BY user_id
"""
import pandas as pd

# Simulating the Followers table
followers = pd.DataFrame({
    'user_id': [0, 1, 2, 2],
    'follower_id': [1, 0, 0, 1]
})

# Counting followers for each user
followers_count = followers.groupby('user_id')['follower_id'].count().reset_index()
followers_count.columns = ['user_id', 'followers_count']

# Sorting by user_id (optional, for displaying the output in the specified order)
followers_count = followers_count.sort_values('user_id')

# Displaying the result
print(followers_count)
