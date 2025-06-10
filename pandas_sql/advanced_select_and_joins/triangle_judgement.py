# /*
# Table: Triangle
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.
#
#
# Report for every three line segments whether they can form a triangle.
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
# Triangle table:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# Output:
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+
# */
# WITH Triangle AS (
#     SELECT 13 AS x, 15 AS y, 30 AS z UNION ALL
#     SELECT 10 AS x, 20 AS y, 15 AS z
# )
# SELECT
#     x,y,z,
#     IF(x+y<=z OR z+y<=x OR z+x<=y, 'No', 'Yes') triangle
# FROM
#     Triangle;

import pandas as pd

# Creating the Triangle DataFrame
data = {
    'x': [13, 10],
    'y': [15, 20],
    'z': [30, 15]
}

df = pd.DataFrame(data)


# Function to check if three sides can form a triangle
def check_triangle(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        return 'Yes'
    else:
        return 'No'


# Apply the function to each row in the DataFrame
df['triangle'] = df.apply(lambda row: check_triangle(row['x'], row['y'], row['z']), axis=1)

# Display the result
print(df[['x', 'y', 'z', 'triangle']])
