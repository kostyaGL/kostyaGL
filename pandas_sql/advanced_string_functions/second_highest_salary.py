# /*
# Table: Employee
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
#
#
# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output:
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# Example 2:
#
# Input:
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output:
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+
# */
#
# WITH Employee AS (
#     SELECT 1 AS id, 100 AS salary
#     UNION ALL
#     SELECT 2, 200
#     UNION ALL
#     SELECT 3, 300
# )
# SELECT max(salary) FROM Employee where salary <(
# SELECT max(salary) FROM Employee);

import pandas as pd

# Sample data for the Employee table
data = {
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
}

# Create the DataFrame
df = pd.DataFrame(data)

print(pd.DataFrame({'SecondHighestSalary': df['salary'].nlargest(1, keep='last')}))

