#
# Table: Logs
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# In SQL, id is the primary key for this table.
# id is an autoincrement column.
#
#
# Find all numbers that appear at least three times consecutively.
#
# Return the result table in any order.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Logs table:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+
# Output:
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# Explanation: 1 is the only number that appears consecutively for at least three times.


import pandas as pd

# Define the data in a dictionary format
data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': ['1', '1', '1', '2', '1', '2', '2']
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Identify consecutive groups of the same number
df['group'] = (df['num'] != df['num'].shift(1)).cumsum()

# Calculate the size of each group
df['group_size'] = df.groupby('group')['num'].transform('size')

# Filter for groups where the group size is 3 or more
consecutive_nums = df[df['group_size'] >= 3]['num'].unique()

# Create a new DataFrame with the result
result_df = pd.DataFrame({'ConsecutiveNums': consecutive_nums})

# Display the result
print(result_df)
