"""/*
Table: Activity

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
This table may have duplicate rows.
The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
The table shows the user activities for a social media website.
Note that each session belongs to exactly one user.


Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
Output:
+------------+--------------+
| day        | active_users |
+------------+--------------+
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+
Explanation: Note that we do not care about days with zero active users.
*/

WITH UserActivities AS (
    SELECT 1 AS user_id, 1 AS session_id, '2019-07-20' AS activity_date, 'open_session' AS activity_type UNION ALL
    SELECT 1 AS user_id, 1 AS session_id, '2019-07-20' AS activity_date, 'scroll_down' AS activity_type UNION ALL
    SELECT 1 AS user_id, 1 AS session_id, '2019-07-20' AS activity_date, 'end_session' AS activity_type UNION ALL
    SELECT 2 AS user_id, 4 AS session_id, '2019-07-20' AS activity_date, 'open_session' AS activity_type UNION ALL
    SELECT 2 AS user_id, 4 AS session_id, '2019-07-21' AS activity_date, 'send_message' AS activity_type UNION ALL
    SELECT 2 AS user_id, 4 AS session_id, '2019-07-21' AS activity_date, 'end_session' AS activity_type UNION ALL
    SELECT 3 AS user_id, 2 AS session_id, '2019-07-21' AS activity_date, 'open_session' AS activity_type UNION ALL
    SELECT 3 AS user_id, 2 AS session_id, '2019-07-21' AS activity_date, 'send_message' AS activity_type UNION ALL
    SELECT 3 AS user_id, 2 AS session_id, '2019-07-21' AS activity_date, 'end_session' AS activity_type UNION ALL
    SELECT 4 AS user_id, 3 AS session_id, '2019-06-25' AS activity_date, 'open_session' AS activity_type UNION ALL
    SELECT 4 AS user_id, 3 AS session_id, '2019-06-25' AS activity_date, 'end_session' AS activity_type
)
# Write your MySQL query statement below

SELECT
    activity_date as day,
    COUNT(DISTINCT user_id) active_users
FROM
    UserActivities
WHERE
  PARSE_DATE('%Y-%m-%d', activity_date) <= '2019-07-27' AND
  PARSE_DATE('%Y-%m-%d', activity_date) > '2019-06-27'
GROUP BY activity_date
"""
import pandas as pd

# Simulating the UserActivities table
user_activities_data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'session_id': [1, 1, 1, 4, 4, 4, 2, 2, 2, 3, 3],
    'activity_date': ['2019-07-20', '2019-07-20', '2019-07-20', '2019-07-20', '2019-07-21',
                      '2019-07-21', '2019-07-21', '2019-07-21', '2019-07-21', '2019-06-25', '2019-06-25'],
    'activity_type': ['open_session', 'scroll_down', 'end_session', 'open_session', 'send_message',
                      'end_session', 'open_session', 'send_message', 'end_session', 'open_session', 'end_session']
}

user_activities = pd.DataFrame(user_activities_data)

# Converting activity_date column to datetime type
user_activities['activity_date'] = pd.to_datetime(user_activities['activity_date'])

# Filtering activities for the required date range
start_date = pd.to_datetime('2019-06-27')
end_date = pd.to_datetime('2019-07-27')
filtered_activities = user_activities[
    (user_activities['activity_date'] >= start_date) & (user_activities['activity_date'] <= end_date)
]

# Counting active users per day
active_users_per_day = filtered_activities.groupby('activity_date')['user_id'].nunique().reset_index()
active_users_per_day.rename(columns={'activity_date': 'day', 'user_id': 'active_users'}, inplace=True)

print(active_users_per_day)
