# --/*
# --
# --Table: Users
# --
# --+----------------+---------+
# --| Column Name    | Type    |
# --+----------------+---------+
# --| user_id        | int     |
# --| name           | varchar |
# --+----------------+---------+
# --user_id is the primary key (column with unique values) for this table.
# --This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
# --
# --
# --Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# --
# --Return the result table ordered by user_id.
# --
# --The result format is in the following example.
# --
# --
# --
# --Example 1:
# --
# --Input:
# --Users table:
# --+---------+-------+
# --| user_id | name  |
# --+---------+-------+
# --| 1       | aLice |
# --| 2       | bOB   |
# --+---------+-------+
# --Output:
# --+---------+-------+
# --| user_id | name  |
# --+---------+-------+
# --| 1       | Alice |
# --| 2       | Bob   |
# --+---------+-------+
# --*/
# --WITH Users AS (
# --    SELECT 1 AS user_id, 'aLice' AS name
# --    UNION ALL
# --    SELECT 2, 'bOB' AS name
# --)
# --SELECT user_id, INITCAP(lower(name)) FROM Users;

import pandas as pd

# Sample data
data = {
    'user_id': [1, 2],
    'name': ['aLice', 'bOB']
}

# Create DataFrame
df = pd.DataFrame(data)

# Apply the function to 'name' column
df['name'] = df['name'].apply(lambda x: x.lower().capitalize())

# Display the result
print(df)
