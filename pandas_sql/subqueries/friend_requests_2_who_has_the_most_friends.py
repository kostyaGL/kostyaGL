"""/*
Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.


Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.



Example 1:

Input:
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output:
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation:
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.


Follow up: In the real world, multiple people could have the same most number of friends. Could you find all these people in this case?
*/

WITH RequestAccepted AS (
    SELECT 1 AS requester_id, 2 AS accepter_id, '2016/06/03' AS accept_date
    UNION ALL
    SELECT 1, 3, '2016/06/08'
    UNION ALL
    SELECT 2, 3, '2016/06/08'
    UNION ALL
    SELECT 3, 4, '2016/06/09'
), foo as (
select accepter_id as id, count(*) as num from RequestAccepted
group by 1
UNION ALL
select requester_id as id, count(*) as num from RequestAccepted
group by 1
)
select id, sum(num) as num from foo
group by id
order by 2 desc limit 1
"""
import pandas as pd

# Simulating the RequestAccepted table
data = {
    'requester_id': [1, 1, 2, 3],
    'accepter_id': [2, 3, 3, 4],
    'accept_date': ['2016/06/03', '2016/06/08', '2016/06/08', '2016/06/09']
}

df = pd.DataFrame(data)

# Step 2: Count friends for each person
requester_counts = df['requester_id'].value_counts()
accepter_counts = df['accepter_id'].value_counts()

# Step 3: Aggregate total friends
all_friends_counts = requester_counts.add(accepter_counts, fill_value=0).astype(int)

# Step 4: Identify person(s) with the maximum friends
max_num_friends = all_friends_counts.max()
max_friends_ids = all_friends_counts[all_friends_counts == max_num_friends].index.tolist()

# Prepare the output DataFrame
output_df = pd.DataFrame({'id': max_friends_ids, 'num': max_num_friends})

print(output_df)
