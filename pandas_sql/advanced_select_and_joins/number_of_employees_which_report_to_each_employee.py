# /*
# Table: Employees
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | reports_to  | int      |
# | age         | int      |
# +-------------+----------+
# employee_id is the column with unique values for this table.
# This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).
#
#
# For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
#
# Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.
#
# Return the result table ordered by employee_id.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Employees table:
# +-------------+---------+------------+-----+
# | employee_id | name    | reports_to | age |
# +-------------+---------+------------+-----+
# | 9           | Hercy   | null       | 43  |
# | 6           | Alice   | 9          | 41  |
# | 4           | Bob     | 9          | 36  |
# | 2           | Winston | null       | 37  |
# +-------------+---------+------------+-----+
# Output:
# +-------------+-------+---------------+-------------+
# | employee_id | name  | reports_count | average_age |
# +-------------+-------+---------------+-------------+
# | 9           | Hercy | 2             | 39          |
# +-------------+-------+---------------+-------------+
# Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
# Example 2:
#
# Input:
# Employees table:
# +-------------+---------+------------+-----+
# | employee_id | name    | reports_to | age |
# |-------------|---------|------------|-----|
# | 1           | Michael | null       | 45  |
# | 2           | Alice   | 1          | 38  |
# | 3           | Bob     | 1          | 42  |
# | 4           | Charlie | 2          | 34  |
# | 5           | David   | 2          | 40  |
# | 6           | Eve     | 3          | 37  |
# | 7           | Frank   | null       | 50  |
# | 8           | Grace   | null       | 48  |
# +-------------+---------+------------+-----+
# Output:
# +-------------+---------+---------------+-------------+
# | employee_id | name    | reports_count | average_age |
# | ----------- | ------- | ------------- | ----------- |
# | 1           | Michael | 2             | 40          |
# | 2           | Alice   | 2             | 37          |
# | 3           | Bob     | 1             | 37          |
# +-------------+---------+---------------+-------------+
# */
import numpy as np
import pandas as pd

# Simulating the Employees table as a pandas DataFrame
data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name': ['Michael', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'reports_to': [np.nan, 1, 1, 2, 2, 3, np.nan, np.nan],
    'age': [45, 38, 42, 34, 40, 37, 50, 48]
}

employees_df = pd.DataFrame(data)

# Perform the transformation similar to the SQL query
# Step 1: Join to find managers and their reports
managers_df = employees_df.merge(employees_df, left_on='employee_id', right_on='reports_to', suffixes=('', '_report'))

# Step 2: Filter to keep only managers who have reports
managers_df = managers_df[managers_df['employee_id_report'].notnull()]

# Step 3: Calculate reports_count and average_age
manager_summary = managers_df.groupby(['employee_id', 'name']).agg({
    'employee_id_report': 'count',
    'age_report': 'mean'
}).reset_index()

manager_summary['average_age'] = manager_summary['age_report'].round().astype(int)

# Step 4: Select and order the required columns
manager_summary = manager_summary[['employee_id', 'name', 'employee_id_report', 'average_age']]

# Display the result
print(manager_summary)
