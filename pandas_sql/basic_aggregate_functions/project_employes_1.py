"""
Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.


Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee.


Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.

The query result format is in the following example.



Example 1:

Input:
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output:
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

WITH Project AS (
    SELECT 1 AS project_id, 1 AS employee_id UNION ALL
    SELECT 1 AS project_id, 2 AS employee_id UNION ALL
    SELECT 1 AS project_id, 3 AS employee_id UNION ALL
    SELECT 2 AS project_id, 1 AS employee_id UNION ALL
    SELECT 2 AS project_id, 4 AS employee_id
),

Employee AS (
    SELECT 1 AS employee_id, 'Khaled' AS name, 3 AS experience_years UNION ALL
    SELECT 2 AS employee_id, 'Ali' AS name, 2 AS experience_years UNION ALL
    SELECT 3 AS employee_id, 'John' AS name, 1 AS experience_years UNION ALL
    SELECT 4 AS employee_id, 'Doe' AS name, 2 AS experience_years
)

SELECT
 project_id,
 SUM(e.experience_years) / COUNT(DISTINCT p.employee_id)
FROM
    Project p
JOIN Employee e ON p.employee_id=e.employee_id
GROUP BY project_id
"""

import pandas as pd

# Define the Project and Employee data
project_data = {
    'project_id': [1, 1, 1, 2, 2],
    'employee_id': [1, 2, 3, 1, 4]
}

employee_data = {
    'employee_id': [1, 2, 3, 4],
    'name': ['Khaled', 'Ali', 'John', 'Doe'],
    'experience_years': [3, 2, 1, 2]
}

# Create pandas DataFrames from the data
project_df = pd.DataFrame(project_data)
employee_df = pd.DataFrame(employee_data)

# Perform the SQL-like query
result_df = (
    project_df.merge(employee_df, on='employee_id')
              .groupby('project_id')
              .agg({'experience_years': 'mean'})
              .reset_index()
)

# Rename columns to match the output format
result_df = result_df.rename(columns={'experience_years': 'average_years'})

# Display the result
print(result_df)
