# /*
# Table: Person
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | email       | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains an email. The emails will not contain uppercase letters.
#
#
# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
#
# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
#
# For Pandas users, please note that you are supposed to modify Person in place.
#
# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Person table:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+
# Output:
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# +----+------------------+
# Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
# */
# WITH Person AS (
#     SELECT 1 AS id, 'john@example.com' AS email
#     UNION ALL
#     SELECT 2, 'bob@example.com'
#     UNION ALL
#     SELECT 3, 'john@example.com'
# )
# SELECT min(id), email FROM Person group by email;

import pandas as pd

# Sample data as defined in the SQL query
person_data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}

# Create pandas DataFrame from the sample data
person_df = pd.DataFrame(person_data)

# Drop duplicates based on 'email', keeping the row with the smallest 'id'
person_df = person_df.sort_values('id').drop_duplicates('email')

# Display the result DataFrame after deletion
print(person_df)

